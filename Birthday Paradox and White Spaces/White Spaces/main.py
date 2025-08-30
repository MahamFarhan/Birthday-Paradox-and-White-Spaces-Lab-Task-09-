from WhiteSpace import WordCounter
def main():
    try:
        sentence = input("Enter a sentence (words separated by spaces): ")
        wc = WordCounter(sentence)
        
        wc.repetitions()  # process words
        print(wc)         # uses __str__ method

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()