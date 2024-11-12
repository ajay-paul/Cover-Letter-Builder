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
    save_image(screenshot_data, "utils/full_page_screenshot.png")
    driver.quit()

    return extract_text_from_image(screenshot_data)

# Async function to fetch content
async def fetch_and_take_screenshot():
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=URL, screenshot=True)
        if result.success:
            soup = BeautifulSoup(result.html, "html.parser")
            text_content_crawler = soup.get_text()

            screenshot_data = base64.b64decode(result.screenshot)
            save_image(screenshot_data, "utils/screenshot.png")

            extracted_text = extract_text_from_image(screenshot_data)
            char_count = len(extracted_text)
            
            if char_count >= 1700:
                print("Using text extracted from AsyncWebCrawler.")
                return extracted_text
            elif len(text_content_crawler) >= 1700:
                print("Using text content from web crawler (HTML text).")
                return text_content_crawler
            else:
                print("Fallback to Selenium")
                return capture_full_page_screenshot_with_selenium()
        else:
            print("AsyncWebCrawler scraping failed. Using Selenium for fallback.")
            return capture_full_page_screenshot_with_selenium()

# Wrapper to process the final extracted text
async def process_text_extraction():
    final_text_model = await fetch_and_take_screenshot()
    # print(f'Final text for model:\n{final_text_model}')
    return final_text_model

# Execute the process
if __name__ == "__main__":
    asyncio.run(process_text_extraction())
