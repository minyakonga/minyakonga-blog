Title: Pelican static site generator tutorial
Date: 2023-04-26 16:00
Category: tool
Authors: minyakonga
Summary: I am Pythonista, thus wired still using Node Hexo as a static site generator. and due to the lost source code of csrgxtu.github.io, decided to migrate to Pelican as my blog static site generator. this post is used to record some key steps to use Pelican in my new blog site minyakonga.github.io.

I am Pythonista, thus wired still using Node Hexo as a static site generator. and due to the lost source code of csrgxtu.github.io, decided to migrate to Pelican as my blog static site generator. this post is used to record some key steps to use Pelican in my new blog site minyakonga.github.io.

1st, prepare the Python environment
```bash
pyenv virtualenv 3.11.2 minyakonga-blog
```

2nd, install dependency packages
```bash
python -m pip install "pelican[markdown]"
python -m pip install pelican-readtime
python -m pip install pelican-neighbors
```

3rd, write a post in markdown and save it into `content` dir
```bash
.
├── Makefile
├── __pycache__
│   └── pelicanconf.cpython-311.pyc
├── content
│   ├── extras
│   │   └── favicon.ico
│   ├── images
│   │   └── douban-a-philosophy-of-software-design.jpg
│   ├── pelican-static-site-generator-tutorial.md
│   └── reading-notes-philosophy-of-software-design.md
...
```

4th, start the local dev server and check the rendered page on your browser
```bash
pelican --autoreload --listen  # http://localhost:8000
```

5th, generate static content
```bash
git clone git@github.com:minyakonga/minyakonga.github.io.git  # clone this static repo into current project root

pelican content -o minyakonga.github.io -s pelicanconf.py  # generate static into minyakonga.github.io
```

6th, commit the newly created file changed into GitHub
```bash
ga *
gcmsg "add post: ****"
gp
```

7th, access `minyakonga.github.io` and check again

8th, commit the blog source code
```bash

```