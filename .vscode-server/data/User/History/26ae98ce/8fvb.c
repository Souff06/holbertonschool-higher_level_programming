#include "main.h"
/**
 * flip_bits - Counts the number of bits needed to be
 *             flipped to get from one number to another.
 * @n: number giver
 * @m: The number to flip n to.
 * Return: The necessary number of bits to flip to get from n to m.
 */
unsigned int flip_bits(unsigned long int n, unsigned long int m)
{
	unsigned long int count = 0;
	unsigned long int xor = n ^ m;

	while (xor > 0)
	{
		count++;
		xor &= (xor - 1);
	}
	return (count);
}