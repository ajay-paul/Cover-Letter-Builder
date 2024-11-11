import asyncio
import base64
import time
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler
from src.utils import save_image, extract_text_from_image
from src.constants import URL 
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Function to take a full-page screenshot using Selenium and extract text
def capture_full_page_screenshot_with_selenium():
    edge_options = Options()
    edge_options.use_chromium = True
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
    driver.get(URL)
    time.sleep(5)

    total_width = driver.execute_script("return document.body.scrollWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(total_width, total_height)
    time.sleep(2)

    screenshot_data = driver.get_screenshot_as_png()
    save_image(screenshot_data, "utils/full_page_screenshot.png")  # Save using helper function
    driver.quit()

    text = extract_text_from_image(screenshot_data)
    return text

# Async function to fetch content and take screenshot using AsyncWebCrawler
async def fetch_and_take_screenshot():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=URL, screenshot=True)
        scrapped = result.success

        if scrapped:
            soup = BeautifulSoup(result.html, "html.parser")
            text_content_crawler = soup.get_text()

            screenshot_data = base64.b64decode(result.screenshot)
            save_image(screenshot_data, "utils/screenshot.png")  # Save using helper function

            extracted_text = extract_text_from_image(screenshot_data)
            char_count = len(extracted_text)
            print("Extracted Text Character Count:", char_count)

            if char_count < 1700:
                print("Text is less than 1700 characters; falling back to Selenium for full-page screenshot.")
                text_selenium = capture_full_page_screenshot_with_selenium()
                char_count_selenium = len(text_selenium)
                print("Extracted Text Character Count:", char_count_selenium)

                if char_count_selenium < 1700:
                    print("Text is less than 1700 characters; text_content_crawler")
                    print(text_content_crawler)
        else:
            print("Scraping failed. Falling back to Selenium for full-page screenshot.")
            text_selenium = capture_full_page_screenshot_with_selenium()

# Main function to initiate the scraping process
async def process_text_extraction():
    await fetch_and_take_screenshot()
