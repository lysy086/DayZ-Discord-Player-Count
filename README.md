# DayZ-Discord-Player-Count

![image](https://github.com/lysy086/DayZ-Discord-Player-Count/assets/32988227/287d8e53-373d-449c-8bed-3f4352733fb2)

Discord Bot with Dynamic Status
This Python script demonstrates how to create a Discord bot using the discord.py library, which updates its status dynamically based on data fetched from an external API. In this example, the bot fetches information about a game server from the BattleMetrics API and displays the current number of players and maximum player count as its status on Discord.

Requirements
Python 3.x
discord.py
requests
Setup
Install Python 3.x from the official website.

Install the required libraries by running the following command:

Copy code
pip install discord requests
Create a Discord bot and obtain its token. Refer to the Discord Developer Portal for more information.

Replace "TOKEN" in the code with your bot's token.

Run the script using Python:

Copy code
python bot.py
Description
The script fetches data from the BattleMetrics API using the requests library.
It defines a function update_status() that continuously updates the bot's status with the current player count and maximum player count from the API response.
The status is updated every 5 seconds.
The bot's presence is set to idle to reflect that it is not actively responding to commands.
Usage
Once the bot is running and connected to your Discord server, it will display its status as "Playing [players count] / [max players count]".
You can customize the bot's prefix or add additional functionality by modifying the PREFIX variable or implementing new commands using the discord.py framework.
Disclaimer
This script is intended for educational purposes only. Use it responsibly and respect Discord's terms of service and API usage policies.
