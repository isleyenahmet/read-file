# file = open("log2.txt", "w", encoding="utf-8") #yazma modunda açtık
# file.write("Ahmet İşleyen\n")
# file.close() #dosyayi kaydet ve kapat

with open("log2.txt", "w", encoding="utf-8") as file: #yazma
    file.write("Ahmet İşleyen\n")
    file.write("Sema Nur Çağlar")
    
with open("log2.txt", "r", encoding="utf-8") as file: #okuma
    for i in file:
        print(i, end="")