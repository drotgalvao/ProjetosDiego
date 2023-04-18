#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "portuguese");
    int num;
    printf("Digite um número para verificar se pertence à sequência de Fibonacci: ");
    scanf("%d", &num);

    int a = 0;
    int b = 1;
    int c = 0;

    while (c < num) {
        c = a + b;
        a = b;
        b = c;
    }

    if (c == num) {
        printf("%d pertence à sequência de Fibonacci.\n", num);
    } else {
        printf("%d não pertence à sequência de Fibonacci.\n", num);
    }

    return 0;
}
