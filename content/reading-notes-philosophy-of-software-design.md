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
- Comment are very important
- Good naming
- Consitency
