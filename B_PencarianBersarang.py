print("========  Pencarian Bersarang (O(n²)) ======== ")
print("======== Rahmadi - 552010125009 =========\n")



def nested_search(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and data[i] == data[j]:
                print(f"Duplikat ditemukan: {data[i]} di index {i} dan {j}")

# Contoh penggunaan
data = [5, 8, 12, 5, 20]

nested_search(data)