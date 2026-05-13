#Kullanıcı terminal aracılığıyla sisteme kayıt olacaktır. Her alan doğru bir biçimde doldurulana kadar form ilerlemez.

gecerli_departmanlar = ["Mühendislik","İK","Pazarlama","Finans"]

calisanlar = []

print("Çalışan kaydı başlıyor. Çıkmak için q'ya yazınız")

#1. Ad ve Soyad
#2. departman
#3. maaş

#4. tamamı doğru bir biçimde doldurulduğunda çalışanlar list'ine eklenecek.
while True:
    while True:
        ad = input("Ad ve Soyadı giriniz (çıkmak için 'q')")
        if ad != "":
            break

    if ad.lower() == 'q':
        break
    while True:
        departman = input("departman:").strip()
        if departman  in gecerli_departmanlar:
            break

        print("Hata: Geçersiz departman!")
    
    while True:
        maas_str = input('maaş:').strip()
        if maas_str.replace(".","",-1).isdigit() and float(maas_str) > 0:
            maas = float(maas_str)
            break
        print("Hata: Geçersiz maaş")

    calisan = {"ad":ad, "departman":departman, "maas":maas}
    calisanlar.append(calisan)


    print(f"Kayıt eklendi. Toplam çalışan sayısı:",len(calisanlar))



for calisan in calisanlar:
    print(calisan["ad"],calisan["departman"],calisan["maas"])