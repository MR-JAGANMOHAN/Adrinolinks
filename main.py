import telebot

import requests

# Initialize the bot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# Define the URL of your API

API_URL = "https://adrinolinks.in/st?api=813a8f143fa948cc4c187a94421e0b75b86eeb32"

# Define the function to shorten a link using your API

def shorten_link_with_api(link):

    # Make a request to your API

    response = requests.get(API_URL, params={"url": link})

    # Check if the request was successful

    if response.status_code == 200:

        # Get the shortened link from the response

        shortened_link = response.json()["shortened_url"]

        return shortened_link

    else:

        # Raise an error if the request was not successful

        raise Exception("Error shortening link: {}".format(response.status_code))

# Replace the code to shorten a link with the code to shorten a link using your API

shorten_link = shorten_link_with_api

# Define a function to convert a post containing several links to Adrino links

def convert_post(post):

    # Get the links from the post

    links = post.text.split(" ")

    # Shorten each link

    shortened_links = []

    for link in links:

        shortened_links.append(shorten_link(link))

    # Replace the links in the post with their shortened versions

    new_post = ""

    for link, shortened_link in zip(links, shortened_links):

        new_post += shortened_link + " "

    return new_post

# Define a handler for the /convert command

@bot.command("/convert")

def convert(message):

    # Get the post from the message

    post = message.text

    # Convert the post to Adrino links

    new_post = convert_post(post)

    # Send the new post back to the user

    bot.send_message(message.chat.id, new_post)

# Define a handler for the bot starting event

@bot.on_startup

def startup():

    # Send a welcome message to the user

    bot.send_message("Hi! I am Adrino Links Shortener. I can shorten any link you send me.")

# Start the bot

#bot.polling()

if __name__ == "__main__":

    # Deploy the bot to Render

    import render

    render.deploy(bot)

