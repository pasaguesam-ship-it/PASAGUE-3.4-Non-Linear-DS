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

## How to run

```
python binary_tree_traversal.py
python graph_traversal.py
```
