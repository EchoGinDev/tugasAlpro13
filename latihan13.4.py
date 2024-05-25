def digitRec(n):
    if n == 0:
        return 0, ""
    
    digit = n % 10
    sisa = n // 10
    

    hasil, digitStr = digitRec(sisa)
    hasil = hasil + digit

    if digitStr == "":
        digitStr = str(digit)
    else:
        digitStr = digitStr + " + " + str(digit)
    
    return hasil, digitStr

try:
    nomor = int(input("input bilangan: "))
    if nomor < 0:
        print("bilangan harus positif")
    elif nomor == 0:
        print("0 = 0")
    else:
        hasil, digitStr_output = digitRec(nomor)
        print(f"{digitStr_output} = {hasil}")
except ValueError:
    print("Input bukan bilangan bulat")
