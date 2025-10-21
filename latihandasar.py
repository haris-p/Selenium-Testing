a = ['indonesia', "malaysia", "pakistan"]
a.append("brunei")
c = ["rusia", "inggris", "meksiko"]
c.extend(a)
print(c)

b = input("Masukan nama negara: ")

if b in a:
    print("ada negara",a)
else:
    print("tidak ada negara tersebut")