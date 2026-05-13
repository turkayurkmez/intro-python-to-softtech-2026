from datetime import date 

def kidem_yil(ise_baslama: str):
    baslama_tarihi = date.fromisoformat(ise_baslama)
    return (date.today() - baslama_tarihi).days // 365

def rapor_goster(calisanlar: list):
    return {
        "rapor_tarihi": date.today().isoformat(),
        "calisan_sayisi": len(calisanlar)       
    }

