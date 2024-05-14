# -*- coding: utf-8 -*-

import os
import json
import pandas as pd
import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "XXX"  # Replace with your actual developer key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    video_id = "q8q3OFFfY6c"
    comments = retrieve_video_comments(youtube, video_id)
    
    if comments:
        save_comments_to_csv(comments, "youtube_comments.csv")
        print("Comments data saved to 'youtube_comments.csv'")

def retrieve_video_comments(youtube, video_id):
    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=video_id,
            maxResults=100,  # Max results per page (default is 20, max is 100)
            pageToken=next_page_token if next_page_token else ""
        )
        response = request.execute()

        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]
            author = comment["authorDisplayName"]
            comment_text = comment["textDisplay"]
            publish_time = comment["publishedAt"]
            comments.append({"author": author, "comment": comment_text, "published_at": publish_time})

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break  # No more pages

    print(f"Retrieved {len(comments)} comments.")
    return comments

def save_comments_to_csv(comments, filename):
    df = pd.DataFrame(comments)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    main()
