# GÖREV 01 | Uzay Gemisini Uçur!

# Süre: 10 dakika
# Zorluk: Kolay

# Sizden Beklenenler
# -Başlangıç yakıtı 15 olsun.
# -Kullanıcıdan uçuş yapmak isteyip istemediğini öğren.
# -Uçuş için en az 5 yakıt gerektiğini kontrol et.
# -Uçuş başarılıysa yakıtı 5 azalt.
# -Kalan yakıtı ekrana yazdır.

yakit = 15

print("=== UZAY GEMİSİ ===")

secim = input("Uçuş yapılsın mı? (e/h): ")

if secim == "e":
    if yakit >= 5:
        yakit -= 5 # yakit = yakit - 5
        print("Uçuş başarılı!")
    else:
        print("Yetersiz Yakıt!")
else:
    print("Uçuş Modu İptal Edildi!")

print("Kalan Yakıt:",yakit)