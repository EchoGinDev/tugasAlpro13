def deretGanjil(n):

    if n == 1:
        return 1
    if n % 2 != 0:
        return n + deretGanjil(n - 2)
    else:
        return deretGanjil(n - 1)

try:
    nomor = int(input("Masukkan bilangan ganjil terbesar yang ingin dihitung: "))
    if nomor < 1:
        print("Bilangan harus lebih besar atau sama dengan 1")
    else:
        hasil = deretGanjil(nomor)
        print(f"Jumlah deret bilangan ganjil hingga {nomor} adalah {hasil}")
except ValueError:
    print("Input yang dimasukkan bukan bilangan bulat")
