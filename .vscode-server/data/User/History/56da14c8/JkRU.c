#include "binary_trees.h"
/**
 * binary_tree_is_full - Checks if a binary tree is full
 * @tree: Pointer to the root node of the tree to check
 * Return: 1 if the tree is full, 0 otherwise
 */
int binary_tree_is_full(const binary_tree_t *tree)
{
	int child_1 = 0;
	int child_2 = 0;

	if (tree == NULL)
		return (0);

	if (tree->left != NULL)
		child_1 = 1 + child_1 + binary_tree_is_full(tree->left);

	if (tree->right != NULL)
		child_2 = 1 + child_2 + binary_tree_is_full(tree->right);

	if (child_1 == child_2)
		return (1);

	else
		return (0);
}

