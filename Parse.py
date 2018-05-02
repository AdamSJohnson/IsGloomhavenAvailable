from Keys import SECRET_KEY , CLIENT_KEY , USERNAME , API_KEY
from pushbullet.pushbullet import PushBullet
import praw
import time


# this function backups the do not notify list.
# Since we are just looping through new posts we don't
# need to keep the entire list 
def backup_list(backupthis=''):
    write = ''
    for line in backupthis:
        write = write + line + '\n'
    #open the file, write to it, close it
    file = open('CheckedAlready.txt', 'w')
    file.write(write)
    file.close()

#define a function that just keeps checking the new queue every 
#5 minutes and sends a notification if there is a new gloomhaven
#Post
def loop_through_posts(reddit='', push=''):
    #grab the device we want to push to
    devices = push.getDevices()
    #this may be different from user to user (This is my phone)
    phone = devices[1]["iden"]
    t = 60 * 5 # five minutes
    #get our alerted on list:
    check = open('CheckedAlready.txt', 'r')
    dontnotifylist = []
    for line in check:
        dontnotifylist.append(line.replace('\n',''))
    check.close()
    #get the subreddit instance
    subreddit = reddit.subreddit('boardgamedeals')
    push.pushNote(phone, 'RUNNING!', 'Running')
    old_list = []
    while True:
        print('Running!')
        new_list = subreddit.new(limit=15)
        if old_list == new_list:
            time.sleep(t) 
            continue

        for post in new_list:
            if(  'gloomhaven' in post.title.lower() ) and not post.id in dontnotifylist:
                #print(post.title)
                dontnotifylist.append(post.id)
                #send our notification
                push.pushNote(phone, 'GLOOMHAVEN ALERT', post.title)

        backup_list(backupthis=dontnotifylist)
        old_list = new_list
        time.sleep(t) 
        #back up the do not notify list
        #push.pushNote(phone, 'RUNNING!', 'Running')
        backup_list(backupthis=dontnotifylist)



def main():
    #setup our reddit instance
    reddit = praw.Reddit(client_id=CLIENT_KEY,
                         client_secret=SECRET_KEY,
                         user_agent=USERNAME)
    #setup our pushbullet instance
    push = PushBullet(API_KEY)

    loop_through_posts(reddit=reddit, push=push)

if __name__ == '__main__':
    main()