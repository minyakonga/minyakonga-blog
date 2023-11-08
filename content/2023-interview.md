## 九坤工程师面试题目
1， 2个多选，9个填空，1个编程
编程：任务之间有依赖，找到任务的执行顺序。（未成功做出，实际需要用图论的知识）

## 仕锦源 系统架构师
1， HR 面，并准备了如下题目
    1、目前薪资及接下来对薪资的要求。
    2、SAAS系统架构设计应该如何做，是否方便先画出架构图。
    3、项目如何实现高并发？
    4、 数据库高并发造成死锁如何解决？
    5、如何保障服务器网络安全。

## 富途牛牛的面试准备
output of following code:
```Golang
package main

func main() {
 fmt.Println(test1())
 fmt.Println(test2())
 fmt.Println(test3())
 fmt.Println(test4())

 return
}

func test1() (v int) {
 defer fmt.Println(v)
 return v
}

func test2() (v int) {
 defer func() {
  fmt.Println(v)
 }()
 return 3
}

func test3() (v int) {
 defer fmt.Println(v)
 v = 3
 return 4
}

func test4() (v int) {
 defer func(n int) {
  fmt.Println(n)
 }(v)
 return 5
}
```

slice vs array
array are sequential memory address, which can be indexed, slice is a pointer to the orginal array.

一面一个半小时，变成题目
```Python
原升序数组[]int{1,3,5,7,9}，将数组所有元素向右移动n=3个单位后得到[]int{5,7,9,1,3}。
要求设计一种算法，根据偏移后的数组求n。
例子1:
输入：[]int{5,7,9,1,3}，输出：3
例子2:
输入：[]int{5,1,2,3,4}，输出：1

#coding=utf-8
import sys 
from typing import List

# 1, 3, 5, 7, 9
# 5, 7, 9, 1, 3

# 1, 2, 3, 4, 5
# 5, 1, 2, 3, 4

def get_offset(lst: List[int]) -> int:
    """ get offset ..."""
    offset, origin_list = 0, sorted(lst)

    for idx in range(len(lst)):
        if lst[0] == origin_list[idx]:
            print(f'Debug: matched {idx}')
            offset = 5 - idx
            break

    return offset

if __name__ == '__main__':
#     offset = get_offset([5, 7, 9, 1, 3])
    offset = get_offset([5, 1, 2, 3, 4])
    print(offset)

```