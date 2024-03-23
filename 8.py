knut = int(input())

# 1galleon=17sickles, 1sickle=29knuts
galleons = knut // (17 * 29)
knut2 = knut % (17 * 29)
sickles = knut2 // 29
knut3 = knut2 % 29

if galleons > 0:
    print (f"{galleons} галлеонов ")
if sickles > 0:
    print(f"{sickles} сиклей ")
if knut3 > 0:
    print(f"{knut3} кнатов")
