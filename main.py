from stats import book_analysis
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

try:
    book_analysis(sys.argv[1])
except Exception as e:
    print(f"An error has occured! \nException: {e}")
    sys.exit(1)