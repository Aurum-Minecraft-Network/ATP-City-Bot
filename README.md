# Aurum Bot
This is the bot for use in the [Aurum Minecraft Network Discord Server](https://discord.aurumnet.ga).

## Runtime
This bot is run using Python 3.10.2.

## Environmental Variables
To run the bot, a few environmental variables have to be initialized. Most likely you have to create a file called `.env` at the root of this project.
An `.env` file should look like this: 

    TOKEN = yourTokenHere
    OWNER = yourDiscordUserIDHere
    ID = yourBotClientIDHere
    AWSKEY = yourAWSAccessKeyIDHere
    AWSSECRET = yourAWSSecretAccessKeyHere
    IMGURID = yourImgurAPIClientIDHere

Put your Discord Bot token (obtain one [here](https://www.writebots.com/discord-bot-token/)) in place of `yourTokenHere`.<br/>Put your own Discord user ID in place of `yourDiscordUserIDHere`.<br/>Put your Discord Bot's Client ID in place of `yourBotClientIDHere`.<br/>Put your AWS S3 Bucket's Access Key in place of `yourAWSAccessKeyIDHere`.<br/>Put your AWS Secret Access Key in place of `yourAWSSecretAccessKeyHere`.<br/>Put your Imgur API Client ID in place of `yourImgurAPIClientIDHere`.

## Install dependencies
Dependencies are listed in the `requirements.txt` file. Install them using pip with `pip install -r requirements.txt`.

## To run
Run the `main.py` file in any way you wish.

## Features
- A [DISBOARD](https://disboard.org) bump reminder
- An FAQ command
- Several fun commands including a command that gets the color of a user's default avatar
- Invite Manager module that tries to figure out who invited a new joined user, and what link did the new user use to join a server (unreliable)
  
## Compatibility
Most of the features are designed with only the Aurum Minecraft Network Discord Server in mind, and are server-specific.

## To Do
- Use pattern matching from Python 3.10 to improve runtime