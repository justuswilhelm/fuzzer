#include "stdint.h"
#include "stdio.h"
#include "stdlib.h"

int main(void) {
    char input[128] = {0};
    char output[] = "hello world";
    fgets(input, sizeof(input), stdin);
    int length = atoi(input);
    // Simple
    // printf("%.*s", length, output);
    // Lol
    for (int i = 0; i < length; i++){
        putchar(output[i]);
    }
}
