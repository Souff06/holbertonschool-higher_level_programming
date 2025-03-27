#include "binary_trees.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * *binary_tree_node - Function that creates a binary tree node
 * @parent: the pointer to the parent node of the node to create
 * @value: the value to put in the new node
 * Return: a pointer to a new node or NULL
 */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
    binary_tree_t *new;
    new = malloc(sizeof(binary_tree_t));

    if (new == NULL)
        return (NULL);
    new->n = value;
    new->parent = parent;
    new->left = NULL;
    new->right = NULL;
    return (new);
}
