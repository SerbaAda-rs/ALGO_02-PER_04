print("===== Program linear Search & Nested Loop =====")
print("===== Rahmadi - 552010125009 =====\n")


#LINEAR SEARCH (O(n))
data = [1, 3, 5, 7, 9, 11, 13]
target = int(input("Cari angka: "))
count = 0

#PERULANGAN LINEAR SEARCH
for item in data:
    count += 1
    if item == target:
        break

print("Jumlah langkah:", count)

#Nested Loop (O(n2))
data = [1, 3, 5, 7, 9, 11]
count = 0

#NESTED LOOP    
for i in data:
    for j in data:
        count += 1

print("Jumlah langkah:", count)