yakit = 20

print("Başlangıç Yakıtı:",yakit)

yakit -= 5 # yakit = yakit - 5 

# değişkenimiz aynı içindeki veri güncellendi
# sağ tarafan atanacak bilgi sol taraf atanan. sol ve sağ taraftaki bilgiler birbirinden bağımsızdır.

print("Uçuştan Sonra Yakıt:",yakit)

yakit += 10 #yakit = yakit + 10

print("Eklemeden SONRA Yakıt:",yakit)

# Koşullarla karar verme
# Uzay gemisinin uçabilmesi için en az 50 birim yakıt gerekmektedir.

if yakit >= 50:
    print("Uçuş Başarılı!")
else:
    print("Yetersiz Yakıt! Gerekli Olan Yakıt Miktarı:",50-yakit)

# =     | Atama işartedir. ve değişkenlere bilgi atar.
# ==    | Soru operatörüdür. bilgiler birbirine eşit mi dye sorar. x == Y y x e eşit mi
# >=    | Büyük veya eşit mi operatörüdür. x >= y. x y ifadesine ya eşittir ya da büyüktür diye sorar
# <=    | Küçük veya eşit mi operatörüdür. x <= y. x y ifadesine ya eşittir ya da küçüktür diye sorar

 