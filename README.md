# DS Python – Lab, Practical & Unit Code

Python programs for SPPU SE Computer (2024 Pattern) **Data Structures** (PCC-201-COM) and **Data Structures Laboratory** (PCC-204-COM). Every file is self-contained and runs with `python3 file.py`.

## Copy-paste quickly
Open **[ALL_CODE.md](ALL_CODE.md)**: every program on one page, practicals first.

All 30 programs were run and checked with Python 3 (Nov 2026).

## Practical exam programs (`practicals/`)

| Code | File | Program | Chits |
|---|---|---|---|
| GA1 | `GA1_library_borrowing.py` | Library borrowing: average, highest/lowest, zero borrows, mode, complexity | 1, 2, 3, 4, 5, 19 |
| GA2 | `GA2_customer_search.py` | Customer IDs: linear + binary search (iterative and recursive) | 1, 6, 18 |
| GA3 | `GA3_salary_sort.py` | Salaries: selection + bubble sort, top 5 | 2, 7, 17 |
| GB4 | `GB4_undo_redo_stack.py` | Text editor undo/redo with two stacks | 3, 8, 16, 20 |
| GB5 | `GB5_event_queue.py` | Event processing queue: add, process, display, cancel | 4, 9, 15, 20 |
| GB6 | `GB6_student_linked_list.py` | Student records in a linked list: add, delete, update, search, sort asc/desc | 5, 10, 14, 19 |
| GC7 | `GC7_hash_chaining.py` | Hash table size 10, division method, chaining | 6, 10, 13, 18 |
| GC8 | `GC8_hash_linear_probing.py` | Fixed-size hash table, division method, linear probing | 7, 12, 17 |
| GD9 | `GD9_graph_bfs_dfs.py` | City graph: DFS on adjacency matrix, BFS on adjacency list | 8, 11, 16 |
| GD10 | `GD10_bst.py` | BST: insert, delete, search, display | 9, 11, 12, 13, 14, 15 |

## Basics and syllabus units

| Folder | File | What it covers |
|---|---|---|
| 00-basics | `python_basics.py` | Input patterns, lists, 2D lists, dicts, functions, recursion, classes, menu skeleton |
| unit1-complexity | `complexity_step_count.py` | Step count, O(log n) / O(n) / O(n²) / O(n³) |
| | `divide_conquer_product_sort.py` | Case study: e-commerce product sorting (merge sort) |
| | `greedy_calendar.py` | Case study: calendar scheduling (greedy activity selection) |
| unit2-arrays-search-sort | `arrays_matrices.py` | Array ADT, address formulas, matrix add/multiply/transpose, sparse matrix, social network matrix |
| | `searching.py` | Linear, sentinel, binary, Fibonacci, indexed sequential |
| | `sorting.py` | Bubble, selection, insertion, quick, merge with passes |
| unit3-stack-queue-linkedlist | `stack_expressions.py` | Stack, two stacks in one array, infix → postfix/prefix, postfix evaluation |
| | `queues.py` | Linear, circular, priority queue |
| | `call_center_queue.py` | **Lab B3** – call center queue |
| | `linked_lists.py` | Singly (all primitive ops), doubly, circular |
| | `stack_queue_using_linked_list.py` | Case study: stack and queue on a linked list |
| unit4-hashing | `extendible_hashing.py` | **Lab C3** – extendible hashing |
| | `dictionary_hash.py` | Case study: dictionary with chaining and rehashing |
| unit5-graphs-trees | `mst_and_shortest_path.py` | **Lab D2** – Prim, Kruskal, Dijkstra (pizza delivery / GPS) |
| | `binary_tree_traversals.py` | Recursive + non-recursive traversals, height, leaves, mirror |
| | `expression_tree.py` | **Lab D4** – expression tree from prefix, non-recursive postorder, delete |
| | `city_population_bst.py` | **Lab D5** – city BST, asc/desc, max comparisons |
| | `propositional_formula_tree.py` | **Lab D6** – formula → binary tree |
| | `huffman_coding.py` | Case study: Huffman compression |

The earlier OOPCG Java code is kept under the git tag `oopcg-java`.
