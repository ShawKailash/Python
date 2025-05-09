items=['one', 'two', 'three', 'four', 'five']
for item in items:
    if item=='two' or item =='four':
        continue
    print(item)
print("\n")

for item in items:
    if item=='three':
        break
    print(item)
print("\n")

num = 0
while num<=20:
    num=num+1
    if num%2==0:
        continue
    print(num)
print("\n")

num=0
while num<=1_000_000:
    num=num+1
    if num==13:
        break
    print(num)
