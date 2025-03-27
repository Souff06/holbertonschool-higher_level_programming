#include "sort.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/**
* swap - Function that swap 2 int values
* @array: the array of integer to sort
* @size: the size of array
* @bas: the low index of the sort range
* @haut: the hight index of the sort range
*/
void swap(int *array, size_t size, int *a, int *b)
{
    if (*a != *b)
    {
        *a = *a + *b;
        *b = *a - *b;
        *a = *a - *b;
        print_array((const int *)array, size);
    }
}

/**
* lomuto_partition - partitions the array
* @array: the array of integer to sort
* @size: the size of array
* @bas: the low index of the sort range
* @haut: the hight index of the sort range
* Return: size_t
*/
size_t lomuto_partition(int *array, size_t size, ssize_t bas, ssize_t haut)
{
    int i, j, pivot = array[haut];

    for (i = j = bas; j < haut; j++)
    {
        if (array[j] < pivot)
        {
            swap(array, size, &array[j], &array[i++]);
            swap(array, size, &array[i], &array[haut]);
            return(i);
        }
    }
}

/**
* quicksort - Function that partitionning via lomuto 
* @array: the array of integer to sort
* @size: the size of array
* @bas: the low index of the sort range
* @haut: the hight index of the sort range 
*/
void quicksort(int *array, size_t size, ssize_t bas, ssize_t haut)
{
    if (bas < haut)
    {
        size_t p = lomuto_partition(array, size, bas, haut);
        quicksort(array, size, bas, p - 1);
        quicksort(array, size, p + 1, haut);
    }
}

/**
* quick_sort - Function that sorts an array of
* integers in ascending order
* @array: the array to print
* @size: the size of array
*/
void quick_sort(int *array, size_t size)
{
    if (array == NULL || size == 0)
        return;
    quicksort(array, size, 0, size - 1);
}
