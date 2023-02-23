AUTHOR = 'minyakonga'
SITENAME = '夏嘉莫察瓦绒'
SITESUBTITLE = '余生北国，虽闻飞鱼之名，竟不知其为何物...'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/minyakonga'),
    ('github', 'https://github.com/csrgxtu'),
    ('email', 'minyakonga@gmail.com')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'themes/Peli-Kiera'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'neighbors']

STATIC_PATHS = ['images', 'extras']
EXTRA_PATH_METADATA = {
    'extras/favicon.ico': {'path': 'favicon.ico'},  # and this
}

DISQUS_SITENAME = ''
