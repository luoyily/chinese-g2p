import json

index = json.load(open("index_常用读音_概率合并.json", "r", encoding="utf-8"))
words = json.load(open("words.json", "r", encoding="utf-8"))

sm = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j",
      "q", "x", "zh", "ch", "sh", "r", "z", "c", "s", "w", "y"]
tone_map = {
    'ā': 1, 'á': 2, 'ǎ': 3, 'à': 4,
    'ō': 1, 'ó': 2, 'ǒ': 3, 'ò': 4,
    'ē': 1, 'é': 2, 'ě': 3, 'è': 4,
    'ī': 1, 'í': 2, 'ǐ': 3, 'ì': 4,
    'ū': 1, 'ú': 2, 'ǔ': 3, 'ù': 4,
    'ǖ': 1, 'ǘ': 2, 'ǚ': 3, 'ǜ': 4,
    'ń': 2, 'ň': 3, '': 4
}


def forward_maximum_matching(text, word_dict):
    result = []
    text_length = len(text)
    max_word_length = max(len(word) for word in word_dict)

    index = 0
    while index < text_length:
        matched = False
        for i in range(max_word_length, 0, -1):
            if text[index:index+i] in word_dict:
                result.append(text[index:index+i])
                index += i
                matched = True
                break
        if not matched:
            result.append(text[index:])
            break
    return result


def get_tone(text):
    i = text[0]
    if i in tone_map:
        return tone_map[i]
    elif i in sm:
        return 0
    else:
        return 5


def get_tone_list(text):
    return [get_tone(i) for i in text]


def batch_replace(text, replacements):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def replace_tone(text):
    tone_normal_map = {
        'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a',
        'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o',
        'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e',
        'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
        'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u',
        'ǖ': 'v', 'ǘ': 'v', 'ǚ': 'v', 'ǜ': 'v',
        'ń': 'n', 'ň': 'n', '': 'n'
    }
    return batch_replace(text, tone_normal_map)


items = {}

for i in index:
    py, char = tuple(i)
    py_split = forward_maximum_matching(py, sm)
    py_split_no_tone = [replace_tone(i) for i in py_split]
    tones = get_tone_list(py_split)
    items.update({
        char: {
            "phoneme": py_split_no_tone,
            "tone": tones
        }
    })

for i in words:
    word, pys = tuple(i)
    pys = pys.replace('，', ' ').replace(',', '').replace('·', '')
    py_split_no_tone = []
    tones = []
    for py in pys.split(' '):
        py_split = forward_maximum_matching(py, sm)
        py_split_no_tone += [replace_tone(i) for i in py_split]
        tones += get_tone_list(py_split)
    items.update({
        word: {
            "phoneme": py_split_no_tone,
            "tone": tones
        }
    })
    if len(py_split_no_tone) != len(tones):
        print(word)

print(len(items.keys()))
json.dump(items, open('dict_v2.json', 'w',
          encoding='utf-8'), ensure_ascii=False)
