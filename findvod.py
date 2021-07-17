import os
import json
from dotenv import load_dotenv

load_dotenv()

channel_name = os.getenv('channel_name')

vidDict = {}
with open(f"{channel_name}vods.txt", 'r') as channelfile:
    vidDict = json.load(channelfile)

searchTerm = input("What video are you searching for?")

for vid_id in vidDict:
    if searchTerm in vidDict[vid_id][1]:
        print(vidDict[vid_id][1], vidDict[vid_id][0])
