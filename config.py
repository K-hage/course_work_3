from os import path


parent_dir = path.dirname(path.abspath(__file__))
POST_DATA = path.join(parent_dir, 'data', 'data.json')
COMMENTS_DATA = path.join(parent_dir, 'data', 'comments.json')
BOOKMARKS_DATA = path.join(parent_dir, 'data', 'bookmarks.json')
LOG_PATH = path.join(parent_dir, 'log', 'api.log')
