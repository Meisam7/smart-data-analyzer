import re
import json
import sqlite3
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def show_menu():
    print("\n==============================")
    print("Smart Data Analyzer")
    print("==============================")
    print("1. Analyze direct text")
    print("2. Analyze text file")
    print("3. Analyze web page")
    print("4. Show analysis history")
    print("5. Exit")


def count_lines(text):
    lines = text.splitlines()

    if len(lines) == 0:
        return 1

    return len(lines)


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    return len(text)


def clean_word(word):
    cleaned = word.strip(".,!?;:()[]{}\"'")
    cleaned = cleaned.lower()
    return cleaned


def get_words(text):
    raw_words = text.split()
    clean_words = []

    for word in raw_words:
        cleaned = clean_word(word)

        if cleaned != "":
            clean_words.append(cleaned)

    return clean_words


def get_most_common_words(text, limit=10):
    words = get_words(text)
    word_counts = {}

    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] = word_counts[word] + 1

    word_items = list(word_counts.items())
    word_items.sort(key=lambda item: item[1], reverse=True)

    return word_items[:limit]


def find_emails(text):
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    emails = re.findall(email_pattern, text)
    return emails


def find_urls(text):
    url_pattern = r"https?://[^\s]+"
    urls = re.findall(url_pattern, text)
    return urls


def create_result_dictionary(line_count, word_count, character_count, common_words, emails, urls):
    result = {
        "line_count": line_count,
        "word_count": word_count,
        "character_count": character_count,
        "most_common_words": common_words,
        "emails": emails,
        "urls": urls
    }

    return result


def print_result(result):
    print("\n===== Analysis Result =====")
    print(f"Lines: {result['line_count']}")
    print(f"Words: {result['word_count']}")
    print(f"Characters: {result['character_count']}")

    print("\nMost common words:")
    for word, count in result["most_common_words"]:
        print(f"- {word}: {count}")

    print("\nEmails found:")
    if len(result["emails"]) > 0:
        for email in result["emails"]:
            print(f"- {email}")
    else:
        print("No emails found.")

    print("\nURLs found:")
    if len(result["urls"]) > 0:
        for url in result["urls"]:
            print(f"- {url}")
    else:
        print("No URLs found.")


def save_result_as_json(result, output_path):
    file = open(output_path, "w", encoding="utf-8")
    json.dump(result, file, indent=4)
    file.close()


def ask_to_save_json(result):
    choice = input("\nDo you want to save the result as JSON? (y/n): ").strip().lower()

    if choice == "y":
        output_path = input("Enter output file path, for example data/result.json: ").strip()
        save_result_as_json(result, output_path)
        print(f"Result saved to {output_path}")
    else:
        print("Result was not saved.")


def create_word_frequency_chart(common_words, output_path):
    """
    Create and save a bar chart for the most common words.
    """
    if len(common_words) == 0:
        print("No words available for chart.")
        return

    words = []
    counts = []

    for word, count in common_words:
        words.append(word)
        counts.append(count)

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.title("Most Common Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def ask_to_create_chart(result):
    choice = input("\nDo you want to create a word-frequency chart? (y/n): ").strip().lower()

    if choice == "y":
        output_path = input("Enter chart file path, for example reports/word_frequency.png: ").strip()
        create_word_frequency_chart(result["most_common_words"], output_path)
        print(f"Chart saved to {output_path}")
    else:
        print("Chart was not created.")

def create_database():
    connection = sqlite3.connect("analysis.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type TEXT NOT NULL,
            source_name TEXT NOT NULL,
            line_count INTEGER,
            word_count INTEGER,
            character_count INTEGER,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_analysis_to_database(source_type, source_name, result):
    connection = sqlite3.connect("analysis.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analyses (
            source_type,
            source_name,
            line_count,
            word_count,
            character_count,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        source_type,
        source_name,
        result["line_count"],
        result["word_count"],
        result["character_count"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def show_analysis_history():
    connection = sqlite3.connect("analysis.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, source_type, source_name, line_count, word_count, character_count, created_at
        FROM analyses
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    connection.close()

    print("\n===== Analysis History =====")

    if len(rows) == 0:
        print("No analysis history found.")
        return

    for row in rows:
        analysis_id = row[0]
        source_type = row[1]
        source_name = row[2]
        line_count = row[3]
        word_count = row[4]
        character_count = row[5]
        created_at = row[6]

        print(
            f"{analysis_id}. [{source_type}] {source_name} | "
            f"Lines: {line_count}, Words: {word_count}, Characters: {character_count} | "
            f"{created_at}"
        )


def analyze_text(text, source_type, source_name):
    line_count = count_lines(text)
    word_count = count_words(text)
    character_count = count_characters(text)
    common_words = get_most_common_words(text)
    emails = find_emails(text)
    urls = find_urls(text)

    result = create_result_dictionary(
        line_count,
        word_count,
        character_count,
        common_words,
        emails,
        urls
    )

    print_result(result)
    save_analysis_to_database(source_type, source_name, result)
    ask_to_save_json(result)
    ask_to_create_chart(result)


def analyze_direct_text():
    print("\nEnter your text:")
    text = input("> ")

    analyze_text(text, "direct_text", "user_input")


def read_text_file(file_path):
    file = open(file_path, "r", encoding="utf-8")
    text = file.read()
    file.close()

    return text


def analyze_text_file():
    file_path = input("\nEnter file path: ").strip()

    try:
        text = read_text_file(file_path)
        analyze_text(text, "file", file_path)
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as error:
        print(f"Unexpected error: {error}")


def get_web_page_text(url):
    """
    Download a web page and extract readable text from HTML.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    return text


def analyze_web_page():
    url = input("\nEnter web page URL: ").strip()

    try:
        text = get_web_page_text(url)
        analyze_text(text, "web", url)
    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


def main():
    create_database()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            analyze_direct_text()
        elif choice == "2":
            analyze_text_file()
        elif choice == "3":
            analyze_web_page()
        elif choice == "4":
            show_analysis_history()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()