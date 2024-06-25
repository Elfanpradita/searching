def linear_search(arr, x):
    count = 0
    for item in arr:
        if item == x:
            count += 1
    return count

def menu_mencari_nama_penduduk():
    # Meminta pengguna untuk memasukkan jumlah warga
    try:
        n = int(input("Masukkan jumlah warga: "))
    except ValueError:
        print("Masukan harus berupa angka!")
        return

    # Menginisialisasi daftar warga
    warga = []

    # Meminta pengguna untuk memasukkan nama warga
    for _ in range(n):
        name = input("Masukkan nama warga: ")
        warga.append(name)

    # Meminta pengguna untuk memasukkan nama yang akan dicari jumlahnya
    x = input("Masukkan nama warga yang akan dihitung jumlahnya: ")

    # Menghitung jumlah kemunculan nama menggunakan linear search
    result = linear_search(warga, x)

    # Menampilkan hasil
    print(f"Nama {x} ditemukan sebanyak {result} kali dalam daftar warga.")

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

def menu_kode_stok_barang():
    # Meminta pengguna untuk memasukkan jumlah barang
    try:
        n = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Masukan harus berupa angka!")
        return

    # Menginisialisasi daftar barang
    items = []

    # Meminta pengguna untuk memasukkan kode dan nama barang
    for _ in range(n):
        try:
            code = int(input("Masukkan kode barang: "))
        except ValueError:
            print("Kode barang harus berupa angka!")
            return
        name = input("Masukkan nama barang: ")
        items.append((code, name))

    # Mengurutkan daftar barang berdasarkan kode barang
    items.sort(key=lambda item: item[0])

    # Memisahkan kode barang dan nama barang
    codes = [item[0] for item in items]
    names = [item[1] for item in items]

    # Meminta pengguna untuk memasukkan kode barang yang akan dicari
    try:
        x = int(input("Masukkan kode barang yang akan dicari: "))
    except ValueError:
        print("Kode barang harus berupa angka!")
        return

    # Mencari kode barang menggunakan binary search
    result = binary_search(codes, x)

    if result != -1:
        print(f"Kode barang ditemukan pada indeks {result} dengan nama barang: {names[result]}")
    else:
        print("Kode barang tidak ditemukan dalam daftar")

def menu_binary_ppt():
    try:
        arr = list(map(int, input("Masukkan daftar elemen yang sudah terurut: ").split()))
    except ValueError:
        print("Daftar elemen harus berupa angka dan dipisahkan oleh spasi!")
        return

    try:
        x = int(input("Masukkan elemen yang akan dicari: "))
    except ValueError:
        print("Elemen yang dicari harus berupa angka!")
        return

    result = binary_search(arr, x)

    if result != -1:
        print(f"Elemen ditemukan pada indeks {result}")
    else:
        print("Elemen tidak ditemukan dalam daftar")

def main():
    print("Menu:")
    print("1. Mencari nama penduduk")
    print("2. Kode stok barang")
    print("3. Binary PPT")
    
    try:
        choice = int(input("Pilih menu: "))
    except ValueError:
        print("Pilihan harus berupa angka!")
        return
    
    if choice == 1:
        menu_mencari_nama_penduduk()
    elif choice == 2:
        menu_kode_stok_barang()
    elif choice == 3:
        menu_binary_ppt()
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()