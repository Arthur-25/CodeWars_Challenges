def encontra_maior(array):
    maior = 0
    index = 0

    for number in range(0,len(array),1):
        if (len(array[number])>maior):
            maior = len(array[number])
            index = number
    return index
def soma_strings(array,k):
    lista_nova = []
    for number in range (0,len(array)):
        stra = array[number]
        if (number<len(array)-1):
            for n in range (1,k):
                stra += array[number + n]


            lista_nova.append(stra)
    return lista_nova
def longest_consec(strarr, k):
    strarr = soma_strings(strarr,k)
    return strarr[encontra_maior(strarr)]

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"],2))