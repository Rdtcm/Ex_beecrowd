#desenvolvendo um algoritmo de ordenacao por bubble sort

def bubble_sort(vet):
    for i in range(len(vet)):
        for j in range(len(vet) - 1 - i):
            if vet[j] > vet[j+1]:
                aux = vet[j]
                vet[j] = vet[j+1]
                vet[j+1] = aux
    return vet

def main():
    vetor = [5,4,3,2,1]
    novo_vetor = bubble_sort(vetor)
    print(f"Vetor ordenado: {novo_vetor}")

if __name__ == '__main__':
    main()