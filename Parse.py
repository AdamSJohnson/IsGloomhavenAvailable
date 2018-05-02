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

check = open('CheckedAlready.txt', 'r')
dontnotifylist = []
for line in check:
    dontnotifylist.append(line.replace('\n',''))
check.close()
print(dontnotifylist)
subreddit = reddit.subreddit('boardgamedeals')
for post in subreddit.new(limit=25):
    if(  'gloomhaven' in post.title.lower() ) and not post.id in dontnotifylist:
        print(post.title)
        dontnotifylist.append(post.id)

write = ''
for line in dontnotifylist:
    write = write + line + '\n'
open('CheckedAlready.txt', 'w').write(write)