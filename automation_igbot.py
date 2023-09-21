import sys
sys.path.append("intabot");
from instabot import Bot
from time import sleep


def follow(bot, followers, follow_count, amt):
    lower = follow_count
    count = 0
    for user in followers[lower:]:
        if count >= amt:
            return count
        username = bot.get_username_from_user_id(user)
        print("Following", username)
        if bot.follow(username):
            print("Followed", username)
            count += 1
        else:
            print("Not followed", username)
        sleep(5)
    return count

def unfollow(bot, amt):
    following = bot.get_user_following('')
    i = 0
    for user in reversed(following[:100]):
        username = bot.get_username_from_user_id(user)
        print("Unfollowing", username)
        if bot.unfollow(username):
            i += 1
            print("Unfollowed -", username)
        else:
            print("Not Unfollowed", username)
        if i >= amt:
            break
        sleep(5)
        
        return True;


def filter(bot, amt):
    f = open('followed.txt', 'r')
    following = f.read().splitlines()
    f.close()
    
    print(following)
    add_to_acc = []
    
    for user in reversed(following[-amt:]):
        username = bot.get_username_from_user_id(user)
        user_info = bot.get_user_info(user)
        bio = user_info['biography']
        name = user_info['full_name']
        followers = user_info['follow_count']
        following = user_info['following_count']
        
        if "rapper" in bio.lower() or "rapper" in name.lower() or "rapper" in username.lower():
            if 1000 < followers < 10000 and following / followers < 1.4:
                add_to_acc.append(username)
        sleep(5)
    
    return add_to_acc

bot = Bot(filter_users=False, max_following_to_followers_ratio=100, max_follower_to_following_ratio=100, follow_delay = 10, unfollow_delay = 10, max_followers_per_day = 1000, max_unfollow_per_day = 1000);

username = "your_username"
password = "your_password"

# Log in to your Instagram account
bot.login(username=username, password=password)

accounts = []
accounts.append("keyword")

amt = 150

for acc in accounts:
    followers = bot.get_user_followers(acc)
    follow_count = 1200
    
    while follow_count <= len(followers):
        follow_count += follow(bot, followers, follow_count, amt)
        sleep(3600)
        unfollow(bot, amt)
        sleep(3600)
        accounts.append(filter(bot, amt))
