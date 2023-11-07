## Engineering experience

1, What kinds of software projects have you worked on before? Which operating systems, development environments, languages, databases?  

Here are the projects and the tech stacks we used:  
* Shopee seller center, which is a platform for sellers where they can manage the products, orders, payment invoices, markting etc. at that time we use Ubuntu Linux and Mac as my development os, Python2.7 as the main language, MySQL as the data storage, Redis as the cache solution, ElasticSearch as the logging solution. we deployed the service on kubernates with Jekins as the CI/CD tool. 
* Domain compliance detect system for Tencent cloud, which is a service used for detect whether the domain in the web traffic meet the local goverment complicance requirements, if not should ban the traffic next time. It is developed by Python3.10 with asyncio, with MySQL as data storage, kafka as the message queue, Ubuntu 20.04 as the server envirenment. also used other internal tools for deployement, logging etc.
* Other kinds of web systems, the main goal is to help bussiness team do the work more effiently. Use Golang with GoFrame, MySQL as the storage, Redis as the cache etc. 
* A web system for Hunan YueYang local goverment which can scrape videos from cameras on fire-fighters in real time and cast it on the monitor. we use NodeJs with SailJs, Nginx with RTMP/RTSP, Embedded development on a camera linux with C as the language.

2, Give details of your Go software development experience to date, how would you rate your competency with Go?
* Been using Go as development language for about 4 years, mainly use it build services, internal framework tools. compared to Python's concurrency model, Go's GMP is much better.
* Familiar with Go, can use it develop all kinds of services. still digging the internals of the language, just like I did in Python.

3, How comprehensive would you say your knowledge of a Linux distribution is, from the kernel up? How familiar are you with low-level system architecture, runtimes and Linux distro packaging? How have you gained this knowledge?  
* There are many Linux distros, such as Ubuntu, Debian, Arch, etc, I have been using Ubuntu since college, which is 8.04 at that time. to summary, linux distros are kernels + gui + packaging + community, but some are well supported and have advantages than others. 
* I have benn trying to write drivers for fingerprints on my newly bought laptop which is not supported well on Linux.
* I gain these knowledge mainly from reading books(such as [Advanced Programming in the UNIX Environment] [Linux Device Drivers] etc), blogs, watching conference videos.

4, Outline your thoughts on quality in software development. What practices are most effective to drive improvements in quality? What ideals have been the hardest to achieve?  
There are many aspects of a good quality software development, here are the points I can remember right now
* A clean and simple archetecure/class design, follow the Unix KISS princeple
* A unified tech stack or framework which will reduce the differences introduced by developers
* Test driven development can be used to improve the quality
* Serious code review
* A deep understanding of the requirements and computer science
* Coding Style which can be done automatically

so the most effective is the TDD and simple archetecure/class design. Serious code review is hard, cuz many team workers are busy on their own tasks and won't pay much attention on the code review.

5, Outline your thoughts on documentation in large software projects. What practices should teams follow? What are great examples of open source docs? How have you approached documentation in your current projects?

There should be two kinds of docs, one is the design docs which is used to illustrate the design archetectures, contexts, etc, you can get most of the project knowledges in summary. the other is code/api doc, which can be used to detail every modification. with these two the developer can maintain the system with ease. also there should be user documentation, which will guide user how to use the software.

6, Elaborate on an engineering challenge that you solved and are most proud of.

Refactor the archetecture for traffic processing system in Tencent, to achieve following goals:
* High performance with multi-processing+asyncio+routines
* Reliability, redesigned class with documentation, remove internal c/c++ dependency with standard dependencies
* Mainability, can track every processed traffic from beginning to ending

## Context
1, Outline your thoughts on the state of the art in Linux based development experience. What are examples of tools with great dev experience and why? What is underrated? What is overrated?

I think it is way more better than development in Windows, but not the best compared to development in Mac. for example there are much more tools or software that make developer's life easier. but docker which based on Linux cgroups/namespaces are very convineint these days.

2, Describe your knowledge and experience with containerisation on Linux. How deeply have you delved in cgroups, namespaces and other container-oriented constructs? How well do you understand the underpinnings, design and differences between Docker, LXD, and snap containers?  

My experience on containerisation is mainly use it as server end deployment, we have been using docker&kubernates as the basic infrastructure. and use snap as the package manager installing apps on Ubuntu. I know that docker is based on Linux's cgroups and namespaces, but never implement a simple docker myself yet.

3, What improvements would you like to see in Ubuntu for developers?  
* IM tools for Ubuntu(some im don't have a Linux client, and this makes me feel not connected to the world when programming)
* Error messages when installing tools(maybe with containerisation this will a lot better)
* easy install some frequently used apps or tools

4, In what environments did you find yourself thriving as an engineer and why? What was detrimental to your performance?
* Ownership of the work I am doing will make me actively thinkinking about the project, thus find myself thriving as an engineer.
* Too much formalism and not solving real problems in work.

5, Why do you most want to work for Canonical?
I have been using Ubuntu linux since 


## Education
