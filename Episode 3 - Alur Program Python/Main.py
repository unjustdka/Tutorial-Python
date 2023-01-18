import time
start_time = time.time()
print("Hello")
print("Hello World")
a = 10 # ini adalah comment
# ini juga comment
# di eksekusi berdasarkan urutan

print(a)
for i in range(1,1000):
    a = 10

print(time.time() - start_time, "detik")
# kita bisa mengcopile python ke bytecode
# cara mengcompile, buka terminal dan tuliskan
# python -m py_compile Main.pyc