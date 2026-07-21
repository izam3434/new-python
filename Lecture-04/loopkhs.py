print("KPH\tMPH")
print("-----------")
for i in range(60, 140, 10):
    mph = i * 0.6214
    print(f"{i}\t{mph:.1f}")