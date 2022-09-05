price = int(input())

charge = 1000 - price
charge_lst = [500, 100, 50, 10, 5, 1]
cnt = 0
for c in charge_lst:
    if charge == 0:
        break
    elif charge >= c:
        cnt += charge//c
        charge %= c

print(cnt)