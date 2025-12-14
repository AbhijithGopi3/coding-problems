cost=3
amount=15
choclates = amount // cost
print("initial choclate: ",choclates)
wrappers=choclates 
print("initial wrappers: ",wrappers)

while (wrappers>=3):
    exchange=wrappers//3 # 1
    wrappers=wrappers%3+exchange # 1
    choclates=choclates+exchange # 7
    print(f"Exchanged {exchange} new chocolates")
    print(f"Total chocolates now: {choclates}")
    print(f"Wrappers now: {wrappers}")

print(f"\nFinal total chocolates: {choclates}")

