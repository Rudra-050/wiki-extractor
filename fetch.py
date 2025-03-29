import requests
import json
from bs4 import BeautifulSoup

def get_summary(topic, sentences=3):
    """Scrapes Wikipedia for a topic's summary and saves it to summaries.json."""
    search_url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    
    try:
        response = requests.get(search_url)
        response.raise_for_status()  # Raise an error for bad responses (404, etc.)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the first paragraph in the article
        paragraphs = soup.select("p")  # Select all paragraphs
        for para in paragraphs:
            if para.text.strip():  # Ignore empty paragraphs
                summary = " ".join(para.text.strip().split(". ")[:sentences]) + "."
                
                # Save summary to summaries.json
                save_summary(topic, summary)
                
                return summary

        return "No summary found for this topic."
    
    except requests.exceptions.RequestException:
        return f"Could not fetch data for '{topic}'. Check your internet connection or the topic spelling."

def save_summary(topic, summary):
    """Saves the extracted summary to summaries.json."""
    try:
        with open("data/summaries.json", "r") as file:
            summaries = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        summaries = {}
    
    summaries[topic] = summary
    
    with open("data/summaries.json", "w") as file:
        json.dump(summaries, file, indent=4)

# Example Usage
if __name__ == "__main__":
    topic = input("Enter a Wikipedia topic: ")
    print(get_summary(topic))
