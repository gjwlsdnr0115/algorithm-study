n = int(input())

scores = list(map(int, input().split()))
scores.sort()
for i in range(n):
    scores[i] = scores[i]/scores[-1]*100
print(sum(scores)/n)
