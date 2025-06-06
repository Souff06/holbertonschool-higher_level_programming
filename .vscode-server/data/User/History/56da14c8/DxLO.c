#include "binary_trees.h"


int binary_tree_is_full(const binary_tree_t *tree)
{
    if (tree == NULL)
        return (1);
    if ((tree->left == NULL && tree->right != NULL) ||
        (tree->left != NULL && tree->right == NULL))
        return (0);
}
