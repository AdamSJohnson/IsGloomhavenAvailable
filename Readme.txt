Usage:
Run this script in the background to have to check for posts about Gloomhaven on /r/boardgamedeals

Requirements:
PRAW and https://github.com/Azelphur/pyPushBullet

Setup:
Create a Keys.py file formatted as such:
SECRET_KEY = {Reddit application secret ID}
CLIENT_KEY = {Reddit application client ID}
USERNAME = {reddit username}
API_KEY = {Push bullet API Key}

You may need to change the device the notification is sent to. Good luck.
