import praw
from mdutils.mdutils import MdUtils


reddit = praw.Reddit(
    client_id="",
    client_secret="",
    username="",
    password="",
    user_agent="redditcoronav1",
)
subreddit = reddit.subreddit("Coronavirus")
submission = reddit.submission(id="fgy7rg")
submission.comments.replace_more(limit=0)
all_comments = submission.comments
found = 0
mdFile = MdUtils(file_name="test", title="Reddit ama corona virus")
for comment in all_comments:
    if len(comment.replies) > 0:
        for reply in comment.replies:
            if reply.author == "Emergencydocs":
                found = 1
                print(20 * "=")
                print("QUESTION: ")
                mdFile.new_header(level=1, title=comment.body)
                print(comment.body)
                print("ANSWER: ")
                mdFile.new_paragraph(reply.body)
                print(reply.body)
            else:
                continue

mdFile.create_md_file()


# hot_python = subreddit.hot()
# for submission in hot_python:
#     # check for removing pinned posts...
#     if not submission.stickied:
#         print(
#             "Title: {}, ups:{}, downs:{}, Have We visited: {}".format(
#                 submission.title, submission.ups, submission.downs, submission.visited
#             )
#         )
#         submission.comments.replace_more(limit=0)
#         comments = submission.comments.list()
#         # for comment in comments:
#         #     print(20 * "-")
#         #     # print(comment.author, "+", comment.body)
#         #     print("Parent Id:", comment.parent())
#         #     print("Comment Id:", comment.id)
#         #     # if len(comment.replies) > 0:
#         #     #     for reply in comment.replies:
#         #     #         print("REPLY: ", reply.body)
