import json
import pypinyin
print(1)
elements_chinese = [
    "氢", "氦", "锂", "铍", "硼", "碳", "氮", "氧", "氟", "氖",
    "钠", "镁", "铝", "硅", "磷", "硫", "氯", "氩", "钾", "钙",
    "钪", "钛", "钒", "铬", "锰", "铁", "钴", "镍", "铜", "锌",
    "镓", "锗", "砷", "硒", "溴", "氪", "铷", "锶", "钇", "锆",
    "铌", "钼", "锝", "钌", "铑", "钯", "银", "镉", "铟", "锡",
    "锑", "碲", "碘", "氙", "铯", "钡", "镧", "铈", "镨", "钕",
    "钷", "钐", "铕", "钆", "铽", "镝", "钬", "铒", "铥", "镱",
    "镥", "铪", "钽", "钨", "铼", "锇", "铱", "铂", "金", "汞",
    "铊", "铅", "铋", "钋", "砹", "氡", "钫", "镭", "锕", "钍",
    "镤", "铀", "镎", "钚", "镅", "锔", "锫", "锎", "锿", "镄",
    "钔", "锘", "铹", "𬬻", "𬭊", "𬭳", "𬭛", "𬭶", "鿏", "𫟼", 
    "𬬭", "鿔", "鿭", "𫓧", "镆", "𫟷", "鿬", "鿫"
]
pinyin = pypinyin.lazy_pinyin(
    ''.join(elements_chinese), style=pypinyin.Style.FINALS_TONE3)
print(pinyin)
elements_pinyin = zip(elements_chinese, pinyin)
elements_pinyin = dict(elements_pinyin)
with open('full_yunmu.json', 'w', encoding='utf-8') as f:
    json.dump(elements_pinyin, f, ensure_ascii=False, indent=4)