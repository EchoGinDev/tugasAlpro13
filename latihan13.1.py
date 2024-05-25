def cek_bilangan_prima(n,i=2):

    if n <= 1:
        return False
    elif i * i > n:
        return True
    elif n % i == 0:
        return False
    return cek_bilangan_prima(n, i + 1)

try:
    bilangan = int(input("Masukkan bilangan yang ingin diperiksa: "))
    if cek_bilangan_prima(bilangan):
        print(f"{bilangan} adalah bilangan prima")
    else:
        print(f"{bilangan} bukan bilangan prima")
except ValueError:
    print("Input yang dimasukkan bukan bilangan bulat")