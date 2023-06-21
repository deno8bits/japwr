import japwr

r = japwr.Reddit('japwr:v0.0.0 (by /u/denobyte)')

posts = r.batchPosts(["14d6fb9", "14d6fbv"])

print(posts[0].score)
