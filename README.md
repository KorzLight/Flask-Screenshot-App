# Website Screenshot Generator

A simple web application built with Python and Flask that allows users to enter a website URL and instantly see a screenshot of that page.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration & Environment](#configuration--environment)
- [Customization Options](#customization-options)

## Overview
This project uses the Flask web framework to provide a simple form where users can enter a URL. The backend sends the URL to a screenshot API (such as ScreenshotBase), receives the image, saves it, and displays it in the browser. It can be used for website previews, monitoring, or quick captures.

## Features
- Enter any website URL and get a screenshot.
- Built with Python and Flask.
- Uses a third-party REST API to capture screenshots.
- Simple responsive frontend using Bootstrap.
- Optional settings for format, viewport, and full-page capture.

## Prerequisites
Before starting, you should have:
- Python 3.9 or higher installed.
- Basic understanding of Python and Flask.
- An API key for a screenshot API (such as ScreenshotBase).
- A code editor and terminal for running Flask.

## Getting Started
1. Clone or download the project folder.
2. Create and activate a virtual environment.
3. Install the required packages: Flask and requests.
4. Set your screenshot API key as an environment variable (for example SCREENSHOTBASE_API_KEY).
5. Run the Flask app in development mode and open it in your browser (http://127.0.0.1:5000).
6. Enter a URL and submit to view the screenshot.

## Usage
- Open the app in your browser.
- Enter a valid website URL and submit.
- Wait for the screenshot to load.
- The image will appear on the page and be saved in the static folder.
- If an error occurs, an error message will be displayed.

## Configuration & Environment
- Store your API key in an environment variable (SCREENSHOTBASE_API_KEY).
- Update the API endpoint in app.py if needed (for example https://api.screenshotbase.com/v1/take).
- Make sure the static folder has write permissions.
- Turn off debug mode in production with app.run(debug=False).

## Customization Options
You can modify screenshot options such as:
- Format (PNG, JPG, GIF, WEBP)
- Full-page or viewport capture
- Viewport width and height to simulate different devices
- Unique filenames or batch captures
