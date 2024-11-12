import asyncio
import ollama
import os
import sys
import time
import threading
from docx import Document
from src.constants import PROFILE 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.processing.text_extractor import process_text_extraction

def loading_animation():
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    idx = 0
    while not stop_loading:
        elapsed_time = time.time() - start_time
        sys.stdout.write(f"\rGenerating Cover Letter... {animation[idx % len(animation)]} {elapsed_time:.1f}s")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)

async def generate_cover_letter(job_description):
    # Fetch job description from process_text_extraction
    job_description = await process_text_extraction()
    print(f"Job description fetched! \n")

    global stop_loading
    stop_loading = False
    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()

    try:
        # Run the model request
        response = ollama.chat(
            model='llama3.2',
            messages=[
                {
                    'role': 'user',
                    'content': (
                        'Based on the web-scraped data, write a cover letter in English for the position. '
                        'You may start with my address, then the company address, then '
                        'start with "Hello Recruiting Team,":\n '
                        'show my deep motivation for the position\n '
                        f'{job_description}.\n'
                        'Additional Information about myself:\n'
                        f'{PROFILE}'
                        'Tailor the application to align closely with the specific requirements outlined in the job description'
                        'Job found on your career page\n'
                    ),
                },
            ]
        )

    finally:
        stop_loading = True
        loading_thread.join()

    # Extract the content and save to a .docx file
    cover_letter_content = response['message']['content']
    print("\nGenerated Cover Letter:\n" + cover_letter_content)
    save_to_docx(cover_letter_content, "cover_letter.docx")

def save_to_docx(content, filename="output.docx"):
    # Create a new Document
    doc = Document()
    doc.add_paragraph(content)
    doc.save(filename)
    print(f"Content saved to {filename}")

if __name__ == "__main__":
    asyncio.run(generate_cover_letter())
