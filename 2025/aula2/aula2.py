import os
from itertools import permutations
import math

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') 

def permutar_palavra(palavra):
    permutacoes = set("".join(p) for p in permutations(palavra))
    i = 1
    for perm in sorted(permutacoes):
        print(i,"°: ",perm,sep="")
        i += 1

def carregar_dicionario(arquivo="br-utf8.txt"):
    with open(arquivo, encoding="utf-8") as f:
        return set(p.strip().lower() for p in f)

def encontrar_anagramas(palavra, dicionario):
    permutacoes = set("".join(p) for p in permutations(palavra))
    return permutacoes.intersection(dicionario)

def main():
    while True:
        limpar_terminal()
        op = input("Digite 1 para permutar uma palavra\n"
                   "Digite 2 para encontrar anagrama no dicionário\n"
                   "Digite 3 para calcular fatorial\n"
                   "Digite 4 para calcular permutação com repetição\n"
                   "Digite 5 para calcular combinação\n"
                   "Digite 0 para encerrar o programa\n")

        if op == "0":
            break

        match op:
            case "1":
                palavra = input("Digite uma palavra: ")
                permutar_palavra(palavra)

            case "2":
                dicionario = carregar_dicionario()
                palavra = input("Digite uma palavra: ").lower()
                anagramas = encontrar_anagramas(palavra, dicionario)
                print("Anagramas encontrados:", ", ".join(anagramas) if anagramas else "Nenhum anagrama encontrado.")

            case "3":
                n = int(input("Digite n para calcular n! : "))
                res = math.factorial(n)
                print(f"{n}! = {res}, número de algarismos: {len(str(res))}")

            case "4":
                n = int(input("Digite o n números de elementos: "))
                A = [int(x) for x in input("Digite em uma só linha os números de repetições: ").split()]
                res = math.factorial(n)
                for ai in A:
                    res = res/math.factorial(ai)
                print("Permutações com repetição: ",int(res))

            case "5":
                n = int(input("Digite o n números de elementos: "))
                k = int(input("Digite o k, 0 <= k <= n, elementos da escolha: "))
                print("Combinações : ", int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k))) )
            
            case _:
                print("Opção inválida")

        input("\nPressione Enter para continuar...") 

if __name__ == "__main__":
    main()