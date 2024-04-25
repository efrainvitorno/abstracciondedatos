#modulo para leer numero real 
def LeerNumeroReal(Texto="ingrese numero real:", Minimo=0, Maximo=10000.0 ):
    Nro=float(input(Texto))
    while (Nro<Minimo) or (Nro>Maximo):
        print("error numero fuera de rango")
        Nro=float(input(Texto))
    return Nro 
