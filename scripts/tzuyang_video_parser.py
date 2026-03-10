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

main_channel_data = youtube.channels().list(part="contentDetails", id=tzuyang_main_id).execute()
main_uploads_playlist_id = main_channel_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

page_token = None

while True: 
    main_videos_raw = youtube.playlistItems().list(part="snippet", playlistId=main_uploads_playlist_id, maxResults=50, pageToken=page_token).execute()
    main_videos = main_videos_raw["items"]
    for video in main_videos:
        video_id = video["snippet"]["resourceId"]["videoId"]
        video_title = video["snippet"]["title"]
        print(f"{video_id}: {video_title}")
    page_token = main_videos_raw.get("nextPageToken")
    if not page_token:
        break