import requests

from analyzers.text_analyzer import analyze_text_content
from analyzers.file_handler import read_text_file, save_result_as_json
from analyzers.web_analyzer import get_web_page_text
from analyzers.visualizer import create_word_frequency_chart
from database.db_manager import (
    create_database,
    save_analysis_to_database,
    get_analysis_history
)


def show_menu():
    print("\n==============================")
    print("Smart Data Analyzer")
    print("==============================")
    print("1. Analyze direct text")
    print("2. Analyze text file")
    print("3. Analyze web page")
    print("4. Show analysis history")
    print("5. Exit")


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


def ask_to_save_json(result):
    choice = input("\nDo you want to save the result as JSON? (y/n): ").strip().lower()

    if choice == "y":
        output_path = input("Enter output file path, for example data/result.json: ").strip()
        save_result_as_json(result, output_path)
        print(f"Result saved to {output_path}")
    else:
        print("Result was not saved.")


def ask_to_create_chart(result):
    choice = input("\nDo you want to create a word-frequency chart? (y/n): ").strip().lower()

    if choice == "y":
        output_path = input("Enter chart file path, for example reports/word_frequency.png: ").strip()
        create_word_frequency_chart(result["most_common_words"], output_path)
        print(f"Chart saved to {output_path}")
    else:
        print("Chart was not created.")


def analyze_text(text, source_type, source_name):
    result = analyze_text_content(text)

    print_result(result)
    save_analysis_to_database(source_type, source_name, result)
    ask_to_save_json(result)
    ask_to_create_chart(result)


def analyze_direct_text():
    print("\nEnter your text:")
    text = input("> ")

    analyze_text(text, "direct_text", "user_input")


def analyze_text_file():
    file_path = input("\nEnter file path: ").strip()

    try:
        text = read_text_file(file_path)
        analyze_text(text, "file", file_path)
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as error:
        print(f"Unexpected error: {error}")


def analyze_web_page():
    url = input("\nEnter web page URL: ").strip()

    try:
        text = get_web_page_text(url)
        analyze_text(text, "web", url)
    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


def show_analysis_history():
    rows = get_analysis_history()

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