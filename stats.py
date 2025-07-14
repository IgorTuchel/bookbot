import sys
def book_analysis(file_path: str) -> str:
        file_contents = get_file_contents(file_path)
        char_content_dict = get_char_count(file_contents)
        word_count = get_word_count(file_contents)
        char_count = sort_dict(char_content_dict)
        generate_report(file_path,word_count,char_count)

def get_file_contents(file_path: str) -> str:
    try:
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
    except Exception as e:
         print(f"An error occured trying to get file contents! \nException: {e}")
         sys.exit(1)
    
def get_char_count(text: str) -> dict:
    contents_dict = {}
    for i in text.lower():
        if i.isalpha():
            if i in contents_dict:
                contents_dict[i] += 1
            else:
                contents_dict[i] = 1
    return contents_dict

def get_word_count(text: str) -> int:
    return len(text.split())

def sort_dict(contents_dict: dict) -> list[dict]:
    sorted_list = []
    for dic in contents_dict:
        sorted_list.append({"char": f"{dic}", "num":contents_dict[dic]})
    sorted_list.sort(reverse=True,key=lambda items: items['num'])
    return sorted_list


def generate_report(file_path: str, word_count: int, char_count: list[dict]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for chars in char_count:
        print(f"{chars['char']}: {chars['num']}")
    print("============= END ===============")