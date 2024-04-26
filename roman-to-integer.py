"""Romen rakamları yedi farklı sembolle temsil edilir:  I, V, X, L, C, Dve M.

Sembol        Değeri
ben 1
V5
X 10
L 50
Ç 100
D 500
M1000
Örneğin,   Romen rakamı ile sadece iki tanesinin toplanmasıyla 2yazılır . basitçe olarak yazılır  . Sayı olarak yazılır , yani .II12XIIX + II27XXVIIXX + V + II

Romen rakamları genellikle soldan sağa büyükten küçüğe doğru yazılır. Ancak dört rakamı değil IIII. Bunun yerine dört sayısı şu şekilde yazılır IV: Bir, beşten önce olduğu için çıkarıyoruz ve dört yapıyoruz. Aynı prensip, olarak yazılan dokuz sayısı için de geçerlidir IX. Çıkarmanın kullanıldığı altı örnek vardır:

I4 ve 9 yapmak için  V(5) ve (10)' un önüne yerleştirilebilir .X
X40 ve 90 yapmak için  L(50) ve (100)' den önce yerleştirilebilir .C
C400 ve 900 yapmak için D(500) ve (1000)' den önce yerleştirilebilir .M
Bir Romen rakamı verildiğinde onu tam sayıya dönüştürün.

 

Örnek 1:

Giriş: s = "III"
 Çıkış: 3
 Açıklama: III = 3.
Örnek 2:

Giriş: s = "LVIII"
 Çıkış: 58
 Açıklama: L = 50, V= 5, III = 3.
Örnek 3:

Giriş: s = "MCMXCIV"
 Çıkış: 1994
 Açıklama: M = 1000, CM = 900, XC = 90 ve IV = 4."""



class Solution(object):
    def romanToInt(s):
        dictr = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
            print(sum, i)
            if i == 0:
                sum += dictr[s[i]]
            elif len(s) == i + 1:
                if dictr[s[i]] > dictr[s[i-1]]:
                    sum += dictr[s[i]] - dictr[s[i-1]]
                else:
                    sum += dictr[s[i]]
            elif dictr[s[i]] >= dictr[s[i+1]] and dictr[s[i]] <= dictr[s[i-1]]:
                sum += dictr[s[i]]
            elif dictr[s[i]] > dictr[s[i+1]] and dictr[s[i]] > dictr[s[i-1]]:
                sum += dictr[s[i]] - dictr[s[i-1]]
            elif dictr[s[i]] < dictr[s[i+1]] and dictr[s[i]] < dictr[s[i-1]]:
                continue
            
        print(sum)     
    romanToInt("MCMXCIV")





















