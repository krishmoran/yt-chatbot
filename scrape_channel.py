from youtube_transcript_api import YouTubeTranscriptApi
import googleapiclient.discovery

# Initialize the YouTube API
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="AIzaSyDwqDrmGmJOe-XD1KEw3GqXbbaaYiAhi8I")

# Get the channel ID for the YouTube channel
channel_id = "CHANNEL_ID"

# Get the list of all video IDs from the channel
request = youtube.search().list(
    part="snippet",
    channelId=channel_id,
    maxResults=50,  # Change as needed
    type="video"
)
response = request.execute()

video_ids = [item['id']['videoId'] for item in response['items']]

# For each video, download the transcript and combine
all_transcripts = ""
for video_id in video_ids:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        all_transcripts += " ".join([t['text'] for t in transcript])
    except:
        print(f"An error occurred for video: {video_id}")

# Now `all_transcripts` contains the combined transcripts of all videos
print(all_transcripts)
