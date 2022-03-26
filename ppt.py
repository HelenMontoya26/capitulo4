piedra= 1
papel= 2
tijera= 3
persona1=int(input("que elemento saco el jugador 1: "))
persona2= int(input("que elemento saco el jugador 2: "))
if persona1==piedra and persona2==papel :
    print("piedra es envuelta por el papel, gana el jugador2")
elif persona1==piedra and persona2==tijera:
    print("piedra daña a tijera, gana el jugador 1")
elif persona1==piedra and persona2==piedra:
    print("la piedra no daña a la piedra, nadie gana")
if persona1==papel and persona2==piedra:
    print("papel envuelve a piedra, gana el jugador 1")
elif persona1==papel and persona2==tijera:
    print("tijera corta al papel, gana jugador2")
elif persona1==papel and persona2==papel: 
    print("el papel no daña a papel, nadie gana")
if persona1==tijera and persona2==piedra:
    print("la tijera no daña la piedra, gana jugador 2")
elif persona1==tijera and persona2==papel:
    print("tijera corta el papel, gana jugador1")
elif persona1==tijera and persona2==tijera:
    print("tijera no corta a otra tijera, ningun jugador gana")

