def is_group_word(word):
    group = True
    padded_word = '*'+word+'*'

    for c in word:
        split = padded_word.split(c)
        stripped_split = [s for s in split if s != '']
        if len(stripped_split) > 2:
            group = False
            break

    if group:
        return 1
    else:
        return 0

n = int(input())
count = 0
for i in range(n):
    w = input()
    count += is_group_word(w)
print(count)