print("===== Program Loop Bersarang =====")
print("===== Rahmadi - 552010125009 =====\n")

n = int(input("Masukkan nilai n: "))
count = 0

for i in range(n):
    for j in range(n):
        count += 1

print("Jumlah iterasi:", count)