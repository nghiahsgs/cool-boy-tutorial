import re
import io
def ham_regex(ndung):
    regex1 = re.compile('(\d)..(.*)')
    # ndung = '10. Mỗi người đều có quyền yêu cái đẹp. Vì vậy, tớ yêu cậu.'
    kq = regex1.search(ndung)
    # print(kq.group(2))
    try:
        return kq.group(2)
    except Exception:
        return ''



def writeUtf8(filename,nd_line):
    f = io.open(filename, mode="a", encoding="utf-8")
    f.write(nd_line + '\n')
    f.close()

f = io.open("ndung.txt", mode="r", encoding="utf-8")
list_lines=f.readlines()
# print(list_lines)
for line in list_lines:
    # print(line)
    kq=ham_regex(line)
    if kq!="":
        writeUtf8('ndung2.txt', kq)
    # print(kq)
