prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
for i in prices:
    rub, kk = str(f"{i:.2f}").split(".")
    print(f"{rub} руб {int(kk):02d} коп, ", end=" ")

print(id(prices))
print(sorted(prices))
print(id(prices))

prices2 = sorted(prices, reverse=True)
print(f"ID change: {id(prices2)} - {prices2}\n{prices2[:5][::-1]}")



