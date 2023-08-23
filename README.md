# Study note on Grokking Algorithms
The intention behind creating this study note is to provide a convenient reference for the key concepts within this book. This resource aims to facilitate cross-referencing of information between Chinese and English, while also offering succinct explanations for each of the important knowledge points.

The original book ["Grokking Algorithms"](https://www.manning.com/books/grokking-algorithms), [《算法图解》](https://github.com/ZhengZhang008/GrokkingAlgorithms/blob/master/%E7%AE%97%E6%B3%95%E5%9B%BE%E8%A7%A3.pdf).

The sample code at GitHub [Grokking Algorithms Sample Code](https://github.com/egonschiele/grokking_algorithms).

## Chapter 1: Introduction to Algorithms
- Binary Search (二分查找)
: Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item until you've narrowed down the possible locations to just one.

- Linear Search (简单查找)
: Linear search is a very simple search algorithm. A sequential search is made over all items one by one. Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data collection.

- Bucket (桶)
: You can treat a bucket as an element of an array, as a cell, or as a space where something can live.

- Linear time (线性时间)
: In linear time algorithms every single element in the input is visited once. As the input size grows our algorithm's run time grows exactly with the size of the input.

- Logarithmic time (对数时间)
: A logarithmic algorithm splits a list or other data structure into smaller pieces every time it runs.

- Factorial time (阶乘时间)
: An algorithm is said to have a factorial time complexity when it grows in a factorial way based on the size of the input data.

- Big O representation (大O表示法)
: We use big-O notation to asymptotically bound the growth of a running time to within constant factors above and below.

  | Big O representation | Common algorithms |
  |:---:|:---:|
  | O(log *n*) | Binary Search |
  | O(*n*) | Simple Search |
  | O(*n* * log *n*) | Quick Search |
  | O(*n^2*) | Selection Search |
  | O(*n*!) | Travel Agent |

## Chapter 2: Selection Sorting
- Array (数组)
: An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together.

- Linked list (链表)
: A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in the form of a pointer.

- Index (索引)
: Indexing refers to the process of accessing a specific element in a sequence, such as a string or a list, using its position or index number.

  | | Array | Linked list |
  |:---:|:---:|:---:|
  | Read | O(1) | O(*n*) |
  | Insert | O(*n*) | O(1) |

- Random access (随机访问)
: Random access files permit nonsequential, or random, access to a file's contents. 

- Sequential access (顺序访问)
: In sequential access, you access the File data from the beginning of the File to the end of the File.

- Selection sort (选择排序)
： Selection sort is a sorting algorithm that sorts an array by repeatedly finding the minimum element and putting them in ascending order. 

## Chapter 3: Recursion
- Recursion (递归)
： Recursion is the process of defining something in terms of itself.

- Pseudocode (伪代码)
： Pseudocode is more like an algorithmic representation of the code involved.

- Base case (基线条件)
: The base case is the condition to stop the recursion.

- Recursive case (递归条件)
: The recursive case is the part where the function calls on itself.

- Call stack (调用栈)
： When a function is called in Python, a new frame is pushed onto the call stack for its local execution, and every time a function call returns, its frame is popped off the call stack.

- Stack (栈)
: A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.

## Chapter 4: Quick sort
- Divide and conquer (分而治之)
: The problem in hand, is divided into smaller sub-problems and then each problem is solved independently. When we keep on dividing the subproblems into even smaller sub-problems, we may eventually reach a stage where no more division is possible.

- Pivot (基准值)
: Pivot is used to reshape a given data frame organized by given index/column values.

- Partitioning (分区)
: The partition searches for a specified string, and splits the string into a tuple containing three elements. 

- Merge sort (合并排序)
: Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.

- Worst Case (最坏情况)
: In the worst case, we calculate the upper bound on the running time of an algorithm.

- Average Case (平均情况)
: In average case, we take all possible inputs and calculate the computing time for all of the inputs.

## Chapter 5: Hashtable
- Hash table (散列表)
: Hash Table in Python utilizes an array as a medium of storage and uses the hash method to create an index where an element is to be searched from or needs to be inserted. 

- DNS resolution (DNS解析)
: The IP addresses when translated to human readable formats or words become known as domain names.

- Cache (缓存)
: Cache is a temporary space from which data can be read or written at a very high speed, as compared to a database or a web service.

- Collision (冲突)
: Collision is a python library that is meant for collision detection between convex and concave polygons, circles, and points.

- Constant time (常量时间)
: Independently of the input data size, it will always have the same running time since it only gets the first value from the list.

- Resizing (调整长度)
: The resize triggers the resize event or attaches a function to run when a resize event occurs.

## Chapter 6: Breath-first search
- Breath-first search (广度优先搜索)
: Breadth-First Search is a recursive algorithm to search all the vertices of a graph or a tree.

- Shortest-path problem (最短路径问题)
: The shortest path problem is one of finding how to traverse a graph from one specified node to another at minimum cost.

- Node (节点)
: A Node is a data structure that stores a value that can be of any data type and has a pointer to another node.

- Edge (边)
: An edge (or link) of a network (or graph) is one of the connections between the nodes (or vertices) of the network.

- Queue (队列)
: Queue is a linear data structure with a rear and a front end, similar to a stack.

- Directed graph (有向图)
: In directed graphs, the connections between nodes have a direction and are called arcs.

- Undirected graph (无向图)
: In undirected graphs, the connections have no direction and are called edges.

- Topological order (拓扑排序)
: A topological order is a linear ordering of the vertices in a graph such that for every directed edge u -> v from vertex u to vertex v, vertex u comes before vertex v in the ordering.

- Tree (树)
: Tree represents the nodes connected by edges. It is a non-linear data structure.

## Chapter 7: Dijkstra's algorithm
- Dijkstra's algorithm (迪科斯特拉算法)
: Dijkstra's algorithm is an iterative algorithm that provides us with the shortest path from one particular starting node (a in our case) to all other nodes in the graph.

- Weight (权重)
: Weights is an optional parameter which is used to weigh the possibility for each value.

- Weight graph (加权图)
: If edges in your graph have weights then your graph is said to be a weighted graph.

- Unweighted graph (非加权图)
: If the edges do not have weights, the graph is said to be unweighted.

- Directed acyclic graph (有向无环图)
: A directed acyclic graph is a graph which doesn't contain a cycle and has directed edges.

- Parent node(父节点)
: Any sub node of a given node is called a child node, and the given node, in turn, is the child's parent.

- Bellman-Ford algorithm (贝尔曼-福德算法)
: Bellman-Ford algorithm is used to find the shortest path from the source vertex to every vertex in a weighted graph.

## Chapter 8: Greedy algorithms
- power set (幂集)
- Approximation algorithm (近似算法)
- ()
- ()
- ()
- ()
- ()
