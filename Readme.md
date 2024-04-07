# Web Scraping Project: Flag Finder

This project is designed to scrape flags from a designated website, navigating through various pages and capturing flag identifiers using a combination of Python, Selenium, and object-oriented programming principles. The project structure emphasizes modularity, readability, and reusability of code.

## Overview

The `Flag Finder` project consists of three main components:

- `DriverWrapper`: Manages Selenium WebDriver interactions, providing a simplified interface for page navigation and element interactions.
- `FlagScraper`: Contains the scraping logic to extract flags from web pages using specific selectors and patterns.
- `FlagFinder`: Orchestrates the scraping process by utilizing `DriverWrapper` and `FlagScraper` to navigate through pages and collect flag data.

## Setup

### Prerequisites

- Python 3.x
- Selenium
- WebDriver Manager for Python

### Installation

1. Clone the repository or download the source code.
2. Ensure Python 3.x is installed on your system.
3. Install required Python packages:

```sh
pip install selenium webdriver_manager
```

### Usage
To run the scraper, navigate to the project directory in your terminal and execute:

```
python FlagFinder.py
```

The script will automatically open a browser window, navigate through the specified pages, and print the collected flags to the console.

### Components

### DriverWrapper
1. Manages the Selenium Webdriver
2. Simplifies page navigation and element interaction methods.
3. Ensures the script waits efficiently for elements before interacting.

### FlagScraper
1. Defines methods for extracting flag data from web pages.
2. Utilizes `DriverWrapper` for all web interactions.
3. Stores collected flags and prints them upon completion.

### FlagFinder
1. Initializes `DriverWrapper` and `FlagScraper` with the target base URL.
2. Orchestrates the scraping process by specifying which pages to vist and what actions to perform.
3. Collects and prints all flags found during the scraping session.

### Contributions
Contributions are welcome! If you have improvements or bug fixes, please open a pull request or issue.

### License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
