print("=== Program Loop Berurutan ===")
print("=====Rahmadi - 552010125009=====\n")

n = int(input("Masukkan nilai n: "))
count = 0

for i in range(n):    #loop pertama berjalan sebanyak n kali
    count += 1
    
for j in range(n):    #loop kedua berjalan sebanyak n kali
    count += 1

print("Jumlah iterasi:", count)