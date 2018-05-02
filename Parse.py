from Keys import SECRET_KEY , CLIENT_KEY , USERNAME , API_KEY
from pushbullet.pushbullet import PushBullet
import praw

#setup our reddit instance
reddit = praw.Reddit(client_id=CLIENT_KEY,
                     client_secret=SECRET_KEY,
                     user_agent=USERNAME)
push = PushBullet(API_KEY)
devices = push.getDevices()
phone = devices[1]["iden"]



check = []
subreddit = reddit.subreddit('boardgamedeals')
for post in subreddit.new(limit=25):
    if(  'gloomhaven' in post.title.lower() ) and not post.id in check:
        print(post.title)
        check.append(post.id)
