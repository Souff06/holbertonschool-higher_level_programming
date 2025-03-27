#include "binary_trees.h"


int binary_tree_is_full(const binary_tree_t *tree)
{
    if (tree != NULL)
    {
        if (tree->left != NULL && tree->right != NULL)
            return (1);
        return (0);
    }
        return (1);
    return (0);
}
