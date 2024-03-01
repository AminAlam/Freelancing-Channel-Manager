# Freelancing Channel Manager Telegram Bot </br></br>
Using this bot, you can manage a telegram freelancing channel automaticly.
The bot offers useful features for both clients and admin.</br> </br>

## Installation

Install the required dependencies using pip as indicated in the following line:
```console
amin@Maximus$ pip3 install requirements.txt
```

After installing the dependencies, please change the content of config.py. Set the `ADMIN_PASSWORD` field, and send it to the bot vai the admin user. The telegram user who sends this string to the bot will be the admin of the bot, and will receive the ads to either accept or reject them.

## Usage:
Change the following parameters in the `configs.py`:
- `BOT_API`: The token of the telegram bot (Get one from Telegram Bot Father)
- `MAIN_CHANNEL`: The telegram name of the channel (The channel should be public)
- `SUPPORT_USER`: The telegram username of the support user
- `BOT_ID`: The telegram ID of the Bot
- `ADMIN_PASSWORD`: If a user sends this password to the bot, the admin control panel of the bot will be activated for the user