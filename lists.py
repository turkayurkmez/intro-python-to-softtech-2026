   #           0                       1          2       3 
books = ['Benim adım kırmızı',"Küçük Prens","Sefiller","Vakıf"]
print(books)
print(books[0])

print(books[len(books)-1])
print(books[-1])
print(books[-2])

books.append("Zihin Toplumu")
books.insert(-2,"Doktor Oks")

print(books)

personel_info = ["Türkay","Ürkmez",46,True]

son_kitap = books.pop()
print(son_kitap)
print(books)

del books[1]
print(books)

list1 = [1,2,3]
list2 = [4,5,6]

combined_list = list1 + list2
print(combined_list)
print(f"ilk iki kitap: {books[0:2]}") # Slicing
print(f"ilk iki kitap: {books[:2]}")
print(f"2. ve 3. kitap: {books[1:3]}")
print(f"ilk iki kitap: {books[2:]}")
print(f"Tersine çevir: {books[::-1]}")
print(f"Gözlem:: {books[::2]}")



