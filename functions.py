# bir uygulamada tekrar eden her eylem için bir fonksiyon yazılmalı. Bu sayede daha geliştirilebilir ve okunabilir
# bir kod yapısı olur. Her fonksiyon sadece bir iş yapmalı.

def islem_tamamlandi_mesaji_goster():
    print("İşlem tamamlandı")

def topla(x, y):
    return x + y



islem_tamamlandi_mesaji_goster()
islem_tamamlandi_mesaji_goster()
toplam = topla(5,8)
print(toplam)