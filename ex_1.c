#include <stdio.h>
#include <string.h>

int main() {
    char str[100];

    printf("Digite uma string: ");
    scanf("%s", str);

    printf("String invertida: ");
    for (int i = strlen(str) - 1; i >= 0; i--) {
        printf("%c", str[i]);
    }
    printf("\n");

    return 0;
}