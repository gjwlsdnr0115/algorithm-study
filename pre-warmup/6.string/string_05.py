words = input().upper()
unique_words = list(set(words))

count_list = []
for c in unique_words:
    count = words.count(c)
    count_list.append(count)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    idx = count_list.index(max(count_list))
    print(unique_words[idx])