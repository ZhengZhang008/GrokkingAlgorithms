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

## Chapter 6: Breath first search
