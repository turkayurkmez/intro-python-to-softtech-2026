calisan = {
    "ad":"Türkay",
    "soyad":"Ürkmez",
    "maas": 100_000,
    "kidem_yili":10,
    "aktif_mi":True,
    "adres":"Eskişehir"
}

# calisan nesnesi bir dictionary. Her value'ya belirtilen key ile erişilebilir.

print(calisan["ad"])
#print(calisan["departman"])

departman = calisan.get('departman','belirtilmemiş')
print(departman)
calisan["ad"] = "Derya"
calisan["departman"]="Yazılım Geliştirme"


print('Dict: ',calisan)
print('Keys:', calisan.keys())
print('Values:', calisan.values())

print('İkisi bir arada:', calisan.items())

for  anahtar, deger   in calisan.items():
    print(f"{anahtar:12} : {deger}")

calisanlar = [
 {"ad":"Ali", "soyad":"Yılmaz","maas":100_000, "departman":"Mühendislik"},
 {"ad":"Tümay", "soyad":"İnanmaz","maas":175_000, "departman":"İK"},
 {"ad":"İlknur", "soyad":"Aşer","maas":130_000, "departman":"Pazarlama", "telefonlar":["0544 111 11 11","0532 222 22 22"]}
]

for  calisan  in calisanlar:
    print(f"Ad: {calisan['ad']} {calisan['departman']}")


# sadece mühendislik departmanında çalışanları nasıl filtrelerim:
muhendisler = []
for  calisan  in calisanlar:
    print(f"Ad: {calisan['ad']} {calisan['departman']}")
    if calisan["departman"] == "Mühendislik":
        muhendisler.append(calisan)

print(muhendisler)

# List comprehension:
# calisanlar içindeki c'nin departmanı "Mühendislik" ise listeye at
engineers = [c for  c in calisanlar if c["departman"]=="Mühendislik"]
isimler = [c['ad'] for c in calisanlar]
print(engineers)
print(isimler)