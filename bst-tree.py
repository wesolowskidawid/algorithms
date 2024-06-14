class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def delete(self, key):
        # Base case: key not found
        if self is None:
            return self

        # If the key to be deleted is smaller than the root's key,
        # then it lies in the left subtree
        if key < self.val:
            self.left = self.left.delete(key)

        # If the key to be deleted is greater than the root's key,
        # then it lies in the right subtree
        elif key > self.val:
            self.right = self.right.delete(key)

        # If key is same as root's key, then this is the node to be deleted
        else:
            # Case 1: Node with only one child or no child
            if self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # Case 2: Node with two children
            # Get the inorder successor (smallest in the right subtree)
            temp = self.right.find_min()

            # Copy the inorder successor's content to this node
            self.val = temp.val

            # Delete the inorder successor
            self.right = self.right.delete(temp.val)

        return self

    def find_min(self):
        current = self
        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left
        return current


def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def print_ascii_tree(root, prefix="", is_left=True):
    if root is None:
        return

    if root.right is not None:
        print_ascii_tree(root.right, prefix + ("│   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))

    if root.left is not None:
        print_ascii_tree(root.left, prefix + ("    " if is_left else "│   "), True)


# Example usage:
if __name__ == "__main__":
    A = [7, 15, 9, 10, 13, 20, 2, 26, 23, 24, 28, 30]
    r = TreeNode(11)
    for element in A:
        r = insert(r, element)

    print("Initial tree:")
    print_ascii_tree(r)

    # Deleting nodes
    r = r.delete(11)
    r = r.delete(20)

    print("\nTree after deletion:")
    print_ascii_tree(r)
