# Sonsuz kere tekrar etme potansiyeli olan bir döngüsel komuttur.

# while koşul: (KOŞUL DOĞRU OLDUĞU SÜRECE KODLARIM ÇALIŞIR)
    # koşul doğruysa çalışacak kodum

ucus = 1
while 0 < 3:
    print("Uçuş Yaptırıldı", ucus)
    ucus += 1

print("Görev Tamamlandı!")

# KULLANICI MENÜ SEÇİMİ YAPMA
print("=== KONTROL PANELİ ===")
print("1 - Uçuş Yap")
print("2 - Yakut Doldur")
print("3 - Çıkış")



secim = 0
while secim != "3": # != eşit değildir diye sorar buradada secim 3'e eşit değilse doğrudur
    secim = input("Seçiminiz: ")
    if secim == "1":
        print("Uçuş Başlatılıyor!")
    elif secim == "2":
        print("Yakıt Dolduruluyor!")
    elif secim == "3":
        print("Program Kapatılıyor!")
    else:
        print("Geçersiz İşlem!")