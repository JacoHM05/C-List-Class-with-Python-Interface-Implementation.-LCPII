import ctypes  #Necesario importar ctypes para usar las funciones de 

lib = ctypes.CDLL('./learning.dll')    #Agregar archivo C++

#declarar tipos para funciones, por cada una
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]   
lib.add.restype = ctypes.c_int


a = 5
b = 8

#necesario usar lib.
resultado = lib.add(a, b)
print("resultado:",resultado)