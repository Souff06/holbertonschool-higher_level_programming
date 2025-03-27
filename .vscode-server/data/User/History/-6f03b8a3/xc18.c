#include "binary_trees.h"


int height(struct Node* node) 
{
    int leftHeight = height(node->left);
    int rightHeight = height(node->right);
    
    if (node == NULL)
        return 0;
    if (leftHeight > rightHeight)
        return leftHeight + 1;
    else
        return rightHeight + 1;
}