import pypinyin
import json
# import load_audio
#加载所需字典
def load_json(file):
    with open('./pinyin_dict/'+file, 'r', encoding='utf-8') as f:
        return json.load(f)
full_pinyin = load_json('full_pinyin.json')
pinyin_without_tone = load_json('pinyin.json')
shengmu = load_json('shengmu.json')
full_yunmu = load_json('full_yunmu.json')
yunmu = load_json('yunmu.json')


element_result = []#用于存储结果

def result_append(word,element):
    element_result.append(
                    {'word': element, 'start': word.get('start'), 'end': word.get('end'), 'score': word.get('core')})
def find_words_pinyin(words_list):
    # 全匹配，除开声调的全匹配,声母匹配,韵母匹配（含有声调）,韵母匹配（不含声调)
    for word in words_list:
        result_append(word,full_matched(word))



def full_matched(word):
    pinyin = pypinyin.lazy_pinyin(
            word["word"], style=pypinyin.Style.TONE3)[0]
    for element, element_pinyin in full_pinyin.items():
        if pinyin == element_pinyin:
            return element
    return full_matched_without_tone(word)


def full_matched_without_tone(word):
    pinyin = pypinyin.lazy_pinyin(
            word["word"], style=pypinyin.Style.NORMAL)[0]
    for element, element_pinyin in pinyin_without_tone.items():
        if pinyin == element_pinyin:
            return element
    return sheng_mu_match(word)


def sheng_mu_match(word):
    pinyin = pypinyin.lazy_pinyin(
            word["word"], style=pypinyin.Style.INITIALS)[0]
    for element, element_pinyin in shengmu.items():
        if pinyin == element_pinyin:
            return element
    return yun_mu_match(word)

def yun_mu_match(word):
    pinyin = pypinyin.lazy_pinyin(
            word["word"], style=pypinyin.Style.FINALS_TONE3)[0]
    for element, element_pinyin in full_yunmu.items():
        if pinyin == element_pinyin:
            return element
    return yun_mu_match_without_tone(word)



def yun_mu_match_without_tone(word):
    pinyin = pypinyin.lazy_pinyin(
            word["word"], style=pypinyin.Style.FINALS)[0]
    for element, element_pinyin in full_yunmu.items():
        if pinyin == element_pinyin:
            return element
    return word["word"]

# 选择支
mode = input('请选择转译方式\n1.从音频转译\n2.从文本转译\n')


# 音频模式
if mode == '1':
    import load_audio
    path = input('请将音频文件拖拽到这里')
    words_list = load_audio.trans_audio_to_whisper(path)
    print(words_list)

# 文本模式
elif mode == '2':
    path = input('请将words_list.json拖拽到这里')
    with open(path,'r',encoding='utf-8') as f:
        words_list = json.load(f)

else:
    raise(ValueError)
    
find_words_pinyin(words_list)
with open('./element_result.json','w',encoding='utf-8') as f:
    json.dump(element_result,f,ensure_ascii=False)