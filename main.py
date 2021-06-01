import os
import discord
import requests

# for local environment
from dotenv import load_dotenv
load_dotenv()

# get environment variables
DISCORD_BOT_ACCESS_TOKEN = os.environ["DISCORD_BOT_ACCESS_TOKEN"]
LINE_NOTIFY_ACCESS_TOKEN = os.environ["LINE_NOTIFY_ACCESS_TOKEN"]
VOICE_CHANNEL_ID = os.environ["VOICE_CHANNEL_ID"]

LINE_NOTIFY_API_URL = "https://notify-api.line.me/api/notify"
HEADERS = {"Authorization": "Bearer " + LINE_NOTIFY_ACCESS_TOKEN}

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after):
    # This function is called when not only member join to the voice channel,
    # but also member changed their status to mute.
    # So, it is necessary to catch only events that joining channel.
    if before.channel != after.channel:
        if after.channel is not None and after.channel.id == int(VOICE_CHANNEL_ID):
            message = {
                "message": "\n" + member.name + "・イン・ザ・ディスコード"
            }
            requests.post(LINE_NOTIFY_API_URL, headers=HEADERS, data=message)
 
client.run(DISCORD_BOT_ACCESS_TOKEN)