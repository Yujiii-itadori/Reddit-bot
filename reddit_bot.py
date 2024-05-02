import praw
import creds



reddit_instance = praw.Reddit (
    client_id = creds.client_id,
    client_secret = creds.client_secret,
    username = creds.username,
    password = creds.password,
    user_agent = "test_bot"
)

print(reddit_instance.user.me()) 

#Getting submissions from posts
subreddit = reddit_instance.subreddit("ChatGPT")
print(subreddit)
top_25_submissions = subreddit.top(limit = 25, time_filter = "all")
for submission in top_25_submissions:
    print(submission.title)

#Submmiting the post
subreddit = reddit_instance.subreddit("testingground4bots")
subreddit.submit(title="Testing my bot", selftext="Hello, How are you?")

#Getting comments 
submission = reddit_instance.submission('1ci1vy8')
comments = submission.comments

#Filtering comments
for comment in comments:
    if "not" in comment.body:
        print(comment.body)

#Replying to comments 
for comment in comments:
    if "not" in comment.body:
        comment.reply("your comment contains not in the body  ")