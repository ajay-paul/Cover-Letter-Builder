import sys
import os
import asyncio

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.constants import URL 
from src.processing import process_text_extraction

if __name__ == "__main__":
    asyncio.run(process_text_extraction())
