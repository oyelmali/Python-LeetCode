"""Bir tamsayı dizisi nums ve bir tamsayı verildiğinde, iki sayının indekslerini, toplamları şuna eşit olacak şekilde target döndürün .target

Her girdinin tam olarak bir çözümü olacağını varsayabilirsiniz ve aynı öğeyi iki kez kullanamazsınız .

Cevabı istediğiniz sırayla geri verebilirsiniz.

 

Örnek 1:

Girdi: sayılar = [2,7,11,15], hedef = 9
 Çıktı: [0,1]
 Açıklama: Sayılar[0] + sayılar[1] == 9 olduğundan, [0, 1] değerini döndürürüz.
Örnek 2:

Giriş: sayılar = [3,2,4], hedef = 6
 Çıkış: [1,2]
Örnek 3:

Giriş: sayılar = [3,3], hedef = 6
 Çıkış: [0,1]
 """
class Solution(object):
    def twoSum(nums, target):
        for i in nums:
            for j in nums:
                if j == i:
                    continue
                elif i + j == target:
                    two = [nums.index(j), nums.index(i)]
                    break
        return two
                
    print(twoSum([2, 7, 11, 15], 9))