#include <iostream>
#include <string>
#include <vector>
#include <functional>

static const std::string EMPTY = "#";

struct BinaryTreeNode
{
	std::string value;
	BinaryTreeNode* leftChild;
	BinaryTreeNode* rightChild;
};

void traverseInOrder(BinaryTreeNode* root, std::function<void(BinaryTreeNode*)> func)
{
	if (root != nullptr)
	{
		traverseInOrder(root->leftChild, func);
		traverseInOrder(root->rightChild, func);
	}
	func(root);
}

void traversePreOrder(BinaryTreeNode* root, std::function<void(BinaryTreeNode*)> func)
{
	func(root);
	if (root != nullptr)
	{
		traversePreOrder(root->leftChild, func);
		traversePreOrder(root->rightChild, func);
	}
}

BinaryTreeNode* treeFromInputRec(BinaryTreeNode* root, std::vector<std::string>::const_iterator& pos, std::vector<std::string>::const_iterator end)
{
	if (*pos != EMPTY)
	{
		root->leftChild = treeFromInputRec(new BinaryTreeNode{ *pos, nullptr, nullptr }, ++pos, end);
	}
	pos++;
	if (*pos != EMPTY)
	{
		root->rightChild = treeFromInputRec(new BinaryTreeNode{ *pos, nullptr, nullptr }, ++pos, end);
	}
	return root;
}

BinaryTreeNode* binaryTreeFromPreOrderInput(std::vector<std::string> input)
{
	BinaryTreeNode* root = new BinaryTreeNode{ input.front(), nullptr, nullptr };
	return treeFromInputRec(root, ++input.cbegin(), input.cend());
}


int main(int argc, char* argv[])
{
	std::vector<std::string> treeInPreOrder(argv + 1, argv + argc);
	BinaryTreeNode* tree = binaryTreeFromPreOrderInput(treeInPreOrder);
	traverseInOrder(tree, [](BinaryTreeNode* node)
	{
		if (node)
		{
			auto temp = node->leftChild;
			node->leftChild = node->rightChild;
			node->rightChild = temp;
		}
	});

	traversePreOrder(tree, [](BinaryTreeNode* node)
	{
		std::cout << (node ? node->value : EMPTY) << " ";
	});
	std::cout << std::endl;


}

