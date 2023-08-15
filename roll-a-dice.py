import random

jogada = "y"
while jogada == "y":
    n = random.randint(1,6)
    if n == 1:
        print("[-----]")
        print("[-----]")
        print("[--1--]")
        print("[-----]")
        print("[-----]")
    if n == 2:
        print("[-----]")
        print("[2----]")
        print("[-----]")
        print("[----2]")
        print("[-----]")
    if n == 3:
        print("[-----]")
        print("[3----]")
        print("[--3--]")
        print("[----3]")
        print("[-----]")
    if n == 4:
        print("[-----]")
        print("[4---4]")
        print("[-----]")
        print("[4---4]")
        print("[-----]")
    if n == 5:
        print("[-----]")
        print("[5---5]")
        print("[--5--]")
        print("[5---5]")
        print("[-----]")
    if n == 6:
        print("[-----]")
        print("[6---6]")
        print("[6---6]")
        print("[6---6]")
        print("[-----]")
    jogada = input("Precione Y para jogar novamente e N para sair: ")
    print("\n")