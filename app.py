from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load API key from environment variables
API_KEY = os.getenv("SCREENSHOTBASE_API_KEY")

# Ensure the API key is available
if not API_KEY:
    raise ValueError("API key not found. Make sure SCREENSHOTBASE_API_KEY is set in your .env file.")

SCREENSHOTBASE_BASE_ENDPOINT = "https://api.screenshotbase.com/v1/take"

@app.route("/", methods=["GET", "POST"])
def home():
    screenshot_url = None

    if request.method == "POST":
        target_url = request.form.get("url")
        format_ = request.form.get("format", "png")
        full_page = request.form.get('full_page') == 'on'

        params = {
            "url": target_url,
            "format": format_,
            "full_page": int(full_page)
            }
        headers = {"apikey": API_KEY}

        try:
            #Send Get request to ScreenshotBase API
            response = requests.get(SCREENSHOTBASE_BASE_ENDPOINT, params=params, headers=headers, timeout=30)
            response.raise_for_status()

            # Save the returned image
            image_extension = format_ if format_ != 'jpeg' else 'jpg'
            image_path = os.path.join("static", f'screenshot.{image_extension}')
            with open(image_path, "wb") as f:
                f.write(response.content)

            screenshot_url = image_path
        
        except requests.exceptions.RequestException as e:
            print(f"Error capturing screenshot: {e}")

    return render_template("index.html", screenshot=screenshot_url)

if __name__ == "__main__":
    app.run(debug=True)