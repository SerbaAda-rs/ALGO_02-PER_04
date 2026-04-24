print("========  Pencarian Linear ======== ")
print("======== Rahmadi - 552010125009 =========\n")

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i  # posisi ditemukan
    return -1  # tidak ditemukan

# penggunaan
data = [5, 8, 12, 20, 7, 17, 2, 27]
target = 17

hasil = linear_search(data, target)

if hasil != -1:
    print("Data ditemukan di index:", hasil)
else:
    print("Data tidak ditemukan")