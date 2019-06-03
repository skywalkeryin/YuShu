
from flask import Blueprint


# Set up static file folder, need to set up static_folder(in the bluePrint, web folder here is the beginning, here using the relative path),
# if you don't set up the static_url_path, it will use the tail
# of static_folder as the url.
# for example:  static_folder='test/statics' ,the url will be statics
# Only you set up the static_folder, then the static_url_path will take affect.

# web = Blueprint('web', __name__, static_folder='statics', static_url_path='/web/statics')


# BluePrint
web = Blueprint('web', __name__)


from app.web import book




