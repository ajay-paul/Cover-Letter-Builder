# Cover Letter Builder

**Cover Letter Builder** is a tool designed to help users quickly generate professional cover letters tailored to specific job positions.

[![Watch the video](https://img.youtube.com/vi/HvSreeG3ekM/0.jpg)](https://www.youtube.com/watch?v=HvSreeG3ekM)

---

# Demo


https://github.com/user-attachments/assets/4adcbe9e-0e35-4350-957d-7439c7077112
# Installation

To use this project, you need Python 3.10+. Follow these steps to set up the environment:

### Clone the repository:

```bash
git clone https://github.com/ajay-paul/Cover-Letter-Builder.git
cd Cover-Letter-Builder
```

# Setup Instructions

1. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Download and configure the LLaMA model**:
   - You may follow here to setup [Ollama](docs/ollama.md) and LLaMA model for language processing.

4. **Web Driver Setup for Selenium**:
   - Selenium requires a web driver to control browsers.

   ### Using Edge WebDriver (Windows)
   Edge WebDriver comes pre-installed on Windows. Ensure your Edge and WebDriver versions match:
   1. Check your Edge version under **Settings > About Microsoft Edge**.
   2. Download the matching WebDriver from [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) if needed.
   3. Add WebDriver to your system PATH.

   ### Using Chrome WebDriver
   1. Download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) matching your Chrome version.
   2. Unzip and add it to your PATH.

   ### Using Firefox WebDriver
   1. Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases).
   2. Extract and add it to your PATH.
> ⚠️ **Note:**  
> If you're using a web driver other than Edge, make sure to import the appropriate driver.

5. **Tesseract OCR**:
   - For Tesseract, you may need to install it separately.

   ### Installation:
   - **Windows**: Download the installer from [Tesseract OCR's official website](https://github.com/tesseract-ocr/tesseract) and follow the installation instructions.
   - **macOS**: Install via Homebrew:
     ```bash
     brew install tesseract
     ```
   - **Linux**: Install via your package manager:
     - For Ubuntu/Debian:
       ```bash
       sudo apt-get install tesseract-ocr
       ```
     - After installation, make sure to add Tesseract to your system's PATH.

## Custom Information 

1. **Define URL in `const.py`**: 
   - Update the `const.py` file with the appropriate URL for the model to access necessary resources.

2. **Configure Your Profile Information**: 
   - Customize your profile with details such as **Experience**, **Skills**, and other relevant information in `const.py` to tailor the cover letter content.

3. **Add Custom Prompt in `model.py`**:
   - You can provide an additional prompt to the model in the `model.py` file. For example:

   ```python
   response = ollama.chat(
       model='llama3.2',
       messages=[
           {
               'role': 'user',
               'content': (
                   'Based on the web-scraped data, write a cover letter in English for the position. '
                   'You may start with my address, then the company address at the top, then '
                   'start with "Hello Recruiting Team,":\n '
                   'Show my deep motivation for the position\n '
                   f'{job_description}.\n'
                   'Additional information about myself:\n'
                   f'{PROFILE}\n'
                   'Tailor the application to align closely with the specific requirements outlined in the job description.\n'
                   'Job found on your career page.\n'
               ),
           },
       ]
   )
    ```
## To Run the Program

Navigate to the project directory and run the main file:

```bash
cd Cover-Letter-Builder
python -m src.main
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.



