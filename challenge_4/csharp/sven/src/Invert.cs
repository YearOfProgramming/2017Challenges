using System;
using System.Linq;
using System.Collections.Generic;

namespace Challenge_4
{
    class BinaryTreeNode
    {
        public BinaryTreeNode(string val, BinaryTreeNode left, BinaryTreeNode right)
        {
            value = val;
            leftChild = left;
            rightChild = right;
        }
        public string value;
        public BinaryTreeNode leftChild;
        public BinaryTreeNode rightChild;
    }

    class Program
    {
        const string EMPTY = "#";
        static BinaryTreeNode binaryTreeFromPreOrderInput(ref IEnumerable<string> input)
        {
            BinaryTreeNode root = new BinaryTreeNode(input.ElementAt(0), null, null);

            if (input.Count() > 1 && input.ElementAt(1) != EMPTY)
            {
                input = input.Skip(1);
                root.leftChild = binaryTreeFromPreOrderInput(ref input);
            }
            input = input.Skip(1);
            if (input.Count() > 1 && input.ElementAt(1) != EMPTY)
            {
                input = input.Skip(1);
                root.rightChild = binaryTreeFromPreOrderInput(ref input);
            }
            return root;
        }

        static BinaryTreeNode traversePreOrder(BinaryTreeNode tree, Func<BinaryTreeNode, BinaryTreeNode> func)
        {
            tree = func(tree);
            if (tree != null)
            {
                tree.leftChild = traversePreOrder(tree.leftChild, func);
                tree.rightChild = traversePreOrder(tree.rightChild, func);
            }
            return tree;
        }

        static BinaryTreeNode traverseInOrder(BinaryTreeNode tree, Func<BinaryTreeNode, BinaryTreeNode> func)
        {
            if (tree != null)
            {
                tree.leftChild = traverseInOrder(tree.leftChild, func);
                tree.rightChild = traverseInOrder(tree.rightChild, func);
            }
            return func(tree);
        }

        static void Main(string[] args)
        {
            IEnumerable<string> input = args.AsEnumerable();
            BinaryTreeNode tree = binaryTreeFromPreOrderInput(ref input);

            tree = traverseInOrder(tree, node => node != null ? new BinaryTreeNode(node.value, node.rightChild, node.leftChild) : null);
            traversePreOrder(tree, node => { Console.Write((node != null ? node.value : EMPTY) + " "); return node; } );

            int x = 3;

            //Console.WriteLine(args.GroupBy(val => val).OrderBy(g => g.Count()).Last().Key);
        }
    }
}