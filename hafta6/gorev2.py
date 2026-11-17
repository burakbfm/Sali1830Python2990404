# GÖREV 02 | Yakıt İstasyonu

# Süre: 10 dakika
# Zorluk: Kolay – Orta

# Öğrenciden Beklenenler
# -Başlangıç yakıtı 10 olsun.
# -Maksimum yakıt kapasitesini 25 olarak belirle.
# -Kullanıcıdan yakıt doldurmak isteyip istemediğini öğren.
# -Yakıt doldurulursa 10 birim ekle.
# -Yakıtın 25'i geçmesini engelle.

yakit = 20
kapasite = 25

print("=== YAKIT İSTASYONU ===")

secim = input("Yakıt doldurulsun mu? (e/h): ")

if secim == "e":
    yakit += 10
    if yakit > kapasite:
        print("Doldurulmak istenen yakıt kapasiteyi aşıyor. Aşılan miktar doldurulmayacak. Aşılan Miktar:",yakit-kapasite)
        yakit = kapasite
    print("Yakıt dolduruldu")
else:
    print("Yakıt Doldurulmadı")

print("Güncel Yakıt:",yakit)
