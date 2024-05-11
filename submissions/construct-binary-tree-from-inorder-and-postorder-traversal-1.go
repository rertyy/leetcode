// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 import "fmt"
func buildTree(inorder []int, postorder []int) *TreeNode {
    n := len(inorder)
    if n == 0 {
        return nil
    } else if n == 1 {
        return &TreeNode{Val: postorder[0]}
    }
    fmt.Println(postorder)
    fmt.Println(n-1)
    root := TreeNode{Val: postorder[n-1]}

    for i, ele := range inorder {
        if ele == root.Val {
            root.Left = buildTree(inorder[:i], postorder[:i])
            root.Right = buildTree(inorder[i+1:], postorder[i:n-1])
            break
        }
    }
    return &root
}
