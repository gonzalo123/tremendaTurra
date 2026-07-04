AUTHOR = "Gonzalo Ayuso"
SITENAME = "Tremenda Turra"
SITESUBTITLE = "Ensayos y reflexiones sin pies ni cabeza."
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output/"
THEME = "theme/el-canto"

TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "es"
DEFAULT_DATE_FORMAT = "%d/%m/%Y"

ARTICLE_PATHS = ["articles"]
PAGE_PATHS = ["pages"]
STATIC_PATHS = ["images"]

DEFAULT_CATEGORY = "Ensayos"
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

ARCHIVES_URL = "archivo/"
ARCHIVES_SAVE_AS = "archivo/index.html"
CATEGORIES_SAVE_AS = "categorias/index.html"
CATEGORY_URL = "categoria/{slug}/"
CATEGORY_SAVE_AS = "categoria/{slug}/index.html"
TAG_URL = "etiqueta/{slug}/"
TAG_SAVE_AS = "etiqueta/{slug}/index.html"
TAGS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
DIRECT_TEMPLATES = ["index", "archives", "categories"]

FEED_ATOM = "feeds/atom.xml"
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 45

DELETE_OUTPUT_DIRECTORY = True
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

MENUITEMS = (
    ("Archivo", "/archivo/"),
)
