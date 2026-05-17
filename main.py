def show_menu():
    print("\n==============================")
    print("Smart Data Analyzer")
    print("==============================")
    print("1. Analyze direct text")
    print("2. Exit")


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


def analyze_direct_text():
    print("\nEnter your text:")
    text = input("> ")

    line_count = count_lines(text)
    word_count = count_words(text)
    character_count = count_characters(text)

    print("\n===== Analysis Result =====")
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {character_count}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            analyze_direct_text()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()