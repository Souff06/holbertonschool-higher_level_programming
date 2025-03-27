#include "main.h"
/**
 * set_bit - ets the value of a bit to 1 at a given index
 * @n: number giver
 * @index: index to return the bit
 * Return: If b is NULL or contains chars not 0 or 1 - 0.
 *         Otherwise - the converted number.
 */
int set_bit(unsigned long int *n, unsigned int index)
{
	if (index > 63)
		return (-1);

	*n |= (1 << index);
	return (1);
}
