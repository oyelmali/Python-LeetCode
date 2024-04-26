"""
Yağmur Suyunun Tutulması
Zor
Konular
Şirketler
nHer çubuğun genişliğinin olduğu bir yükseklik haritasını temsil eden negatif olmayan tamsayılar verildiğinde 1, yağmurdan sonra ne kadar su tutabileceğini hesaplayın.

 

Örnek 1:


Giriş: yükseklik = [0,1,0,2,1,0,1,3,2,1,2,1]
 Çıkış: 6
 Açıklama: Yukarıdaki yükseklik haritası (siyah bölüm) [0,1 dizisi ile temsil edilmektedir. ,0,2,1,0,1,3,2,1,2,1]. Bu durumda 6 birim yağmur suyu (mavi bölüm) hapsolmaktadır.
Örnek 2:

Giriş: yükseklik = [4,2,0,3,2,5]
 Çıkış: 9
 

Kısıtlamalar:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""



def trap(height, hill=0, sum=0):
    for i in range(len(height)):
        print(height)
        if height[i] >= hill and hill == 0:
            print("ilk nokta", hill, height[i], i)
            hill = height[i]
            index = i
            if i > 0:
                for j in range(0, i, 1):                  
                    height.pop(j)
        elif height[i] >= hill and height[i] > height[i + 1]:
            print("son nokta", hill, height[i], i)
            sum += (hill * (i - index))
            for j in range(0, i, 1):
                if j != i and j != 0:
                    sum -= height[0]
                    print("çıkarılan", height[j], j) 
            for j in range(0, i, 1):
                print("silinen", height[0], j)
                height.pop(0)
            if len(height) > 1:
                trap(height, hill=0,sum=sum)
            else:
                return sum
            
        elif height[i] < hill:
            thereIsBar = False
            subHill = height[i]
            bigger = 0
            for i in range(2, len(height)):
                if subHill >= height[i]:
                    thereIsBar = True
                    break
                elif height[i] >= bigger:
                    bigger = height[i]

                






        """elif height[i] < hill and i > 1:
            checkSubHill = False
            subHill = height[i]
            for i in height:
                print("küçükse", i, subHill)
                if i <= subHill:
                    checkSubHill = False
                    break
                elif i > subHill:
                    print("heyo")
                    checkSubHill = True
                    break
            if checkSubHill:
                trap(height, hill=0, sum=sum)"""

                
print(trap([0,1,0,2,1,0,1,3,2,1,2,1], hill=0))




