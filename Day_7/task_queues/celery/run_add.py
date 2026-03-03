from simple_tasks import add

result = add.delay(4, 4)
#print(result)
#print(result.ready())
#print(result.result)
#print(result.get())

nums = [(2, 2), (3, 4), (55, 66), (66, 77), (12, 33),
        (56, 66), (12, 12), (433, 44), (66, 77), (78, 99)]

results = []
for x, y in nums:
    results.append(add.delay(x, y))

print("All jobs submitted...")

while results:
    for r in results:
        if r.ready():
            print(r.get())
            results.remove(r)
