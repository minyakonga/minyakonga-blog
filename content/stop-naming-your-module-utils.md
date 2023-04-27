Title: Stop Naming your modules utils
Date: 2023-04-27 10:00
Category: Python
Authors: minyakonga
Summary: There is a software developer that is either adding new code or refactoring existing one by extracting a class/function. they have to place code somewhere, but it does not seem to fit anywhere, so what does a developer do? they create a new module ---- utils.

看到这篇文章的时候，内心是崩溃的，里面说的bad practice我们目前项目中都有，一个不落。就像写出了非Pythonic的代码，它没有validate Python Grammer，可以正常工作，但就是维护起来费劲。所以说在正确的前提下，我们要尽量在工程中做到这些Best Pracice说到的东西。

总结原文就是我们会在某些情况下将一些通用的或者无法归类的逻辑放在诸如：`util`, `common`等模块中  
- 单个无法归类的function放入util中
- 多个模块公用的就放在了common中

然后后续的programmer因为这个会继续向util中添加很多逻辑，久而久之其变的更加多元化，不确定。当你看到这个模块的时候，你无法确定其具体实现了什么功能，在其它项目模块需要使用util or common中的方法的时候需要将其整体引入的项目中，增加了代码复杂度。

总而言之，根据Python的哲学：Explicit is better than implicit，我们应该保持项目的简介清晰，尽量避免一些模棱两可的东西。

下面是原文：
Imagine the following situation: there is a software developer that is either adding new code or refactoring existing one by extracting a class/function. They have to place the code somewhere, but it does not seem to fit anywhere. So what does a developer do? They create a new module – utils.py.

### Why utils is a terrible name?
Utils is arguably one of the worst names for a module because it is very blurry and imprecise. Such a name does not say what is the purpose of code inside. On the contrary, a utils module can as well contain almost anything. By naming a module utils, a software developer lays down perfect conditions for an incohesive code blob. Since the module name does not hint team members if something fits there or not, it is likely that unrelated code will eventually appear there, as more utils. More on it later.

Synonyms of utils, like helpers, commons, etc. are bad for the same reason.

### Why do people do this?
#### Excuse I – it is just one function
Initially, yes – it may be just one function. One function in a badly named module is not that wrong, isn’t it?

It is. Similarly to the broken windows theory, one occurrence of misbehaviour invites more of them. One function or class in utils is a small problem, indeed. Hence, it should be refactored when it is easy. Once the utils module grows, it will require a lot more effort to split it. And surprise, surprise, no one will be willing to do that.

How bad it can get? Once, in one Python repository, I saw there were several utils.py modules. My favourite contained 13 various functions and one utility class. What were these functions doing? Everything, from validation to data normalization to saving to the database to sending HTTP requests to getting current datetime formatted accordingly to the format parameter (Yes, separate, loose functions).

```Python
def send_post_request(url, data, logger):
    ...

def save_details(source_obj, override_data_from_source_obj: dict = None):
    ...

def normalize_address(address: str) -> str:
    ...

```
That’s how programming hell looks like. utils.py quickly becomes a whirlpool for all code that does not fit other places. It smoothly leads us to excuse number 2…

#### Excuse II – There is no other place to put this code
Indeed, there may be no place that a new class/function fits. Reaction to create a new place for the code is good. However, a programmer needs to put more effort when thinking about the name. As we know, taking the easiest road with utils is a slippery slope.

We can do better by naming module by the purpose of functions living inside. If they will be creating other objects, let’s name it factories.py. If their role is validation – go for validators.py. Maybe we need a few functions that operate on phone numbers? See if they could not be a regular, stateful class PhoneNumber and just put it in a separate file – phone_number.py.

A special case – functions with business logic. There are many techniques for that, some of them are more sophisticated than others (e.g. the Clean Architecture) but let’s consider a simple case. Assuming we have Django + DRF web application that contains business logic in serializers. We slowly migrate our API to version 2 and we need to put business logic extracted from V1 serializer in some other place, so that serializer V2 may reuse that. DO NOT PUT THIS IN utils.py. Try putting business logic in services.py module. Name service comes from an application service – a single thing that the application does for the clients. If this was, for example, booking a flight, a service could be named flight_booking_service and would:

- authorize payment on customer’s payment card
- reserve a flight using 3rd party provider
- send an email (or scheduled a Celery task to do so)

#### Excuse III I need a place for company commons
Let’s say you are building a distributed application and there are chunks of code that needs to be reused in a majority or all microservices. It is a natural reaction to put them together in someplace, like a separate repository to be installed as a package. But please don’t call it {company_name}-utils. I heard about a case of such a repository, but luckily for its maintainers, it was not that big. It contains code responsible for:  

- secrets handling, using public cloud services
- logging configuration that uses specific public services

As I said, it’s not that bad but it would be nice if they were more specific with the name, for example, cloud-toolkit or split that into two separate repositories/packages because frankly there are microservices that use only one of functionalities.

#### Excuse IIII – But Django does that
Yes, there is a couple of utils packages in Django. Shame on them for using utils name. However, notice that at least some of them could be separated from the framework and bundled as optional dependencies. Also, at least they are grouped in cohesive sub-packages – e.g. `django.utils.timezone` or `django.utils.translation`.

Unless you are writing a framework, stay away from utils. 😉

### Are all utils bad?
Not exactly. Eventually, one may need a couple of auxiliary functions. In that case, organize such code in modules named by theme – like datetimes, phone_numbers, etc. Such functions should be pure (in terms of functional programming).

Pure Functions – do not have side effects, that is, they do not change the state of the program. Given the same input, a pure function will always produce the same output.

[https://stackabuse.com/functional-programming-in-python/](https://stackabuse.com/functional-programming-in-python/)

### Summary
Do not use utils as a name for your Python module neither put it into a class name. Try to be more specific about the role of code – e.g. create a place for validators, services or factories. If the role criterion doesn’t help and you really dealing with utils, try grouping code by its theme –

utils modules are dangerous because they deteriorate over time. Each and another person that adds something that does not fit anywhere will happily add it to the utils module, increasing its incohesion. The disorder will grow over time, becoming greater and greater burden to work with.

If you see a newly created utils module in a code review, request it to be renamed. If you are tempted to add something to existing utils, create a new place for your code and move there everything from utils that fits a newly created module.

In the end, you will exercise your brain to become better at designing code.

### Reference
[Stop naming your python module 'utils'](https://breadcrumbscollector.tech/stop-naming-your-python-modules-utils/)  
[Util package are evil](http://www.adam-bien.com/roller/abien/entry/util_packages_are_evil)
  