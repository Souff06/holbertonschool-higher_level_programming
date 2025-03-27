#include "binary_trees.h"
/**
* binary_tree_leaves - function that prints the total number of leaves
* @tree: pointer to the root of the binary tree
* Return: number of leaves
*/

size_t binary_tree_leaves(const binary_tree_t *tree)
{
	size_t leaves = 0;

	if (tree == NULL)
	{
		return (0);
	}

	leaves = leaves + binary_tree_leaves(tree->left);
	leaves = leaves + binary_tree_leaves(tree->right);

	if (tree->left == NULL && tree->right == NULL)
	{
		leaves++;
	}

	return (leaves);
}

/**
* binary_tree_height - function that measures the height of a binary tree
* @tree: pointer to the binary tree
* Return: balance factor of the binary tree
*/

size_t binary_tree_height(const binary_tree_t *tree)
{
	size_t height_left, height_right;

	if (tree == NULL)
		return (0);

	if (tree->left == NULL && tree->right == NULL)
		return (0);

	height_left = binary_tree_height(tree->left);
	height_right = binary_tree_height(tree->right);

	if (height_left > height_right)
	{
		return (height_left + 1);
	}
	else
	{
		return (height_right + 1);
	}
}
/**
* binary_tree_is_perfect - function that checks if a binary tree is perfect
* @tree: pointer to the binary tree to check
* Return: 1 if perfect, 0 if not
*/

int binary_tree_is_perfect(const binary_tree_t *tree)
{
	size_t height, leaves, isperfect;

	if (tree == NULL)
		return (0);

	height = binary_tree_height(tree);
	leaves = binary_tree_leaves(tree);
	isperfect = (1 << height);

	if (leaves == isperfect)
		return (1);
	else
		return (0);
}