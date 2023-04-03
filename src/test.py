import json

with open('./table85.txt', 'r') as f:
    lines = f.readlines()
# 获取表头
x_axis = lines[0].strip().split('\t')[0:]
# 获取数据
data = []
for index, line in enumerate(lines[1:]):
    y, values = line.strip().split('\t', 1)
    values = values.split('\t')
    for i, v in enumerate(values):
        if v:
            data.append({'d': 85,'x': int(x_axis[i]),'y': int(y),  'value': int(v)})

# 生成 JSON 数组
json_data = json.dumps(data, indent=4)
print(json_data)
