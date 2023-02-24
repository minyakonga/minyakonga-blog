Title: Reading Notes -- Philosophy of software design
Date: 2023-02-23 10:20
Modified: 2023-02-24 19:30
Category: ReadingNotes
Authors: minyakonga
Summary: ![Title](./images/douban-a-philosophy-of-software-design.jpg "Philosophy Of Software Design") The most fundamental problem in computer science is **problem decomposition: how to take a complex problem and divide it up into pieces that can be solved independently**. Problem decomposition is the central design task that programmers face every day......

![Title](./images/douban-a-philosophy-of-software-design.jpg "Philosophy Of Software Design")
《Philosophy Of Software Design》 tells you how to keep system simple in various ways. when we working on new features, always remember: keep the current system as simple as possible, even it sacrifice the delivery speed.

Like 《The Zen Of Python》, it is the guidelines for all programmers. due to all computer science problems are complexity decomposition problems, thus keep it(the system) simple is very import(Unix KISS). normally you can keep system simple by doing following: 
- Module should be deep
- Information hiding
- Different layer, different abstraction
- Pull complexity downwards
- Define errors out of existence
- Design it twice
- Comments and Documentations are very important
- Good naming
- Consitency

Strongly suggest you read the original book, there is much more details i can't write down here.

Bad comments and documentations, for example after read the new created framework docs, i still dont know how to use the components, need to analyze others code inorder to use it in our project.

Bad naming, many variable and method names are simplified Chinese Pinyin. like `BAXH`, maintainers dont know what is it means the first time.

Not so good system design, inorder to save us time, have a lot of dependencies which is developed by other teams. sounds great but works terrible. cuz always have dependency system problems which need programmers process at midnight.

Here is some quoates of the book:

> The overall goal is to reduce complexity.

> As a program evolves and acquires more features, it becomes complicated, with subtle dependencies between its components. Over time, complexity accumulates and it becomes harder and harder for programmers to keep all of the relevant factors in their minds as they modify the system. this slows down development and leads to bugs, which slow development even more and add to its cost. Complexity increases inevitably over the life of any program. the larger the program, and the more people that work on it, the more difficult it is to manage complexity.

> Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system.

> Complexity is more apparent to readers than writers.

> Change amplification: the first symptom of complexity is that a seemingly simple change requires code modifications in many different places.

> Cognitive load: the second symptom of complexity is cognitive load, which refers to how much a developer needs to know in order to complete a task. a higher cognitive load means that developers have to spend more time learning the required information, and there is a greater risk of bugs becuase they have missed something important.

> Unkown unkowns: the third symptom of complexity is that it is not obvious which pieces of code must be modified to complete a task, or what information a developer must have to carry out the task successfully.

> One of the most important goals of good design is for a system to be obvious. 

> By separating the interface of a module from its implementation, we can hide the complexity of the implementation from the rest of the system. users of a module need only understand the abstraction provided by its interface. the most import issue in designing classes and other modules is to make them deep, so that they have simple interfaces for the common use cases, yet still provide significant functionality.

> The word "somewhat" is important: dont get carried away and build something so general-purpose that it is difficult to use for your current needs.

> Software systems are composed in layers, where higher layers use the facilities provided by lower layers. if a system contains ajacent layers with similar abstractions, this is a red flag that suggests a problem with the class decomposition.

......