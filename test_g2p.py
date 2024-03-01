import json

dict_f = open('dict_v2.json', 'r', encoding='utf-8')
dict_json = json.load(dict_f)
dict_f.close()

dict_words = dict_json.keys()
max_word_length = max(len(word) for word in dict_words)


def forward_maximum_matching(text):
    result = []
    text_length = len(text)

    index = 0
    while index < text_length:
        matched = False
        for i in range(max_word_length, 0, -1):
            if text[index:index+i] in dict_words:
                result.append(text[index:index+i])
                index += i
                matched = True
                break
        if not matched:
            result.append(text[index:index+i])
            index += i
    return result


def g2p_str(text):
    split = forward_maximum_matching(text)
    g2p_result = ''
    for seg in split:
        if seg in dict_json:
            ps = dict_json[seg]['phoneme']
            ts = dict_json[seg]['tone']
            for p, t in zip(ps, ts):
                if t != 0:
                    g2p_result += f'{p}{t} '
                else:
                    g2p_result += f'{p}'
    return g2p_result


def g2p_list(text):
    split = forward_maximum_matching(text)
    g2p_result_p = []
    g2p_result_t = []
    for seg in split:
        if seg in dict_json:
            g2p_result_p += dict_json[seg]['phoneme']
            g2p_result_t += dict_json[seg]['tone']
    return g2p_result_p, g2p_result_t


texts = [
    '我这次回来这里呢，是为了再一次，倾听星星的声音呢。',
    '有些风景，自然而然就在脑海中复苏。',
    '有些记忆，就像是和飘落的樱花相呼应一样在我内心深处不断浮现。',
    '那些全是即使我不愿回想……也会浮现而来的景象。',
    '落英斑斓的樱花瓣在空中飞舞。',
    '「主人!早上了哦,快起来快起来」',
    '「不在恰当的时候做恰当的事情，你会后悔的,主人」',
    '「就是和同龄的朋友大声地欢笑，愉快地玩耍」',
    '「不去体验这种理所当然的事情，往后的生活会很难受，主人」'
]

for text in texts:
    print(text, '\n', g2p_str(text))

result = g2p_list(texts[0])
print(f"{texts[0]}\nPhoneme: {result[0]}\nTone: {result[1]}")
