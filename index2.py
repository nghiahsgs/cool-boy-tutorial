import io
import random
f = io.open("ndung2.txt", mode="r", encoding="utf-8")
list_lines = f.read().split('\n')

print('========Nạnh Nùng Boy=========')
print('========Mỗi ngày 10p sẽ giúp bạn thành cool boy=========')
print('Bài 1: Hãy rep ờ hoặc ừ trong mọi hoàn cảnh')
print("== == == ==")
while True:
    line=random.choice(list_lines)
    print(line)
    input()
