import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time



def capture_screenshot_with_xpath(url, username, token, xpaths, output_dir="screenshots"):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Add Authorization header (username:token as Base64 for Basic Auth)
    auth_string = f"{username}:{token}"
    chrome_options.add_argument(f"--header=Authorization: Basic {auth_string}")

    # Initialize WebDriver
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)

    results = []

    try:
        # Open the website
        driver.get(url)
        time.sleep(3)  # Allow time for the page to load

        for i, xpath in enumerate(xpaths):
            try:
                element = driver.find_element(By.XPATH, xpath)
                screenshot_path = os.path.join(output_dir, f"screenshot_{i+1}.png")
                element.screenshot(screenshot_path)
                results.append(f"Screenshot saved at: {screenshot_path}")
            except Exception as e:
                results.append(f"Failed to capture element with XPath: {xpath}. Error: {e}")

    finally:
        driver.quit()

    return results


# Streamlit App
st.title("XPath-Based Screenshot Tool")

# Inputs from the user

# Streamlit App
st.sidebar.header("Inputs")
url = st.sidebar.text_input("Website URL", "https://example.com")
username = st.sidebar.text_input("Username/Email", "your_username")
token = st.sidebar.text_input("Personal Access Token", type="password")
xpaths = st.sidebar.text_area(
    "XPaths (one per line)", 
    "//div[@id='example-id']\n//span[contains(text(), 'Example Text')]"
)
output_dir = "screenshots"

# Submit button
if st.sidebar.button("Capture Screenshots"):
    st.info("Processing...")
    xpaths_list = xpaths.splitlines()
    results = capture_screenshot_with_xpath(url, username, token, xpaths_list, output_dir)


    # Display results
    for result in results:
        st.write(result)

    # Show screenshots
    if os.path.exists(output_dir):
        st.header("Screenshots")
        for file_name in os.listdir(output_dir):
            st.image(os.path.join(output_dir, file_name), caption=file_name)


