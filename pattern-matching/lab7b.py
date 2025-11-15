def empty_tree_fn():
    return 0


def leaf_fn(key):
    return key**2


def inner_node_fn(key, left_value, right_value):
    return key + left_value


def traverse(search_tree, inner_node_fn, leaf_fn, empty_tree_fn):
    """Search a tree."""

    if not search_tree:                     # If branch is empty
        return empty_tree_fn()

    elif isinstance(search_tree, int):      # If branch is a leaf
        leaf = search_tree
        return leaf_fn(leaf)

    elif len(search_tree) == 3:             # If branch is a subtree
        left_branch, key, right_branch = search_tree
        left_value = traverse(left_branch, inner_node_fn,
                              leaf_fn, empty_tree_fn)
        right_value = traverse(right_branch, inner_node_fn,
                               leaf_fn, empty_tree_fn)

        return inner_node_fn(key, left_value, right_value)


def contains_key(compare_value, search_tree):
    """Check if a tree contains a inputted value."""

    def empty_tree_fn():
        return False

    def leaf_fn(key):
        return key == compare_value

    def inner_node_fn(key, left_value, right_value):
        return key == compare_value or left_value or right_value

    return traverse(search_tree, inner_node_fn, leaf_fn, empty_tree_fn)


def tree_size(search_tree):
    """Check the amount of inner nodes and leafs in a tree."""

    def empty_tree_fn():
        return 0

    def leaf_fn(key):
        return 1

    def inner_node_fn(key, left_value, right_value):
        return 1 + left_value + right_value

    return traverse(search_tree, inner_node_fn, leaf_fn, empty_tree_fn)


def tree_depth(search_tree):
    """Check the depth of a tree."""

    def empty_tree_fn():
        return 0

    def leaf_fn(key):
        return 1

    def inner_node_fn(key, left_value, right_value):

        if right_value > left_value:
            return right_value + 1
        else:
            return left_value + 1
    
    return traverse(search_tree, inner_node_fn, leaf_fn, empty_tree_fn)


# Test uppgift 1
print("Test uppgift 1")
print(traverse([3, 2, 5], inner_node_fn, leaf_fn, empty_tree_fn))  # Test a normal case, Expect 11
print(traverse([[[], 10, []], 7, 8], inner_node_fn, leaf_fn, empty_tree_fn))  # Test with empty list, Expect 17


# Test uppgift 2
print("Test uppgift 2")
print(contains_key(5, [[10, 11, [5, 6, 8]], 7, 8]))  # Test a key in tree, Expect True
print(contains_key(77, [[10, 11, [5, 6, 8]], 7, 8]))  # Test a key not in tree, Expect False
print(contains_key(4, [3, 5, [[], 2, 4]]))  # Test if a leaf is empty, Expect True


# Test uppgift 3
print("Test uppgift 3")
print(tree_size([3, 4, [2, 24, 7]]))  # Test normal case, Expect 5
print(tree_size([[], 6, [3, 4, [[], 5, []]]]))  # Test with empty leafs, Expect 4
print(tree_size([]))  # Test a case with no tree, Expect 0


# Test uppgift 4
print("Test uppgift 4")
print(tree_depth([1, 5, [10, 7, [[], 8, 9]]]))  # Test a normal case, Expect 4
print(tree_depth([]))  # Test a case with no tree, Expect 0
