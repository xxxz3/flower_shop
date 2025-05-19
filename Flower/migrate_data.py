import os
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Flower.settings')
django.setup()

def fix_json_data(json_file):
    """修复JSON数据中可能的问题"""
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 检查并修复数据
        modified = False
        for item in data:
            if 'model' in item and item['model'] == 'api.flower':
                fields = item['fields']
                if 'image' in fields and fields['image']:
                    # 确保 image 字段是字符串类型
                    if isinstance(fields['image'], bytes):
                        fields['image'] = fields['image'].decode('utf-8')
                    modified = True

        # 保存修复后的数据
        output_file = 'fixed_' + json_file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"数据修复完成，已保存到 {output_file}")
        return True

    except Exception as e:
        print(f"修复数据时出错：{str(e)}")
        return False

def migrate_data():
    try:
        # 检查源数据文件是否存在
        if not os.path.exists('api_data.json'):
            print("找不到 api_data.json 文件！")
            return

        # 处理并修复导出的数据
        if fix_json_data('api_data.json'):
            # 使用 loaddata 导入数据
            result = os.system('python manage.py loaddata fixed_api_data.json')
            if result == 0:
                print("数据迁移成功！")
            else:
                print("数据导入过程中出错")

    except Exception as e:
        print(f"迁移过程中出错：{str(e)}")

if __name__ == '__main__':
    migrate_data()