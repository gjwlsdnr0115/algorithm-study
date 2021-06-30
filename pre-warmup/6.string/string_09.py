encoded = ['c=','c-','dz=','d-','lj','nj','s=','z=']
croa_str = input()
count = len(croa_str)
for a in encoded:
    croa_str = croa_str.replace(a, '*')
print(len(croa_str))