# angka satuan (integer)
data_integer = 11
print("data : ", data_integer)
print("- bertipe :", type (data_integer))

# angka dengan koma (float)

data_float = 1,5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# kumpulan karakter (string)

data_string = "ucup 10"
print("data : ", data_string)
print("- bertipe :", type (data_string))

# binar true/false (boolean)

data_bool = True
print("data : ", data_bool)
print("- bertipe :", type (data_bool))

# data khusus
# bilangan kompleks

data_complex = complex (5,6)
print("data : ", data_complex)
print("- bertipe :", type (data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe :", type(data_c_double))
