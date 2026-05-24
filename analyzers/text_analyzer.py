import re


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


def analyze_text_content(text):
    line_count = count_lines(text)
    word_count = count_words(text)
    character_count = count_characters(text)
    common_words = get_most_common_words(text)
    emails = find_emails(text)
    urls = find_urls(text)

    result = {
        "line_count": line_count,
        "word_count": word_count,
        "character_count": character_count,
        "most_common_words": common_words,
        "emails": emails,
        "urls": urls
    }

    return result