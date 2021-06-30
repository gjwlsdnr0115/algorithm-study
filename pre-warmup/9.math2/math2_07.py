x, y, w, h = map(int, input().split())
dist_list = [x, y, w-x, h-y]
print(min(dist_list))