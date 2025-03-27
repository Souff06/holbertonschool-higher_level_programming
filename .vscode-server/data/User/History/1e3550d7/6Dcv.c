#include "main.h"
/**
 * get_bit - that returns the value of a bit at a given index.
 * @n: number given
 * @index: index to return the bit
 * Return: If b is NULL or contains chars not 0 or 1 - 0.
 *         Otherwise - the converted number.
 */
int get_bit(unsigned long int n, unsigned int index)
{
	if (index > 63)
		return (-1);

	return (n >> index & 1);
}
