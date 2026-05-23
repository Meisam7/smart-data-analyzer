import re


def show_menu():
    print("\n==============================")
    print("Smart Data Analyzer")
    print("==============================")
    print("1. Analyze direct text")
    print("2. Analyze text file")
    print("3. Exit")


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
    """
    Clean one word by removing punctuation and converting it to lowercase.
    Example: 'Python!' becomes 'python'
    """
    cleaned = word.strip(".,!?;:()[]{}\"'")
    cleaned = cleaned.lower()
    return cleaned


def get_words(text):
    """
    Convert text into a list of clean words.
    """
    raw_words = text.split()
    clean_words = []

    for word in raw_words:
        cleaned = clean_word(word)

        if cleaned != "":
            clean_words.append(cleaned)

    return clean_words


def get_most_common_words(text, limit=10):
    """
    Count words using a dictionary and return the most common words.
    """
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
    """
    Find email addresses inside text using regex.
    """
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    emails = re.findall(email_pattern, text)
    return emails


def find_urls(text):
    """
    Find URLs inside text using regex.
    """
    url_pattern = r"https?://[^\s]+"
    urls = re.findall(url_pattern, text)
    return urls


def print_result(line_count, word_count, character_count, common_words, emails, urls):
    print("\n===== Analysis Result =====")
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {character_count}")

    print("\nMost common words:")
    for word, count in common_words:
        print(f"- {word}: {count}")

    print("\nEmails found:")
    if len(emails) > 0:
        for email in emails:
            print(f"- {email}")
    else:
        print("No emails found.")

    print("\nURLs found:")
    if len(urls) > 0:
        for url in urls:
            print(f"- {url}")
    else:
        print("No URLs found.")


def analyze_text(text):
    line_count = count_lines(text)
    word_count = count_words(text)
    character_count = count_characters(text)
    common_words = get_most_common_words(text)
    emails = find_emails(text)
    urls = find_urls(text)

    print_result(
        line_count,
        word_count,
        character_count,
        common_words,
        emails,
        urls
    )


def analyze_direct_text():
    print("\nEnter your text:")
    text = input("> ")

    analyze_text(text)


def read_text_file(file_path):
    file = open(file_path, "r", encoding="utf-8")
    text = file.read()
    file.close()

    return text


def analyze_text_file():
    file_path = input("\nEnter file path: ").strip()

    try:
        text = read_text_file(file_path)
        analyze_text(text)
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
    except Exception as error:
        print(f"Unexpected error: {error}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            analyze_direct_text()
        elif choice == "2":
            analyze_text_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()