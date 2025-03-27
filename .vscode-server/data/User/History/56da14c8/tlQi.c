#include "binary_trees.h"
/**
 * binary_tree_balance - Function that measures the balance
 * factor of a binary tree
 * @tree: the pointer to the root node of the tree to
 * measure the balance factor
 * Return: 
 */
int binary_tree_is_full(const binary_tree_t *tree)
{
    if (tree == NULL)
        return (1);
    if ((tree->left == NULL && tree->right != NULL) ||
        (tree->left != NULL && tree->right == NULL))
        return (0);
    return (binary_tree_is_full(tree->left) && binary_tree_is_full(tree->right));
}
