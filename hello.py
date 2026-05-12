print("selam!")
# aha bu açıklama satırı.
# string ad = "Türkay";
ad = "Türkay"
soyad ="Ürkmez"
maas = 120000
aktif_mi = True

print(type(ad))
print(type(maas))
print(type(aktif_mi))

noneValue = None
print(noneValue)
print(type(noneValue))

maas = "yüz yirmi bin"
print(type(maas))
print(type(8))

maas = None
maas = "yüzyirmibin"
maas = 120_000

print(type(maas)== int) #Şimdilik True (doğru) ama kırılgan (her zaman garanti edemiyoruz)
print(isinstance(maas,int)) # Daha tutarlı. Her zaman doğru çalışır.
print(isinstance(maas,(int,float))) # Herhangi biri ise sonuç True

print("Çalışan: "+ ad + " " + soyad)
print(f"Çalışan: {ad} {soyad}")
print(f"Maaş: {maas:,} TL")
kidem_yil = 7
print(f"Kıdem ile birlikte {maas +  (maas * (0.03 * kidem_yil)) : .2f} TL")

print(f"""
       --- Çalışan Kartı ---
       Adı ve Soyadı: {ad} {soyad}
       Kıdem: {kidem_yil} yıl
       Maaş: {maas:,} TL
      """)

ad = input("Adınız:")
 # maas = int(input("Maaş bilgisi:")) # Eğer burada sözel bir ifade girilirse hata alacaksınız.
info = input("Maaş bilgisi")

if info.isdigit():
    maas = int(info)
    print("Maaş başarıyla int'e çevirildi")
else:
    print("Geçersiz giriş! Sadece rakam kabul ediliyor!!")
    maas =0

maas+=1000
print(maas)

scientific_notation= 1.5e3 # (1.5 * 10^3)
big_number = 1234567891012345678910
print(f"scientific tip: {type(scientific_notation)}, big_number ise {type(big_number)} tipinde")

complex_type = 3 + 4j
print(type(complex_type))

number1 = 9
number2 = 2

print(f"{number1} / {number2} = {number1 / 2}")
print(f"{number1} // {number2} = {number1 // 2}")
print(f"{number1} ** {number2} = {number1 ** number2}")