renkler = {"kırmızı","pembe","beyaz","kırmızı","mavi"}
print("Renkler set'i: ", renkler)
print("Renkler eleman sayısı: ", len(renkler))

bos_kume = set()

sehirler = ["İstanbul","İstanbul","İstanbul","Ankara","Ankara"]
sehirler_kumesi = set(sehirler)
print(sehirler_kumesi)

print("renkler kümesinde mavi var mı:", "mavi" in renkler)
renkler.add("sarı")
renkler.remove("mavi")

while len(renkler) > 0:
    print('eleman sayıaı',len(renkler),'değer: ',renkler.pop())


print("renkler kümesi boş:",renkler)

#küme işlemleri
A = {1,2,3,4,5}
B = {4,5,6,7,8,9}

print("A U B ", A.union(B))
print("A kesişim B", A.intersection(B))
print("A fark B", A.difference(B))

C = {1,2}
print("C A'nın alt kümesi mi?", C.issubset(A))
print("A C'nın üst kümesi mi?", A.issuperset(C))
