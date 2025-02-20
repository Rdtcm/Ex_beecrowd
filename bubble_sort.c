#include <stdio.h>


int main() {
    int vet[] = {5,4,3,2,1};
    int tamanho = 5;

    //ordenando
    for (int i=0; i < tamanho - 1; i++) {
        for (int j=0; j < tamanho - 1 - i; j++)
            if (vet[j] > vet[j+1]) {
                int aux = vet[j];
                vet[j] = vet[j+1];
                vet[j+1] = aux;
            }
    }
    //printando
    for (int k=0; k < tamanho; k++) {
        printf("%d", vet[k]);
    }
    printf("\n");

    return 0;
}