
"""Negatif olmayan iki tamsayıyı temsil eden iki boş olmayan bağlantılı liste verilir . Rakamlar ters sırada saklanır ve düğümlerinin her biri tek bir rakam içerir. İki sayıyı ekleyin ve toplamı bağlantılı liste olarak döndürün.

İki sayının, 0 sayısı dışında herhangi bir başta sıfır içermediğini varsayabilirsiniz.

 

Örnek 1:


Giriş: l1 = [2,4,3], l2 = [5,6,4]
 Çıkış: [7,0,8]
 Açıklama: 342 + 465 = 807.
Örnek 2:

Giriş: l1 = [0], l2 = [0]
 Çıkış: [0]
Örnek 3:

Giriş: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 Çıkış: [8,9,9,9,0,0,0,1]
 

"""

class Solution(object):
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = []
        for i in range(len(l1)):
            y = l1[i] + l2[i]
            if y >= 10 and len(l1) == i:
                sum.append( y)
            elif  y >= 10: 
                l1[i+1] += 1
                y = y % 10
                sum.append(y)
            else:
                sum.append(y)
        sum = sum[::-1]
        print(sum)

    addTwoNumbers([2, 4, 3], [5, 6, 4])