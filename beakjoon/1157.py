import sys

sis = sys.stdin.readline().strip()

words = sis.upper()
unique_words = list(set(words))
cnt_list = []
for word in unique_words:
    cnt = words.count(word)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])

print(unique_words)