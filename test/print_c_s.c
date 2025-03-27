#include "main.h"
/**
 * print_c - Prints characters from the list of arguments.
 * @ptr: Pointer to the list of arguments.
 * Return: the count of characters printed.
*/
int print_c(va_list *ptr)
{
	char a = va_arg(*ptr, int);

	_putchar(a);
	return (1);
}
/**
 * print_s - prints string from the list of arguments.
 * @ptr: Pointer to the list of arguments.
 * Return: the count of characters printed.
 */
int print_s(va_list *ptr)
{
	char *a = va_arg(*ptr, char *);
	char *b = "(Null)";
	int count = 0, i, j;

	for (i = 0; a[i] != '\0'; i++)
	{
		_putchar(a[i]);
		count++;
	}
	if (a == NULL)
	{
		for (j = 0; b[j] != '\0'; j++)
		{
			_putchar(b[j]);
			count++;
		}
	}
	return (count);
}
