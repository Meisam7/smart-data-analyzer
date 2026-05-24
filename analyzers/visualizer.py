import matplotlib.pyplot as plt


def create_word_frequency_chart(common_words, output_path):
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