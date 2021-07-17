le pagination:
    #     channelget = requests.get(
    #         f"https://api.twitch.tv/helix/videos?user_id={channel_id}&first=100&after={pagination}", headers=headers)

    #     response = channelget.json()

    #     videos = response["data"]
    #     pagination = response["pagination"]

    #     for video in videos:
    #         with open(f"{channel_name}vods.txt", 'w') as channelfile:
    #             print(video["title"], video["id"],
    #                   video["url"], file=