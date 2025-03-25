import pandas as pd
import random

# 读取 Excel 文件
def load_data(filepath):
    try:
        df = pd.read_excel(filepath)
        # 去除空值，避免异常
        df.dropna(subset=['关键字', '回应语句', '情绪标注', '标签分类'], inplace=True)
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"❌ 读取文件失败：{e}")
        return []

# AI 疗愈回应函数
def ai_response(user_input, data):
    matched_rows = []

    for row in data:
        # 假设关键词用空格分隔（如：压力 焦虑）
        keywords = str(row['关键字']).split()
        for kw in keywords:
            if kw in user_input:
                matched_rows.append(row)
                break  # 每行只算一次匹配

    if matched_rows:
        chosen = random.choice(matched_rows)
        return {
            '回应语句': chosen['回应语句'],
            '情绪标注': chosen['情绪标注'],
            '标签分类': chosen['标签分类']
        }
    else:
        return {
            '回应语句': "我在这里陪着你，说说发生了什么吧。",
            '情绪标注': "未知",
            '标签分类': "未分类"
        }

# 主程序
def main():
    print("🎧 AI 疗愈助手启动中...\n")
    data = load_data("情绪安慰语料.xlsx")

    if not data:
        print("⚠️ 数据加载失败，程序退出。")
        return

    while True:
        user_input = input("你想说些什么？（输入 q 退出）\n> ")
        if user_input.lower() == 'q':
            print("👋 再见，希望你每天都好一点。")
            break

        result = ai_response(user_input, data)

        print("\n🤖 回应语句:", result['回应语句'])
        print("📌 情绪标注:", result['情绪标注'])
        print("🏷️ 标签分类:", result['标签分类'], "\n")

# 运行程序
if __name__ == "__main__":
    main()