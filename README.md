# YouTube Selenium Automation

A Python browser automation project using Selenium WebDriver to demonstrate automated navigation and interaction with YouTube.

## Overview

This project automates a basic YouTube browsing workflow, reducing repetitive manual steps and demonstrating browser automation fundamentals.

## Features

- Launches Google Chrome using Selenium WebDriver
- Opens YouTube automatically
- Searches for a configurable tutorial or keyword
- Opens the first matching video
- Waits for page elements using explicit waits
- Attempts to open the Share dialog
- Handles common automation errors
- Closes the browser safely after execution

## Technology Stack

- **Language:** Python
- **Automation Framework:** Selenium WebDriver
- **Browser:** Google Chrome
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## Project Structure

```text
YouTube-Selenium-Automation/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

- Python 3.10 or later
- Google Chrome
- Git
- Visual Studio Code (recommended)

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Enter the project directory:

   ```bash
   cd YouTube-Selenium-Automation
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate it on Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the Project

Execute:

```bash
python main.py
```

Chrome will open, navigate to YouTube, search for the configured query, open the first result, and attempt to open the Share dialog.

## Configuration

Edit the `SEARCH_QUERY` variable in `main.py` to search for a different keyword or tutorial.

## Learning Outcomes

- Browser automation with Selenium
- Locating web elements using XPath and HTML attributes
- Explicit waits and clickable element detection
- Handling exceptions in automation scripts
- Managing Python dependencies and virtual environments
- Version control and GitHub project documentation

## Limitations

- YouTube may change its page layout, labels, or element attributes.
- Search results may vary.
- A successful run depends on network connectivity and page availability.
- This project does not automatically like videos or subscribe to channels.
- It is a learning demonstration, not an official YouTube API integration.

## Responsible Use

Use browser automation responsibly and respect the platform's terms and applicable policies. Do not use automation to generate artificial engagement, spam, or perform actions without authorization.

## License

This project is available under the MIT License. See `LICENSE` for details.