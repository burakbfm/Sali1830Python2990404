# Kullanıcıdan yakıt miktarı al. Yakıt 10 veya üzerindeyse geminin kalkabileceğini, değilse kalkamayacağını göster.
# ⭐ Bonus: Yakıt 0 veya negatifse "Geçersiz yakıt" mesajı göster.

# if elif else 

yakit = int(input("Yakıt Miktarı: "))

if yakit <0:
    print("Geçersiz Yakıt!")
elif yakit >=10:
    print("Uçuş başarılı!")
else:
    print("Yetersiz Yakıt!")