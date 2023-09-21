from instabot import Bot

# Create a bot instance
bot = Bot()

# Replace "Ijoshuabot" and "2joshuabot99" with your actual Instagram username and password
username = ""
password = ""

# Log in to your Instagram account
bot.login(username=username, password=password)

# Get user information for the logged-in user
user_info = bot.get_user_info(bot.user_id)

# Print the biography of the logged-in user
print(user_info['biography'])

# Replace "target_user" with the username of the user you want to get information about
target_username = "target_user"
user_id = bot.get_user_id_from_username(target_username)

# Check if the user_id is valid (not None)
if user_id is not None:
    # Get user information using the obtained user_id
    user_info = bot.get_user_info(user_id)
    print(user_info)
else:
    print("Invalid username or user not found.")
