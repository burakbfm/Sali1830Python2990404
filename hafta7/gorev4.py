# GÖREV 2 | Üç Uçuş Görevi 

# Öğrenciden istenen: Geminin 3 uçuş yapmasını sağla. Her uçuş 5 yakıt tüketsin. Yakıt yetmezse görev sonlansın.
yakit = int(input("Yakıtın ne kadar: "))
ucus = 0

while ucus < 3:
    if yakit >=5:
        yakit -= 5
        ucus += 1
        print("Uçuş başarılı, Toplam Uçuş:", ucus)
    else:
        print("Yakıt Bitti!")
        break # while sürekli döngüde olduğu için whildan çıkış sağlar.

if ucus == 3:
    print("Toplam 3 Uçuş yaptınız başarılar. Kalan Yakıt:",yakit)
else:
    print("Toplam", ucus, "Yaptınız. Kalan ucus", 3-ucus, "Görev Başarısız!")