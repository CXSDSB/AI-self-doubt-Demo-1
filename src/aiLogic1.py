import pandas as pd
import random

# 读取 Excel 文件
df = pd.read_excel('情绪安慰语料.xlsx')  # 替换为你的文件名

# 确保列名一致，如果不一致请修改
keyword_col = '关键词'
response_col = '原始句子'
emotion_col = '情绪标注'
tag_col = '标签分类'

# 清洗关键词列（支持多个关键词）
df[keyword_col] = df[keyword_col].astype(str).apply(lambda x: [kw.strip() for kw in x.replace('、', ',').split(',')])

# 清洗回应语句（支持多个回应）
df[response_col] = df[response_col].astype(str).apply(lambda x: [resp.strip() for resp in x.replace('\n', '|').split('|')])

print("欢迎进入智能回应系统，输入“退出”可离开。")

while True:
    user_input = input("\n你说：")
    if user_input.strip().lower() == '退出':
        print("感谢使用，再见！")
        break

    matched = False
    for i, row in df.iterrows():
        for keyword in row[keyword_col]:
            if keyword in user_input:
                matched = True
                response = random.choice(row[response_col])
                print(f"\n回应：{response}")
                print(f"情绪标注：{row[emotion_col]}")
                print(f"标签分类：{row[tag_col]}")
                break
        if matched:
            break

    if not matched:
        print("抱歉，我还无法理解这个内容。")