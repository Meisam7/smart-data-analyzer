def show_menu():
    print("\n==============================")
    print("Smart Data Analyzer")
    print("==============================")
    print("1. Analyze direct text")
    print("2. Exit")


def analyze_direct_text():
    print("\nEnter your text:")
    text = input("> ")

    print("\nYou entered:")
    print(text)


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