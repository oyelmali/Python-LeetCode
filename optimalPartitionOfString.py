"""
Dizenin Optimal Bölümü
Orta
Konular
Şirketler
İpucu
Bir dize verildiğinde , her bir alt dizedeki karakterler benzersizs olacak şekilde dizeyi bir veya daha fazla alt dizeye bölün . Yani, tek bir alt dizede hiçbir harf birden fazla görünmez .

Böyle bir bölümdeki minimum alt dize sayısını döndürün .

Her karakterin bir bölümdeki tam olarak bir alt dizeye ait olması gerektiğini unutmayın.

 

Örnek 1:

Giriş: s = "abacaba"
 Çıkış: 4
 Açıklama: 
İki olası bölüm şunlardır: ("a", "ba", "cab", "a") ve ("ab", "a", "ca", "ba") ). 
İhtiyaç duyulan minimum alt dizi sayısının 4 olduğu gösterilebilir.
Örnek 2:

Giriş: s = "ssssss"
 Çıkış: 6
 Açıklama:
 Geçerli tek bölüm ("s", "s", "s", "s", "s", "s")'dir.
 

Kısıtlamalar:

1 <= s.length <= 105
s yalnızca İngilizce küçük harflerden oluşur.
"""




def OptimalPartition(s):
    bigger = 0
    count = 0
    for i in s:
        for j in s:
            if i == j:
                count += 1
        if count > bigger:
            bigger = count
        count = 0
    return bigger

print(OptimalPartition("ssssss"))









