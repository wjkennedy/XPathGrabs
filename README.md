# XPath Screenshot Tool

This tool allows you to capture screenshots of specific elements on a webpage by providing their XPath. It uses Selenium for web scraping and Streamlit for the user interface, packaged into a Docker container.

---

## Features
- Capture screenshots of elements by specifying their XPaths.
- Headless browser execution using Selenium.
- Interactive web-based interface powered by Streamlit.
- Screenshots saved locally for easy access.

---

## Prerequisites
1. Docker installed on your system.
2. Ensure you have access to a website and the required XPaths for the elements you want to capture.

---

## Bootstrap the Container

1. **Build the Docker Image**
   ```bash
   docker build -t xpath-screenshot-tool .
   ```

2. **Run the Container**
   ```bash
   docker run --rm -p 8501:8501 -v $(pwd)/screenshots:/app/screenshots xpath-screenshot-tool
   ```

   - **`-p 8501:8501`**: Maps the Streamlit app to port 8501 on your machine.
   - **`-v $(pwd)/screenshots:/app/screenshots`**: Maps the local `screenshots` directory for saving images.

---

## Access the Application

1. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

2. Fill in the following fields:
   - **Website URL**: URL of the webpage.
   - **Personal Access Token**: (Optional) Token for authentication.
   - **XPaths**: List of XPaths, one per line, for the elements you want to capture.

3. Click **Capture Screenshots** to process the request.

---

## Output

- Screenshots will be saved in the `screenshots` folder in your current directory.
- They will also be displayed directly in the web interface.

---

## Troubleshooting

1. **Element Not Found**:
   - Verify the XPath in your browser's developer tools.
   - Ensure the element is visible and loaded.

2. **Dynamic Content Issues**:
   - Increase the timeout for elements in the script.

3. **iframes**:
   - If elements are inside iframes, ensure the tool is updated to handle them.

