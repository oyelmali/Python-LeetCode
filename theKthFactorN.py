"""
n'nin k'inci Faktörü
Orta
Konular
Şirketler
İpucu
Size iki pozitif tamsayı veriliyor nve k. Bir tam sayının çarpanı, burada nbir tam sayı olarak tanımlanır .in % i == 0

Artan düzenden sıralanmış tüm faktörlerin bir listesini düşünün , bu listedeki faktörü döndürün veya faktörlerden azsa döndürün .kth-1nk

 

Örnek 1:

Giriş: n = 12, k = 3
 Çıkış: 3
 Açıklama: Faktörler listesi [1, 2, 3, 4, 6, 12] olup, 3. faktör 3'tür.
Örnek 2:

Giriş: n = 7, k = 2
 Çıkış: 7
 Açıklama: Faktörler listesi [1, 7], 2. faktör 7'dir.
Örnek 3:

Giriş: n = 4, k = 4
 Çıkış: -1
 Açıklama: Faktörler listesi [1, 2, 4] şeklindedir, sadece 3 faktör vardır. -1 değerini döndürmeliyiz.
 

Kısıtlamalar:

1 <= k <= n <= 1000
"""


def factorFounder(n, k):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    if len(factors) >= k:
        return factors[k - 1]
    else:
        return -1
    


print(factorFounder(4, 4))

