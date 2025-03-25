import pandas as pd

# 读取 Excel 文件
file_path = '情绪安慰语料.xlsx'
try:
    df = pd.read_excel(file_path)
    print("文件读取成功！")
    print("读取的内容预览：")
    print(df.head())  # 打印前5行数据
except Exception as e:
    print("文件读取失败！")
    print("错误信息：", e)