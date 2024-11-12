import sys
import os
import asyncio

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.processing.text_extractor import process_text_extraction
from src.processing.model import generate_cover_letter

async def main():
    job_description = await process_text_extraction()
    
    await generate_cover_letter(job_description)

if __name__ == "__main__":
    asyncio.run(main())

# python -m src.main