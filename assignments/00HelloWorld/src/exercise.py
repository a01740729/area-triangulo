import math
def main():
    #escribe tu código abajo de esta línea
    pass

    a = int(input('Dame el lado a: '))
    b = int(input('Dame el lado b: '))
    c = int(input('Dame el lado c: '))

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print('El área es: '+str(area))


if __name__=='__main__':
    main()
