## Web Scraper
## This script downloads a simple web page, extracts headings, and saves them to CSV.
## It uses sample data if the website cannot be reached.

import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def get_headlines() -> list[str]:
    url = "https://www.python.org/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.select("div.supplemental a")
        headlines = [link.get_text(strip=True) for link in links[:5] if link.get_text(strip=True)]

        if headlines:
            return headlines
    except requests.RequestException as exc:
        print(f"Could not fetch the website: {exc}")

    return [
        "Python News 1",
        "Python News 2",
        "Python News 3",
        "Python News 4",
        "Python News 5",
    ]


def save_to_csv(headlines: list[str], output_file: str | None = None) -> Path:
    output_path = Path(output_file or Path(__file__).with_name("python_headlines.csv"))

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["headline"])
        for headline in headlines:
            writer.writerow([headline])

    return output_path


if __name__ == "__main__":
    headlines = get_headlines()
    output_path = save_to_csv(headlines)

    print("Scraped headlines:")
    for headline in headlines:
        print(f"- {headline}")
    print(f"\nSaved to: {output_path}")
