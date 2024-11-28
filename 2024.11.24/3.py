def tree_leaves(tree_branches):
    count = 0
    for element in tree_branches:
        if type(element) is list:
            count += tree_leaves(element)
        elif element == 'leaf':
            count += 1
    return count

# >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
# >>> tree_leaves(tree)
# 38
