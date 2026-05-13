import random
#
# Sorulacak kelimeler hazırdır.
# tahmin edilen harfler ve deneme sayısı için bir değişkenler hazırdır
# 1. Rastgele bir kelime seç.
# 2. deneme sayısı, 6'dan küçük olduğu sürece:
#   3. kelimeyi _ _ _ _ gibi göster
#   4. kullanıcıdan harf iste
#   5. Eğer kelimede varsa o harfi göster
#   6. Yoksa "bu harf yok" de  
#   7. deneme sayısı her durumda arttır
#  8. Yeniden oynansın mı?  

# #

# Fonksiyonlar:
# rastgele_kelime_sec(liste)
# kelimeyi_goster(secilen_kelime, tahmin_edilen_harfler)
# harf_iste()
# harf_kelimede_var_mi
# yeniden_oynansin_mi


def rastgele_kelime_sec(kelime_listesi):
   return  random.choice(kelime_listesi)

def kelimeyi_goster(secilen_kelime, tahmin_edilen_harfler):
   bulmaca = ""
   #java
   # _ _ _ _
   for harf in secilen_kelime:
      if harf in tahmin_edilen_harfler:
         bulmaca += harf + " "
      else:
         bulmaca += "_ "
   return bulmaca.strip()

def harf_iste():
   while True:
      harf = input("bir harf tahmin edin:")
      if len(harf) ==1 and harf.isalpha():
         return harf
      else:
         print("geçerli bir harf girin")

def harf_kelimede_var_mi(harf, kelime):
   return harf in kelime


def yeniden_oynansin_mi():
   while True:
      yanit = input("yeniden oynamak ister misiniz (e/h)?").lower()
      if yanit in ["e","h"]:
         return yanit == "e"
      else:
         print("Sadece e ya da h geçerlidir")


def adam_asmaca():
   kelimeler = ["java","python", "javascript"]
   kelime = rastgele_kelime_sec(kelimeler)
   tahmin_edilen_harfler = []
   deneme = 6

   while deneme > 0:
      print("Kalan deneme şansınız:",deneme)
      print("Tahmin ettiğiniz harfler:",tahmin_edilen_harfler)
      print("Kelime:",kelimeyi_goster(kelime,tahmin_edilen_harfler))

      harf = harf_iste()

      if harf in tahmin_edilen_harfler:
         print("Bu harfi zaten denediniz")
         continue
      
      tahmin_edilen_harfler.append(harf)

      if not harf_kelimede_var_mi(harf,kelime):
         deneme -=1
         print("yanlış tahmin")
        
      if all( harf in tahmin_edilen_harfler for harf in kelime):
         print("Tüm kelimryi bildiniz")
         break
   else:
      print("Üzgünüm. kelimeyi bilemediniz. Doğrusu",kelime)
      
      #while/else eğer break ile çıkılmamış ise else bloğuna düşer..

   if yeniden_oynansin_mi():
       adam_asmaca()


