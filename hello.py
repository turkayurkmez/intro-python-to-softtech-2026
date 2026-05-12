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
