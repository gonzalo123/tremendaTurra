import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401,F403

SITEURL = os.environ.get("SITEURL", "")
RELATIVE_URLS = not bool(SITEURL)

DELETE_OUTPUT_DIRECTORY = True
