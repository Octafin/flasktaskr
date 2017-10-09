import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'b"+\x8a\x81\xcf\x92\xd7?\xbc_\xc4\x96!\x14\x13~\x94HuJ\x05\xc5\xbeJ\xe1\xecz\x8f\x0c\x85[\xeeV\xa5\xa7\x86'

# defin the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)
