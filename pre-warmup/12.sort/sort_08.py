n = int(input())
words = set()
word_lens = []
for _ in range(n):
    word = input()
    words.add(word)

for word in words:
    word_lens.append([len(word), word])

word_lens.sort()
for word in word_lens:
    print(word[1])