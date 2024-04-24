def resto_11():
    numeros =[]

    for num in range (1000,2001):
        if num % 11 == 5:
            numeros.append(num)

    return numeros
numeros_resto5 = resto_11()
print(f'Os números entre 1000 e 2000 que divididos por 11 , reste 5: {numeros_resto5}')