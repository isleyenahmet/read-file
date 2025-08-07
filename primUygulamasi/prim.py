def primGir():
    ad = input("Adinizi Giriniz: ")
    soyAd = input("Soyadinizi Giriniz: ")
    prim1 = input("1. Prim Tutarini Giriniz: ")
    prim2 = input("2. Prim Tutarini Giriniz: ")
    prim3 = input("3. Prim Tutarini Giriniz: ")

    with open("prim.txt", "a",encoding="utf-8") as file:
        file.write(ad + " " + soyAd + ":" + prim1 + " "  + prim2 + " " + prim3+ "\n")


def primHesapla(satir):
    satir = satir.strip() #boşlukları göz ardı et
    liste = satir.split(":")

    calisanAdiSoyadi = liste[0]
    primler = liste[1].strip().split()

    prim1 = int(primler[0])
    prim2 = int(primler[1])
    prim3 = int(primler[2])

    ortalama = (prim1 + prim2 + prim3) / 3

    return f"{calisanAdiSoyadi}, Ortalama Prim: {ortalama}\n"

def primOku():
    with open("prim.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(primHesapla(satir))

def primKaydet():
    with open("prim.txt", "r", encoding="utf-8") as file:
        liste = []

        for satir in file:
            liste.append(primHesapla(satir)) 

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            file2.writelines(liste)
    print("Güncel Primler Başariyla Kaydedildi")

while True:
    islem = input("1-Prim Gir\n2-Primleri Kontrol Et\n3-Primleri Kaydet\n4-Çikiş Yap\nSeciminizi Giriniz: ")

    if islem == "1":
        primGir()
    elif islem == "2":
        primOku()
    elif islem == "3":
        primKaydet()
    elif islem == "4":
        break
    else: print("Lutfen Gecerli Bir Deger Giriniz!")
