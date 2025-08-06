# with open("markalar.txt", "a", encoding="utf-8") as file:
#     file.write("5-Audi")


# with open("markalar.txt", "r+", encoding="utf-8") as file:
#     markalar = file.read()
#     markalar = "1-Toyota\n" + markalar #burayı toplu oluşturdu
#     file.seek(0) #başlangıçtan al
#     file.write(markalar) #en sonda en baştan burayı yazdı

with open("markalar.txt","r+", encoding="utf-8") as file:
    markalar = file.readlines()
    markalar.insert(2, "7- Ford\n")
    file.seek(0)
    # for marka in markalar:
    #     file.write(marka)
    file.writelines(markalar) #tüm listeyi baştan sonra yazar for loop ile uğraşma

with open("markalar.txt", "r", encoding="utf-8") as file:
    print(file.read())