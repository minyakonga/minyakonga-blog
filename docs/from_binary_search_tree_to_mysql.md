## Background
The other day I saw an online coding interview on youtube, the task is to find the in-order successor of a given node in the binary search tree. each time when I want to interview need re-learn this knowledge, after I successfully found the job will forget this knowledge sooner or later. here I want to make myself understand the internal details of tree data structure and the applications. 

* what is a binary search tree?
* how to create it?
* how to traverse it?
* how to search it?
* how to find in order/preorder the successor of a given node?
* what is a balanced tree?
* what is a red-black tree?
* what is B+ tree?
* are there any applications in Python?
* how MySQL use trees?

### what is a binary search tree?

![bst_1.png](images/bst_1.png)

1, all left children are less than the current node  
2, all right children are bigger than current node  
3, each child itself is a binary tree  
4, there is no duplicate node  

### how to create a binary search tree?
give the following numbers, need to create a binary search tree `1, 3, 4, 6, 7, 8, 10, 13, 14`.

{{ snippet('git@github.com:mprivat/mkdocs-snippet-plugin.git', 'README.md', '## Installation') }}

## References
[coding interview Bloomberg part 1](https://www.youtube.com/results?search_query=coding+interview+bloomberg+part+1)
