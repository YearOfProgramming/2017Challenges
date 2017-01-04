package main

import (
	"fmt"
)

type TreeNode struct {
	Left  *TreeNode
	Right *TreeNode
	Value int
}

func (t *TreeNode) String() string {
	l := ""
	if t.Left != nil {
		l = fmt.Sprintf(" %s", t.Left.String())
	}
	r := ""
	if t.Right != nil {
		r = fmt.Sprintf(" %s", t.Right.String())
	}
	return fmt.Sprintf("(%d%s%s)", t.Value, l, r)
}

func (t *TreeNode) Invert() {
	tmp := t.Left
	t.Left = t.Right
	t.Right = tmp
	if t.Left != nil {
		t.Left.Invert()
	}
	if t.Right != nil {
		t.Right.Invert()
	}
}

func main() {
	tree := &TreeNode{
		Value: 4,
		Left: &TreeNode{
			Value: 2,
			Left: &TreeNode{
				Value: 1,
			},
			Right: &TreeNode{
				Value: 3,
			},
		},
		Right: &TreeNode{
			Value: 7,
			Left: &TreeNode{
				Value: 6,
			},
			Right: &TreeNode{
				Value: 9,
			},
		},
	}
	fmt.Printf("Before: %s\n", tree)
	tree.Invert()
	fmt.Printf("After: %s\n", tree)
}
