# operasi komparasi

# setiap hasil dari operasi komprasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print("======lebih besar dari (>)")
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)


# kurang dari <
print("======kurang dari (<)")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print("======lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)


# kurang dari sama dengan <=
print("======kurang dari sama dengan (<=)")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan (==)
print("======sama dengan (==)")
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print("======tidaksama dengan (==)")
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

 
# 'is' sebagai komparasi objek identity
print("======objek identity (is)")
x = 5 # ini adalah assognment membuat object
y = 5 
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai x =,',y,'id = ',hex(id(y)))
hasil = x is y 
print('x is y =',hasil)

x = 5 # ini adalah assognment membuat object
y = 6 
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai x =,',y,'id = ',hex(id(y)))
hasil = x is y 
print('x is y =',hasil)

print("======objek identity (is not)")
x = 5 # ini adalah assognment membuat object
y = 5 
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai x =,',y,'id = ',hex(id(y)))
hasil = x is not y 
print('x is y =',hasil)

x = 5 # ini adalah assognment membuat object
y = 6 
print('nilai x =,',x,'id = ',hex(id(x)))
print('nilai x =,',y,'id = ',hex(id(y)))
hasil = x is not y 
print('x is y =',hasil)