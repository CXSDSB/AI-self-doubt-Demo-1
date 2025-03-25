import pandas as pd
import re
import random

# ========== 💾 读取 Excel 文件 ==========
try:
    df = pd.read_excel("情绪安慰语料.xlsx")
    print("✅ 文件读取成功！\n")
except Exception as e:
    print("❌ 文件读取失败，请检查文件名或路径。")
    print("错误信息：", e)
    exit()

# ========== 🧼 清理文本函数 ==========
def clean_text(text):
    # 去除非文字内容，转小写
    return re.sub(r'[^\w\u4e00-\u9fa5]', '', str(text)).lower()

# ========== 💡 查找回应函数 ==========
def find_response(user_input):
    user_input_clean = clean_text(user_input)
    possible_matches = []

    for _, row in df.iterrows():
        sentence = str(row["关键词"])
        sentence_clean = clean_text(sentence)

        # 如果用户输入包含了原始句子的一部分关键词
        if any(word in user_input_clean for word in sentence_clean.split()):
            possible_matches.append(row)

    if possible_matches:
        match = random.choice(possible_matches)
        return {
            "情绪": match["情绪标注"],
            "标签分类": match["标签分类"],
            "回应": match["回应语句"]
        }

    # 通用安慰语备用
    default_responses = [
        "我不知道怎么回应你，但你不是一个人。🌸",
        "没关系的，我会陪你慢慢来。🌿",
        "你已经很努力了，可以停下来歇一歇。🍵",
        "不管你现在有多低落，都值得被温柔对待。☁️"
    ]

    return {
        "情绪": "未识别",
        "标签分类": "未知",
        "回应": random.choice(default_responses)
    }

# ========== 🗣️ 交互开始 ==========
print("🎐 情绪安慰小助手上线啦 ~")
print("告诉我你现在的心情，我陪你聊聊：")

while True:
    user_input = input("\n你现在在想什么呢？（输入 '退出' 结束）\n> ")
    if user_input.strip() == '退出':
        print("🫂 谢谢你今天来找我说话，照顾好自己哦。再见！🌙")
        break

    response = find_response(user_input)

    print("\n💡 我能感受到你现在的情绪是：")
    print(f"🌧 情绪：{response['情绪']}")
    print(f"🧩 标签分类：{response['标签分类']}")
    print(f"🫂 回应我想说：{response['回应']}")