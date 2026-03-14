import cv2
import yt_dlp
import easyocr
import re

def scan_video(video_url):
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        stream_url = info['url']

    cap = cv2.VideoCapture(stream_url)
    reader = easyocr.Reader(['ko','en'], gpu=False)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    interval = int(fps * 2)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % interval != 0:
            continue

        results = reader.readtext(frame)

        for bbox, text, prob in results:
            if re.search(r'(서울|부산|대구|인천|경기|도로|로|길|Street|Drive|Avenue|Lane|Way|Las Vegas)', text):
                if (prob < 0.5):
                    continue
                print(f"Found restaurant-related text: {text}")

                pts = bbox
                for i in range(4):
                    cv2.line(frame, tuple(pts[i]), tuple(pts[(i + 1) % 4]), (0, 255, 0), 2)
                cv2.imshow(f"Frame: {frame_count}, Probability: {prob}", frame)
                print("Q to Quit, C to Continue, Space to Approve:")
                cv2.waitKey(0)
                if input().lower() == 'q':
                    exit(0)
                if input().lower() == 'c':
                    print(f"Continuing: {text}")
                if input().lower() == ' ':
                    print(f"Approved: {text}")
                if input() == '':
                    continue
                cv2.destroyAllWindows()
    cap.release()

def test_scan_video():
    video_url = "https://www.youtube.com/watch?v=RSZVP4M1bQ0"
    scan_video(video_url)

test_scan_video()