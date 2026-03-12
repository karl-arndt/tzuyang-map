import googleapiclient.discovery
import json

def set_youtube_api_key(api_key):
    global youtube_api_key, youtube
    youtube_api_key = api_key
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=youtube_api_key)

def get_youtube_channel_id(channel_handle):
    return youtube.channels().list(part="id", forHandle=channel_handle).execute()["items"][0]["id"]

def get_channel_data(channel_id):
    return youtube.channels().list(part="contentDetails", id=channel_id).execute()

def get_playlist_id(channel_id):
    channel_data = get_channel_data(channel_id)
    return channel_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

def get_all_videos_from_playlist(playlist_id):
    video_details = []
    page_token = None
    while True:
        playlist_items = youtube.playlistItems().list(part="snippet", playlistId=playlist_id, maxResults=50, pageToken=page_token).execute()
        for video in playlist_items["items"]:
            video_id = video["snippet"]["resourceId"]["videoId"]
            video_title = video["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_published_at = video["snippet"]["publishedAt"]
            video_details.append({
                "video_id": video_id,
                "video_title": video_title,
                "video_url": video_url,
                "video_published_at": video_published_at
            })
        page_token = playlist_items.get("nextPageToken")
        if not page_token:
            break
    return video_details

def get_all_videos_from_channel_handle(handle):
    channel_id = get_youtube_channel_id(handle)
    playlist_id = get_playlist_id(channel_id)
    return get_all_videos_from_playlist(playlist_id)

def get_all_videos_from_channel_id(channel_id):
    playlist_id = get_playlist_id(channel_id)
    return get_all_videos_from_playlist(playlist_id)

def dump_videos_to_json(video_details, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(video_details, f, ensure_ascii=False, indent=4)
