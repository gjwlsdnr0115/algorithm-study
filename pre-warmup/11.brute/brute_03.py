def get_ranking(n, people):
    p = people[n]
    rank = 1
    for i in range(len(people)):
        if i!=n:
            if p[0] < people[i][0] and p[1] < people[i][1]:
                rank += 1

    return rank

N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, input().split())))

ranking = []
for i in range(len(people)):
    ranking.append(get_ranking(i, people))

for r in ranking:
    print(r, end=' ')