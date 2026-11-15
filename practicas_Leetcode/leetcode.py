#p001 two sum
nums = [2,7,11,15]
target = 9

def dos_sumas(lista, objetivo):
    encontrados = {}
    for key, valor in enumerate(lista):
        sobrante= objetivo - valor
        if sobrante in encontrados:
            return[encontrados[sobrante], key]
        else:
            encontrados[valor] = key
            


print(dos_sumas(nums, target))

# 002 números palíndromos

entrada = 121
n = entrada
inverso = 0
while n > 0 :
    extraer_ultimo = n % 10
    reduccion = n // 10
    inverso = (inverso * 10) + extraer_ultimo
    n = reduccion

if entrada == inverso:
    print("Verdadero")
else: 
    print("Falso")

# conversion de números romanos a enteros

s = "numero romano"

