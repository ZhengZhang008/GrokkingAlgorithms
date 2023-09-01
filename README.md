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

- **Big O representation (大O表示法)**
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
- **Recursion (递归)**
: Recursion is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem.

- Pseudocode (伪代码)
: Pseudocode is a plain language description of the steps in an algorithm or another system. Pseudocode often uses structural conventions of a normal programming language, but is intended for human reading rather than machine reading.

- Base case (基线条件)
: The base case is a way to return without making a recursive call. In other words, it is the mechanism that stops this process of ever more recursive calls and an ever growing stack of function calls waiting on the return of other function calls.

- Recursive case (递归条件)
: The recursive case is input(s) for which the program recurs (calls itself).

- Call stack (调用栈)
: The call stack is used to keep track of multiple function calls. It is like a real stack in data structures where data can be pushed and popped and follows the Last In First Out (LIFO) principle. We use call stack for memorizing which function is running right now.

- **Stack (栈)**
: A stack is a collection of independent components that work together to support the execution of an application. The components, which may include an operating system, architectural layers, protocols, runtime environments, databases and function calls, are stacked one on top of each other in a hierarchy.

- Tail call (尾递归)
: Tail call is a subroutine call performed as the final action of a procedure. If the target of a tail is the same subroutine, the subroutine is said to be tail recursive, which is a special case of direct recursion.

## Chapter 4: Quick sort
- **Quick sort (快速排序)**
: QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

- Divide and conquer (分而治之)
: Divide and Conquer is a recursive problem-solving approach that breaks a problem into smaller subproblems, recursively solves the subproblems, and finally combines the solutions to the subproblems to solve the original problem.

- Pivot (基准值)
: A Pivot element refers to an element of a matrix that is selected by an algorithm to proceed with further calculations.

- Partitioning (分区)
: Partitioning is a method used for making a large code base or project manageable by breaking up different segments of it into smaller chunks that can be handled easily, as opposed to a large code that can have many areas of failure and take up large portions of a disk as well as take a very long time to compile.

- Proving by induction (归纳证明)
: The proof consists of two steps: The basis (base case): prove that the statement holds for the first natural number n. Usually, n = 0 or n = 1. The inductive step: prove that, if the statement holds for some natural number n, then the statement holds for n + 1.

- **Merge sort (合并排序)**
: Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.

- Worst Case (最糟情况)
: Worst case is the function which performs the maximum number of steps on input data of size n.

- Average Case (平均情况)
: Average case is the function which performs an average number of steps on input data of n elements.

## Chapter 5: Hashtable
- **Hash table (散列表)**
: A hash table, also known as a hash map, is a data structure that implements an associative array or dictionary. It is an abstract data type that maps keys to values.[2] A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored. 

- DNS resolution (DNS解析)
: DNS servers convert URLs and domain names into IP addresses that computers can understand and use. They translate what a user types into a browser into something the machine can use to find a webpage. This process of translation and lookup is called DNS resolution.

- Cache (缓存)
: In computing, a cache is a high-speed data storage layer which stores a subset of data, typically transient in nature, so that future requests for that data are served up faster than is possible by accessing the data's primary storage location.

- Collision (冲突)
: One occurs when two or more sets of data are modified and produce the same resulting value. The other is specific to networking and happens when two devices transmit data at the same time.

- Constant time (常量时间)
: An algorithm is said to be constant time (also written as time) if the value of (the complexity of the algorithm) is bounded by a value that does not depend on the size of the input.

- Resizing (调整长度)
: The RESIZE statement is used to adjust: the size of a dynamic variable (dynamic-clause), or. the number of occurrences of X-arrays (array-clause).

## Chapter 6: Breath-first search
- **Breath-first search (广度优先搜索)**
: Breadth-first search (BFS) is an algorithm for searching a tree data structure for a node that satisfies a given property. It starts at the tree root and explores all nodes at the present depth prior to moving on to the nodes at the next depth level.

- Graph theory (图算法)
: Graph theory is the study of graphs that is concerned with the relationship between edges and vertices.

- Shortest-path problem (最短路径问题)
: In graph theory, the shortest path problem is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized.

- Node (节点)
: A node is a basic unit of a data structure, such as a linked list or tree data structure. Nodes contain data and also may link to other nodes.

- Edge (边)
: Edges convey information about the links between the nodes.

- Queue (队列)
: A Queue is defined as a linear data structure that is open at both ends and the operations are performed in First In First Out (FIFO) order. We define a queue to be a list in which all additions to the list are made at one end, and all deletions from the list are made at the other end.

  | First In First Out (FIFO) | Last In First Out (LIFO) |
  |:---:|:---:|
  | Queue | Stack |

- Directed graph (有向图)
: A directed graph is defined as a type of graph where the edges have a direction associated with them.

- Undirected graph (无向图)
: An undirected graph is a type of graph where the edges have no specified direction assigned to them.

- Topological order (拓扑排序)
: A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

- Tree (树)
: A tree is a collection of nodes connected by directed (or undirected) edges. A tree is a nonlinear data structure, compared to arrays, linked lists, stacks and queues which are linear data structures.

## Chapter 7: Dijkstra's algorithm
- **Dijkstra's algorithm (迪科斯特拉算法)**
: Dijkstra's algorithm keeps track of the currently known shortest distance from each node to the source node and updates the value after it finds the optimal path once the algorithm finds the shortest path between the source node and destination node then the specific node is marked as visited.

- Weight (权重)
: A set of weighted inputs allows each artificial neuron or node in the system to produce related outputs.

- Weight graph (加权图)
: A weighted graph is defined as a special type of graph in which the edges are assigned some weights which represent cost, distance, and many other relative measuring units.

- Unweighted graph (非加权图)
: An unweighted graph is a graph in which the edges do not have weights or costs associated with them. Instead, they simply represent the presence of a connection between two vertices.

- Directed acyclic graph (有向无环图)
: A directed acyclic graph (DAG) is a graph that is directed and without cycles connecting the other edges. This means that it is impossible to traverse the entire graph starting at one edge. The edges of the directed graph only go one way.

- Parent node (父节点)
: Any sub-node of a given node is called a child node, and the given node, in turn, is the child's parent.

- Bellman-Ford algorithm (贝尔曼-福德算法)
: The Bellman-Ford algorithm emulates the shortest paths from a single source vertex to all other vertices in a weighted digraph. It is slower than Dijkstra's algorithm for the same problem but more versatile because it can handle graphs with some edge weights that are negative numbers.

## Chapter 8: Greedy algorithms
- **Greedy algorithms (贪婪算法)**
: A greedy algorithm is an algorithm that finds a solution to problems in the shortest time possible. It picks the path that seems optimal at the moment without regard for the overall optimization of the solution that would be formed.

- Power set (幂集)
: The power set is a set which includes all the subsets including the empty set and the original set itself. It is usually denoted by P. Power set is a type of sets, whose cardinality depends on the number of subsets formed for a given set.

- Approximation algorithm (近似算法)
: An Approximate Algorithm is a way of approaching NP-COMPLETENESS for the optimization problem. This technique does not guarantee the best solution. The goal of an approximation algorithm is to come as close as possible to the optimum value in a reasonable amount of time which is at the most polynomial time.

- Factorial function (阶乘函数)
: Factorial of a positive integer (number) is the sum of the multiplication of all the integers smaller than that positive integer.

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

