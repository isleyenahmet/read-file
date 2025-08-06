# file = open("log.txt", encoding="utf-8")  #bir log.txt dosyasi oluşturduk
# print(file.read())
# file.close() # bellekteki oluşturulan file objesi silinsin
#Yukarıdaki onca işlemi yapmaktansa aşağıda veriğim komutla bunların hepsini kolay bir şekilde yapabilirsin

# print(file.read(10)) #işlem sonu close demene gerek yok with bunu kendi yapıyor zaten
# print(file.tell()) #tell konum gösterir nerede olduğunu
# print(file.read()) # 10. satırdan dosyanın sonuna kadar olan her şeyi yazdırır
# print(file.tell()) #bu da dosya işaretçisinin son konumunu verir

try:
    with open("log.txt", encoding="utf-8") as file:
        for i in file:
            print(i, end="") #her okumadan sonra boşluk bırakma
except FileNotFoundError as e:
    print("Dosya Okuma Hatasi")
    
