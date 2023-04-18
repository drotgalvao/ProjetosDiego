#include <stdio.h>
#include <locale.h>

int main() {
	setlocale(LC_ALL, "portuguese");
    int num;
    printf("Digite um n�mero para verificar se pertence � sequ�ncia de Fibonacci: ");
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
        printf("%d pertence � sequ�ncia de Fibonacci.\n", num);
    } else {
        printf("%d n�o pertence � sequ�ncia de Fibonacci.\n", num);
    }

    return 0;
}
