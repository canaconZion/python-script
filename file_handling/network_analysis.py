import re
import matplotlib.pyplot as plt

# 打开文本文件
with open('net.txt', 'r') as file:
    lines = file.readlines()

timestamps = []
txkbps_values = []

# 正则表达式模式用于匹配时间戳和eth0的txkB/s
pattern = r'(\d+:\d+:\d+ \w\w) +p2p1 +\d+\.\d+ +\d+\.\d+ +\d+\.\d+ +(\d+\.\d+)'
with open('net_msg.txt', 'w') as f:
    for line in lines:
        match = re.search(pattern, line)
        if match:
            timestamp = match.group(1)
            txkbps = match.group(2)
            timestamps.append(timestamp)
            txkbps_values.append(float(txkbps))
            f.write(f"{timestamp}-{float(txkbps)}\n")

# 将时间戳字符串转换为数字（你可以根据需要格式化时间戳）
timestamps_as_numbers = list(range(len(timestamps)))

# 增加生成的 PNG 图像的宽度
plt.figure(figsize=(24, 6))  # 增加宽度，保持高度不变
plt.plot(timestamps_as_numbers, txkbps_values, marker='o', linestyle='-')

# 设置图的标签
plt.title('p2p txkB/s over Time')
plt.xlabel('Time')
plt.ylabel('p2p txkB/s')

# 设置 x 轴标签为时间戳
# 将时间戳刻度修改为每隔1分钟
x_tick_positions = range(0, len(timestamps_as_numbers), 30)  # 1分钟 = 60个数据点 
x_tick_labels = [timestamps[i] for i in x_tick_positions]
plt.xticks(x_tick_positions, x_tick_labels, rotation=45)
plt.tight_layout()

# 保存折线统计图为 PNG 图像
plt.savefig('net.png')
