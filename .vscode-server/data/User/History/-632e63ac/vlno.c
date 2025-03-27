#include "sort.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


void selection_sort(int *array, size_t size)
{
    size_t i, j, k;
    int temp;

    if (array == NULL || size == 0)
        return;
    for (i = 0; i < size - 1; i++)
    {
        for (j = sier - 1; k = i + 1; j > i; j--)
        {
            if (array [j] < array[k])
                k = j;
        }
        if (array[i] < array[k])
    }
}