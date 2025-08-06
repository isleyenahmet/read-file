def not_gir():
    ad = input("Ogrenci Adi: ")
    soyAd = input("Ogrenci SoyAdi: ")
    not1 = input("1. Notu Giriniz: ")
    not2 = input("2. Notu Giriniz: ")
    not3 = input("3. Notu Giriniz: ")
    
    with open("not.txt","a", encoding="utf-8") as file:
        file.write(ad+ " " + soyAd + ":" + not1 + " " + not2 + " " + not3+ "\n")

def not_hesapla(satir):
    satir = satir[:-1] #boşluğu gözardı et
    liste = satir.split(":") #listeyi isim soyisim ve notlardan böl

    ogrenciAdi = liste[0]
    notlar = liste[1].strip().split()

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3
    if ortalama >= 90 and ortalama <= 100: harf = "AA"
    elif ortalama >= 80 and ortalama <= 89: harf = "BA"
    elif ortalama >= 75 and ortalama <= 79: harf = "BB"
    elif ortalama >= 70 and ortalama <= 74: harf = "CB"
    elif ortalama >= 65 and ortalama <= 69: harf = "CC"
    elif ortalama >= 60 and ortalama <= 64: harf = "DC"
    elif ortalama >= 50 and ortalama <= 59: harf = "DD"
    elif ortalama >= 40 and ortalama <= 49: harf = "FD"
    elif ortalama >= 0 and ortalama <= 39: harf = "FF"

    return f"{ogrenciAdi}: {harf} ({ortalama})\n"

    
def not_oku():
    with open("not.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
def notlari_kaydet():
    with open("not.txt", "r", encoding="utf-8") as file: #yazıyoruz burada
        liste = []

        for satir in file:
            liste.append(not_hesapla(satir)) #not hesapla fonk satırların hepsinin liste ye ekle

        with open("sonuclar.txt", "w", encoding="utf-8") as file2: #yazdım yeni bilgileri
            file2.writelines(liste) #writeline birden fazla satırı yazmak için kullanılır


while True:
    islem = input("1-Not Gir\n2-Notlari Oku\n3-Notlari Kaydet\n4-Çikis Yap\nSeciminizi Giriniz: ")


    if islem == "1":
        not_gir()
    elif islem == "2":
        not_oku()
    elif islem == "3":
        notlari_kaydet()
    elif islem == "4":
        break
    else: print("Gecerli Bir Deger Giriniz!")