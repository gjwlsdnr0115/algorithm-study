import string

s = input()
char_index_dict = {}
for i in range(len(s)):
    if s[i] not in char_index_dict.keys():
        char_index_dict[s[i]] = i
for c in string.ascii_lowercase:
    print(char_index_dict.get(c, -1), end=' ')