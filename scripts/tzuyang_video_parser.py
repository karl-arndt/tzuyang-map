from dotenv import load_dotenv
import os
import googleapiclient.discovery

load_dotenv()

youtube_api_key = os.getenv("YOUTUBE_API_KEY")
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=youtube_api_key)

tzuyang_main_channel_name = "@tzuyang6145"
tzuyang_vlog_channel_name = "@v-tzuyang"

tzuyang_main_id = youtube.channels().list(part="id", forHandle=tzuyang_main_channel_name).execute()["items"][0]["id"]
tzuyang_vlog_id = youtube.channels().list(part="id", forHandle=tzuyang_vlog_channel_name).execute()["items"][0]["id"]

print(tzuyang_main_id)
print(tzuyang_vlog_id)

main_videos = youtube.search().list(part="id", channelId=tzuyang_main_id, maxResults=50, type="video").execute()
print(main_videos)