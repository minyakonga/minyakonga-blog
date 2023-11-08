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