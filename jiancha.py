import sqlite3
import os
import json
from datetime import datetime

# 连接到SQLite数据库
db_path = r"C:\Users\14814\Desktop\网上花店系统\Flower\db.sqlite3"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 获取表结构
print("=== 表结构 ===")
cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='db_flower';")
schema = cursor.fetchone()
if schema:
    print(schema[0])
else:
    print("未找到 db_flower 表！")
    # 列出所有表
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print("\n可用的表：")
    for table in cursor.fetchall():
        print(table[0])

print("\n=== 数据内容 ===")
try:
    # 获取所有数据
    cursor.execute("SELECT * FROM db_flower")
    # 获取列名
    columns = [description[0] for description in cursor.description]
    print("列名:", columns)

    # 获取并打印所有行
    rows = cursor.fetchall()
    print("\n数据行:")
    for row in rows:
        row_dict = dict(zip(columns, row))
        print(json.dumps(row_dict, ensure_ascii=False, indent=2))
except Exception as e:
    print(f"获取数据时出错: {str(e)}")

conn.close()