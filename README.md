# Reddit Bot with PRAW

This repository contains a basic Reddit bot implemented using the [PRAW](https://praw.readthedocs.io/en/stable/) library. The bot can retrieve posts and comments, submit new posts, and reply to comments based on specified conditions.

## Features
- Fetches top posts from a specified subreddit.
- Submits a new post to a specific subreddit.
- Retrieves comments from a specific post.
- Replies to comments based on predefined criteria.

## Requirements
- Python 3.6+
- `praw` library

## 1. Create a Reddit application to obtain the necessary credentials.**
Go to Reddit App Preferences.
Click on "Create App" or "Create Another App".
Select "script".
Fill in the necessary details and set a redirect URI (e.g., http://localhost:8000).
Save the client ID, client secret, and other details.

## 2.Create a creds.py file in the same directory as your bot script.

- client_id = "your_client_id"
- client_secret = "your_client_secret"
- username = "your_reddit_username"
- password = "your_reddit_password"

## 3. Ensure your bot script imports the creds module to access these credentials.

## Usage
- The bot connects to Reddit using your provided credentials.
- It fetches the top 25 posts from the "ChatGPT" subreddit and prints their titles.
- It submits a new post to the "testingground4bots" subreddit.
- It retrieves comments from a specific post and replies to comments containing the word "not".
##Disclaimer
Use this bot responsibly and in accordance with Reddit's API Terms of Use.
Ensure you have permission to run bots on specific subreddits, and avoid spamming or violating community rules.

