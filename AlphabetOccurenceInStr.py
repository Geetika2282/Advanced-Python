txt = input("Enter your string: ")
def chCount(txt):
    cnt = {}
    count = 0
    for i in txt:
        if i not in cnt:
            cnt[i] = txt.count(i)
    print(cnt)

chCount(txt)
