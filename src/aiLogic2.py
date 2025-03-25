import pandas as pd
import random

# 读取 Excel 文件
df = pd.read_excel('情绪安慰语料.xlsx')
df['关键词'] = df['关键词'].astype(str)
df['回应语句'] = df['回应语句'].astype(str)

print("欢迎进入智能回应系统 💗 输入“退出”即可结束。")
print("你可以告诉我你现在的感受，比如：‘我有点怕失去’、‘最近很焦虑’...")

while True:
    user_input = input("\n你说：").strip()
    if user_input.lower() == '退出':
        print("谢谢你愿意表达，我们下次再聊~ 🌙")
        break

    matched_rows = []

    for i, row in df.iterrows():
        # 以“、”为分隔符，把关键词拆成列表
        keyword_list = [kw.strip() for kw in row['关键词'].split('、')]

        # 判断这些关键词中是否有至少一个出现在用户输入里
        if any(kw in user_input for kw in keyword_list):
            matched_rows.append(row)

    if matched_rows:
        selected = random.choice(matched_rows)
        print(f"\n回应：{selected['回应语句']}")
    else:
        print("我还不能完全理解你的情绪……可以换种方式表达吗？🌿")