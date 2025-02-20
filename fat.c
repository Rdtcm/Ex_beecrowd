#include <stdio.h>

//implementando o fatorial recursivo com c

int fat(int num) {
    if (num == 0 || num == 1) {
        return 1;
    }
    return num * fat(num-1);
}


int main() {
    int num;

    printf("Digite um numero: ");
    scanf("%d", &num);

    int fatorial = fat(num);

    printf("fatorial de %d: %d\n", num, fatorial);

    return 0;
}