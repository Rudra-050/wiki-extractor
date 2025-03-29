from utilities.fetch import get_summary

def main():
    print("Wikipedia Summary Extractor")
    topic = input("Enter a topic to search: ")
    summary = get_summary(topic)
    print("\nSummary:\n", summary)

if __name__ == "__main__":
    main()
