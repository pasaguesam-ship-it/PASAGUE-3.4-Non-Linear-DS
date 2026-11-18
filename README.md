# Assessment 3.4: Non-Linear Data Structure

**Name:** Samantha Leonor B. Pasague  
**Section:** BSIT 3B  
**Surname used:** PASAGUE

## Program 1: Binary Tree (`binary_tree_traversal.py`)

```
              P            level 0
            /   \
           A     S         level 1
          / \   / \
         A   G U   E       level 2
```

Output:

```
Binary Tree Traversal (PASAGUE)
BFS: P - A - S - A - G - U - E
DFS: P - A - A - G - S - U - E
```

## Program 2: Graph (`graph_traversal.py`)

```
                 P                 level 0
              /  |  \
             A   S---G             level 1
             |   |   |
             A---U   E             level 2
```

Edges: P-A, P-S, P-G, S-G, A-A, S-U, G-E, A-U

Output:

```
Graph Traversal (PASAGUE)
BFS: P - A - S - G - A - U - E
DFS: P - A - A - U - S - G - E
```

## Program 3: DFS Methods in Tree (`dfs_methods_tree.py`)

Name used: SAMANTHA PASAGUE

```
                    P                          level 0
             /            \
            M               A                  level 1
         /     \         /     \
        A       T       U       H              level 2
       / \     / \     / \     / \
      S   E   A   A   A   N   S   G            level 3
```

Output:

```
DFS Methods in Tree (SAMANTHA PASAGUE)
Preorder: P - M - A - S - E - T - A - A - A - U - A - N - H - S - G
Inorder: S - A - E - M - A - T - A - P - A - U - N - A - S - H - G
Postorder: S - E - A - A - A - T - M - A - N - U - S - G - H - A - P
```

## How to run

```
python binary_tree_traversal.py
python graph_traversal.py
python dfs_methods_tree.py
```
