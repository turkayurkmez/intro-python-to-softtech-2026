#isterseniz bütün dosyadaki fonksiyonları import edersiniz.
#import employee_utils
#ister yalnızca ihtiyacınız olanm fonksiyonu import edersiniz
#from employee_utils import kidem_yil, rapor_goster

#eğer proje büyürse, daha fazla py dosyası üzerinde işlem yapılırsa birden fazla klasör gerekebilir
#bu nedenle, __init__ ile ayrı modüller geliştirilebilir.
from utils import kidem_yil,rapor_goster

if __name__ == "__main__":
    print("uygulama başlangıcı")
    calisanlar = [
        {"id":1, "ad":"Mehmet Yılmaz", "ise_giris":"2018-06-01"},
        {"id":2, "ad":"Filiz Yılmaz", "ise_giris":"2020-03-15"}
        ]
    
    for calisan in calisanlar:
        yil = kidem_yil(calisan["ise_giris"])
        print(yil)

for key,value in rapor_goster(calisanlar).items():
    print(key,value)
    

