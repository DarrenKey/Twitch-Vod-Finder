import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

channel_name = "northernlion"

temp_client_id = os.getenv('temp_client_id')

client_id = os.getenv('client_id')

oauth_token = os.getenv('oauth')


# get channel id
def getId(channel_name, client_id, oauth_token) -> str:

    headers = {"Authorization": f"Bearer {oauth_token}",
               "Client-ID": client_id}

    channelgetid = requests.get(
        f"https://api.twitch.tv/helix/users?login={channel_name}", headers=headers)

    response = channelgetid.json()

    return response["data"][0]["id"]


# get all videos from channel
def getVideos(channel_id, client_id, oauth_token, channel_name):
    headers = {"Authorization": f"Bearer {oauth_token}",
               "Client-Id": client_id}

    channelget = requests.get(
        f"https://api.twitch.tv/helix/videos?user_id={channel_id}&first=100", headers=headers)

    response = channelget.json()

    videos = response["data"]
    pagination = response["pagination"]

    # json dict - id: (url, title)
    jsonDict = {}

    for video in videos:
        jsonDict[video["id"]] = (video["url"], video["title"])

    while "cursor" in pagination:
        cursor = pagination["cursor"]
        channelget = requests.get(
            f"https://api.twitch.tv/helix/videos?user_id={channel_id}&first=100&after={cursor}", headers=headers)

        response = channelget.json()

        videos = response["data"]
        pagination = response["pagination"]

        for video in videos:
            jsonDict[video["id"]] = (video["url"], video["title"])

    with open(f"{channel_name}vods.txt", 'w') as channelfile:
        json.dump(jsonDict, channelfile)


channel_id = getId(channel_name, temp_client_id, oauth_token)
videos = getVideos(channel_id, temp_client_id, oauth_token, channel_name)
