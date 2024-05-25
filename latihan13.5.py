def kombinasi(n, k):
    if n < k:
        print("Nilai dari n harus lebih besar atau sama dengan nilai k")
        return None
    elif k == 0 or k == n:
        return 1
    return kombinasi(n - 1, k - 1) + kombinasi(n - 1, k)

n, k = map(int, input("Masukkan nilai n dan k (pisahkan dengan koma): ").split(","))
hasil = kombinasi(n, k)
if hasil is not None:
    print(f"Kombinasi C({n}, {k}) adalah {hasil}")
