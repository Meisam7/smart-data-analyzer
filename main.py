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


def print_result(line_count, word_count, character_count):
    print("\n===== Analysis Result =====")
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {character_count}")


def analyze_text(text):
    line_count = count_lines(text)
    word_count = count_words(text)
    character_count = count_characters(text)

    print_result(line_count, word_count, character_count)


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