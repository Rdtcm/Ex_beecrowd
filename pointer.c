//trocar valores de duas variaveis usando ponteiros

#include <stdio.h>

void trocar(int *x, int *y) {
    int tmp = *x;
    *x = *y;
    *y = tmp;
}


int main() {
    int a, b;
    a = 10;
    b = 15;
    printf("(a) vale %d e (b) vale %d\n", a, b);
    trocar(&a, &b);
    printf("(a) vale %d e (b) vale %d\n", a, b);

    return 0;
}