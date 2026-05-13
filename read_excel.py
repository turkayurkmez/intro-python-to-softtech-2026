import pandas as pd

# bu kodun çalışması için:
# 1. pip install openpyxl
# 2. pip install pandas

df = pd.read_excel("personel.xlsx")
muhendisler = df[df["departman"]== "Mühendislik"]
print(df)
print()
print(muhendisler)

print(f"Ortalama maaş: {df['maas'].mean():,.0f} TL")
print(f"En fazla maaş: {df['maas'].max():,.0f} TL")
print(f"En düşük maaş: {df['maas'].min():,.0f} TL")

dictionary = df.to_dict(orient="records")
print(dictionary)
print(dictionary[0]["ad"])

