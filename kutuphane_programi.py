import json
from datetime import datetime
kitap_listesi = []
kitap_nerede = ()
try:
    with open("veri.json", "r") as dosya:
        kitap_listesi = json.load(dosya)
except:
    pass
print("Kütüphaneye hoş geldiniz size nasıl yardımcı olabilirim? ..")
while True:
    print("""
        (1) Kitap listesini gör
        (2) Kitap ekle
        (3) Kitap ver
        (4) Kitap sil
        (5) Kitap ara


    çıkmak için q'ya basınız
    """)
    kontrol = input("Lütfen yapacağınız işlemi seçiniz(1,2,3,4): ")
    if kontrol == "1":
        print("*KÜTÜPHANE*")
        print("-"*len("*KÜTÜPHANE*"))
        print("\n")
        for d in kitap_listesi:
            for anahtar,deger in d.items():
                print(anahtar.capitalize(),deger.title(), end="\t")
            print("\n")
    elif kontrol == "2":
        eklenen_kitap = input("Kitap ekleyiniz: ").lower()
        kitap_nerede = "kütüphane"
        selami = True
        for i in kitap_listesi:
            if i["isim: "] == eklenen_kitap:
                print("Bu kitap zaten kütüphanenizde bulunuyor")
                selami = False
                break
        if selami:
            degisken = {
                "isim: ": eklenen_kitap,
                "kimde: ": kitap_nerede,
                "zaman: ": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            kitap_listesi.append(degisken)
            with open("veri.json", "w") as dosya:
                json.dump(kitap_listesi, dosya, indent=4)
            print(eklenen_kitap," eklendi")
    elif kontrol == "3":
        sorgulanan_kitap = input("Hangi kitabı sorgulamak istiyorsunuz? ").lower()
        kitap_yok = True
        for i in kitap_listesi:
            if i["isim: "] == sorgulanan_kitap:
                kitap_yok = False
                print("\n")
                print(f"""bu kitap {i["kimde: "]} konumunda""")
                evet_hayir = input("""Değiştirmek ister misiniz? 
                EVET  için 1'e basınız
                HAYIR için enter'a basınız """)
                if evet_hayir == "1":
                    kitap_nerede = input("..").lower()
                    i["kimde: "] = kitap_nerede
                    with open("veri.json", "w") as dosya:
                        json.dump(kitap_listesi, dosya, indent=4)
        if kitap_yok:
            print("\n")
            print("Bu kitap kütüphanede bulunmuyor")
    elif kontrol == "4":
        silinen = input("Silmek istediğiniz kitabın adını giriniz: ").lower()
        turgut = True
        for i in kitap_listesi:
            if i["isim: "] == silinen:
                print("basarılı")
                kitap_listesi.remove(i)
                turgut = False
                with open("veri.json", "w") as dosya:
                    json.dump(kitap_listesi, dosya, indent=4)
        if turgut:
            print("Bu kitap kütüphanizde bulunmuyor")
    elif kontrol == "5":
        arananan_kitap = input("Aratmak istediğiniz kitabı yazınız: ").split()
        kontrolumuz = True
        for i in arananan_kitap:
            for z in kitap_listesi:
                for k in z["isim: "].split():
                    if i == k:
                        print(z["isim: "].title(),"---->",z["kimde: "])
                        kontrolumuz = False
                        with open("veri.json", "w") as dosya:
                            json.dump(kitap_listesi, dosya, indent=4)
        if kontrolumuz:
            print("kitap adını doğru şekilde giriniz")
    if kontrol == "q":
        break