# pip install pydelicious
from pydelicious import DeliciousAPI
from getpass import getpass

# logon to delicious
account = DeliciousAPI('igniteflow', getpass('Password:'))

# get a dictionary of all posts
posts = account.posts_all()['posts']

# inspect your data
for post in posts:
	print post['description'], post['tag'], post['href']