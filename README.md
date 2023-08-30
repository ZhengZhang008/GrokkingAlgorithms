# Study note on Grokking Algorithms
The intention behind creating this study note is to provide a convenient reference for the key concepts within this book. This resource aims to facilitate cross-referencing of information between Chinese and English, while also offering succinct explanations for each of the important knowledge points.

The original book ["Grokking Algorithms"](https://www.manning.com/books/grokking-algorithms), [《算法图解》](https://github.com/ZhengZhang008/GrokkingAlgorithms/blob/master/%E7%AE%97%E6%B3%95%E5%9B%BE%E8%A7%A3.pdf).

The sample code at GitHub [Grokking Algorithms Sample Code](https://github.com/egonschiele/grokking_algorithms).

## Chapter 1: Introduction to Algorithms
- **Binary Search (二分查找)**
: Binary search is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array.

- **Linear Search (简单查找)**
: Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found, otherwise, the search continues till the end of the data set.

- Bucket (桶)
: You can treat a bucket as an element of an array, a cell, or a space where something can live.

- Linear time (线性时间) - O(*n*)
: The running time increases most linearly with the size of the input.

- Logarithmic time (对数时间) - O(log *n*)
: When the algorithm runtime increases very slowly compared to an increase in input size i.e. logarithm of input size.

- Factorial time (阶乘时间)
: The time it takes to run an algorithm is directly proportional to the factorial of the input size.

- Big O representation (大O表示法)
: Big O notation characterizes functions according to their growth rates: different functions with the same asymptotic growth rate may be represented using the same O notation. The letter O is used because the growth rate of a function is also referred to as the **order of the function**.

  | Big O representation | Common algorithms |
  |:---:|:---:|
  | O(log *n*) | Binary Search |
  | O(*n*) | Simple Search |
  | O(*n* * log *n*) | Quick Search |
  | O(*n^2*) | Selection Search |
  | O(*n*!) | Travel Agent |

## Chapter 2: Selection Sorting
- **Array (数组)**
: An array is a data structure, which can store a fixed-size collection of elements of the same data type. An array is used to store a collection of data, but it is often more useful to think of an array as a collection of variables of the same type.

- **Linked list (链表)**
: A linked list is a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes that together represent a sequence.

- Index (索引)
: An index is sorting data by creating keywords or a list with pointers to where further information about the keyword is found.

  | | Array | Linked list |
  |:---:|:---:|:---:|
  | Read | O(1) | O(*n*) |
  | Insert | O(*n*) | O(1) |
  | Delete | O(*n*) | O(1) |

- Random access (随机访问)
: Random access is the ability to access an arbitrary element of a sequence in equal time or any datum from a population of addressable elements roughly as easily and efficiently as any other, no matter how many elements may be in the set. 

- Sequential access (顺序访问)
: Sequential access is a term describing a group of elements (such as data in a memory array or a disk file or on magnetic-tape data storage) being accessed in a predetermined, ordered sequence.

- **Selection sort (选择排序)**
: Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

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
- Quick sort (快速排序)
:  A sorting algorithm that sorts an array using a divide-and-conquer strategy

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
: In the average case, we take all possible inputs and calculate the computing time for all of the inputs.

## Chapter 5: Hashtable
- Hash table (散列表)
: Hash Table in Python utilizes an array as a medium of storage and uses the hash method to create an index where an element is to be searched from or needs to be inserted. 

- DNS resolution (DNS解析)
: The IP addresses when translated to human readable formats or words become known as domain names.

- Cache (缓存)
: Cache is a temporary space from which data can be read or written at a very high speed, as compared to a database or a web service.

- Collision (冲突)
: Collision is a Python library that is meant for collision detection between convex and concave polygons, circles, and points.

- Constant time (常量时间)
: Independently of the input data size, it will always have the same running time since it only gets the first value from the list.

- Resizing (调整长度)
: The resize triggers the resize event or attaches a function to run when a resize event occurs.

## Chapter 6: Breath-first search
- Breath-first search (广度优先搜索)
: Breadth-first search is a recursive algorithm to search all the vertices of a graph or a tree.

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
: Dijkstra's algorithm is an iterative algorithm that provides us with the shortest path from one particular starting node (in our case) to all other nodes in the graph.

- Weight (权重)
: Weights is an optional parameter which is used to weigh the possibility for each value.

- Weight graph (加权图)
: If edges in your graph have weights then your graph is said to be a weighted graph.

- Unweighted graph (非加权图)
: If the edges do not have weights, the graph is said to be unweighted.

- Directed acyclic graph (有向无环图)
: A directed acyclic graph is a graph that doesn't contain a cycle and has directed edges.

- Parent node(父节点)
: Any sub-node of a given node is called a child node, and the given node, in turn, is the child's parent.

- Bellman-Ford algorithm (贝尔曼-福德算法)
: Bellman-Ford algorithm is used to find the shortest path from the source vertex to every vertex in a weighted graph.

## Chapter 8: Greedy algorithms
- Greedy algorithms (贪婪算法)
: Greedy algorithms are suitable for problems that have certain properties, such as optimal substructure and greedy choice.

- Power set (幂集)
: The power set of a set S is the set of all subsets of S.

- Approximation algorithm (近似算法)
: An approximation algorithm is a way of dealing with NP-completeness for an optimization problem.

- Factorial function (阶乘函数)
: The number is multiplied with all the integers that lie between 1 and the number itself.

## Chapter 9: Dynamic programming
- Dynamic programming (动态规划)
: Dynamic programming is most important to optimize the solutions to the problem in comparison to the recursive approach.

- Feynman algorithm (费曼算法)
: 1. Write down the problem. 2. Think really hard. 3. Write down the solution.

- Levenshtein distance (编辑距离)
: The Levenshtein distance is a text similarity measure that compares two words and returns a numeric value representing the distance between them.

## Chapter 10: KNN
- K-nearest neighbours (K最近邻)
: K-nearest neighbour basically creates an imaginary boundary to classify the data.

- Normalization (归一化)
: Normalization is the process of organizing data in a database.

- Regression (回归)
: Regression refers to the process of a project regressing, or returning to a previous state.

- Cosine similarity (余弦相似度)
: Cosine similarity is a measure of similarity, often used to measure document similarity in text analysis.

- Naive Bayes classifier (朴素贝叶斯分类器)
: Naive Bayes classifier is successfully used in various applications such as spam filtering, text classification, sentiment analysis, and recommender systems.

## Chapter 11: The next step
- Binary search tree (二叉查找树)
:

- (B树)
:

- (红黑树)
:

- (伸展树)
:

- Inverted index (反向索引)
:

- (傅里叶变换)
:

- (并行算法)
:

- (分布式算法)
:

- (布隆过滤器)
:

- Secure hash algorithm (安全散列算法)
:

- Diffie-Hellman algorithm ()
:

- (线性规划)
:

