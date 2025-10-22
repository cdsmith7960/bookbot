def get_num_words(file_path: str) -> int:
    with open(file_path) as file:
        text = file.read()
    return len(text.split())

def char_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            counts[char] = counts.get(char, 0) + 1
        if char.isalpha() == False and char not in counts:
            counts[char] = counts.get(char, 0) + 1
    return counts

def sort_characters(char_counts: dict[str, int]) -> list[dict]:
    char_counts_list = []
    for char, count in char_counts.items():
        char_counts_list.append({'character': char, 'count': count})
    char_counts_list.sort(key=lambda x: x['count'], reverse=True)
    return char_counts_list