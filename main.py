import sys
import stats

def print_help():
    print("Usage: python3 main.py <path_to_book>")

def report_for(book_file: str):
    text = stats.get_book_text(book_file)
    char_rpt = stats.get_char_counts(text)
    wc = stats.get_word_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    print(stats.char_count_report(char_rpt))
    
def main():
    if len(sys.argv) != 2 :
        print_help()
        sys.exit(1)
    report_for(sys.argv[1])

if __name__ == "__main__":
    main()
