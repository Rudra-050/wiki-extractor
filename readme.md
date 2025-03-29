# Wikipedia Summary Extractor

## 📌 Overview
This Python tool fetches Wikipedia article summaries using web scraping (requests & BeautifulSoup) instead of the Wikipedia API. Extracted summaries are stored in summaries.json.




## 🚀 Features


Extracts Wikipedia summaries via web scraping.

Stores summaries locally for offline access.

Handles errors for invalid or ambiguous topics.

Includes unit tests for reliability.
## Project Structure

wiki_summary_extractor/
│── utilities/
│   ├── fetch.py  # Scraper & summary saver
│── testing/
│   ├── test.py  # Unit tests
│── data/
│   ├── summaries.json  # Stored summaries
│── README.md  # Documentation
│── requirements.txt  # Dependencies
│── main.py  # Optional entry point

## Working
1.The user inputs a Wikipedia topic.
2.The script fetches and parses the page content.
3.Handles errors gracefully:
   - If multiple results, it suggests options.
   - If no page exists, it alerts the user.
3.Extracted summary is displayed and stored in summaries.json.

## 🛠️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/rudra-0501/wiki_summary_extractor.git
   cd wiki_summary_extractor