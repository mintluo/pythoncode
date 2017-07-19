string = input().lower()
wordCounts = {}
for ch in string:
    if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
        string = string.replace(ch, " ")
words = string.split()
for word in words:
    if word in wordCounts:
        wordCounts[word] += 1
    else:
        wordCounts[word] = 1
print(wordCounts)
pairs = list(wordCounts.items())
# 列表中的数据对交换位置,数据对排序
items = [[x, y] for (y, x) in pairs]
items.sort()

print(items[-1][1])