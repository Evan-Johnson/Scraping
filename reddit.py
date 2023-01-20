import praw
import csv

def get_Top_5(sub):
    reddit = praw.Reddit(client_id='XXXXXX', client_secret='XXXXX', user_agent='XXXXXX')

    subreddit = reddit.subreddit(sub)

    top_posts = subreddit.hot(limit=5)

    for post in top_posts:
        print(post.title)
        print(post.url)
        print('author: ' + post.author.name)
        print('upvotes: ' + str(post.ups))
        print('comments: ' + str(post.num_comments))
        print('top comment info:')
        print('author: ' + post.comments._comments[1].author.name)
        print('upvotes: ' + str(post.comments._comments[1].ups))
        print('body: ' + post.comments._comments[1].body)
        
        print()

get_Top_5('anarchychess')