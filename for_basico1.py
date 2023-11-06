
#1 Basico
for i in range(0,151):
    print(i)
print("-------------------")
#2 multiplos de 5
for i in range(5,1001,5):
    print (i)
print("-------------------")
#3 Contar, a la manera del Dojo
for x in range(0,101):
    if x % 10 == 0:
        print("coding dojo")
        continue
    elif x % 5 == 0:
        print("Coding")
        continue
    else:
        print(x)
        continue
print("-------------------")
#4 Whoa. Es un gran idiota
suma_numeros_impares = 0 
for i in range(1,50001,2):
    suma_numeros_impares += i
print("la suma de numeros impares es : ", suma_numeros_impares)
print("-------------------")
#5 Cuenta regresiva de a 4
for cuenta_regresiva in range(2018,0,-4):
    print(cuenta_regresiva)
print("-------------------")
#6 Contador flexible
lowNum=1
highNum=10
mult=2
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)
