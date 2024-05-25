def apakah_palindrom(nilai):

    nilai_str = str(nilai)

    if len(nilai_str) <= 1:
        return True
    else:
        return nilai_str[0] == nilai_str[-1] and apakah_palindrom(nilai_str[1:-1])


try:
    nilai = int(input("Masukkan sebuah nilai:"))  
    if apakah_palindrom(nilai):  
        print("Nilai ini merupakan bilangan palindrom!")  
    else:  
        print("Nilai ini bukan merupakan bilangan palindrom!")  
except ValueError:
    print("Input yang dimasukkan bukan angka")













