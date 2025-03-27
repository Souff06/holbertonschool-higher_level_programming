#ifndef MAIN_H
#define MAIN_H
#include <stdio.h>
#include <stdarg.h>
/**
 * struct print - Structure defining a format specifier and
 *                its corresponding printing function.
 * @symbol: A character representing the format specifier,
 *          such as 'c' for character or 'd' for integer.
 * @f: Pointer to the printing function associated with the format specifier.
*/
typedef struct print
{
    char symbol;
    int (*f)(va_list *);
} print_f;
int _printf(const char *format, ...);
int _putchar(char c);
int print_s(va_list *ptr);
int print_c(va_list *ptr);
void help_i(int i, int *count);
int print_i(va_list *ptr);
#endif
