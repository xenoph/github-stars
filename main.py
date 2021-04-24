import sys
import os

from github import Github
from dotenv import load_dotenv

import stars

load_dotenv()

GITHUB_API = os.getenv('GITHUB_API')

g = Github(GITHUB_API)

user = g.get_user()
user.login

valid_first_arguments = ['all', 'list', 'lang']

if(sys.argv[1] not in valid_first_arguments):
    print("That's not a valid argument.")
    sys.exit()

if sys.argv[1] == 'list':
    if not len(sys.argv) > 2:
        print("You need to provide a language to list out.")
    else:
        stars.get_list_of_type(user, sys.argv[2])

if sys.argv[1] == 'all':
    if not len(sys.argv) > 2:
        stars.get_starred_list(user)
    elif sys.argv[2] == 'asc' or sys.argv[2] == 'desc':
        stars.get_starred_list(user, sys.argv[2])
    else:
        print("You need to provide 'asc' or 'desc' as an order argument")


if sys.argv[1] == 'lang':
    if not len(sys.argv) > 2:
        print('You have to pass a language.')
        sys.exit()

    stars.get_language_starred(user, sys.argv[2])
