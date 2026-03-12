import youtube_video_parser
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    tzuyang_main_channel_name = "@tzuyang6145"
    tzuyang_vlog_channel_name = "@v-tzuyang"
    youtube_api_key = os.getenv("YOUTUBE_API_KEY")
    youtube_video_parser.set_youtube_api_key(youtube_api_key)
    youtube_video_parser.dump_videos_to_json(
        youtube_video_parser.get_all_videos_from_channel_handle(tzuyang_main_channel_name),
        "data/tzuyang_main_videos.json"
    )
    youtube_video_parser.dump_videos_to_json(
        youtube_video_parser.get_all_videos_from_channel_handle(tzuyang_vlog_channel_name),
        "data/tzuyang_vlog_videos.json"
    )

if __name__ == "__main__":
    main()