# Just Another Python Wrapper for Reddit

Python wrapper I use for personal projects. Use at your own risk.

Inspired by [PRAW](https://github.com/praw-dev/praw)

# Install

```
pip install git+https://github.com/deno8bits/japwr
```


# Usage

## Get daily top posts from r/all

```py
from japwr import Reddit

reddit = Reddit('SOME USERAGENT HERE')

posts = reddit.subreddit('all').top()
```

## Get a post

```py
from japwr import Reddit

reddit = Reddit('SOME USERAGENT HERE')

post = reddit.post('144f6xm')
```

## Get multiple posts

```py
from japwr import Reddit

reddit = Reddit('SOME USERAGENT HERE')

post = reddit.batchPosts(['144f6xm', '14nb5qs'])
```



# TODO
- [ ] Ability to read anything there is an endpoint for (if the user is allowed to)
- [ ] Ability to do basic stuff like creating posts and comments (if the user is allowed to)
- [ ] Ability to perform mod actions (if the user is allowed to)
