from datetime import datetime, timezone


class Post:
    """
        Post Object
    """

    # TODO: Check if there is a better way of mapping these vars
    # This will scale poorly
    def __init__(self, itemDict: dict, id: str = '', ) -> None:
        self.raw = itemDict  # Allow viewing the raw json

        item = itemDict['data']  # Wierd Mapping because the json is wierd

        # Manually Mapping vars
        # Strings first
        self.subreddit: str = item['subreddit']
        self.title: str = item['title']
        self.url: str = item['url']
        self.id: str = item['id']
        self.selftext: str = item['selftext']
        self.authorFullname: str = item['author_fullname']
        self.parentWhitelistStatus: str = item['parent_whitelist_status']
        self.whitelistStatus: str = item['whitelist_status']
        self.permalink: str = item['permalink']
        self.authorFlairTextColor: str | None = item['author_flair_text_color']  # IDK what this is supposed to be so I just mapped it as str
        self.discussionType: str | None = item['discussion_type']
        self.author: str = item['author']
        self.linkFlairBackgroundColor: str = item['link_flair_background_color']
        self.removalReason: str | None = item['removal_reason']
        self.modReasonBy: str | None = item['mod_reason_by']
        self.subredditID: str = item['subreddit_id']

        # Then Bools
        self.isVideo: bool = item['is_video']
        self.isSelf: bool = item['is_self']
        self.saved: bool = item['saved']
        self.stickied: bool = item['stickied']
        self.authorPatreonFlair: bool = item['author_patreon_flair']
        self.contestMode: bool = item['contest_mode']
        self.sendReplies: bool = item['send_replies']
        self.isRobotIndexable: bool = item['is_robot_indexable']
        self.authorIsBlocked: bool = item['author_is_blocked']
        self.distinguished: bool | None = item['distinguished']  # wtf why is this None

        # Then Ints
        self.score: int = item['score']
        self.numCrossposts: int = item['num_crossposts']
        self.subredditSubscribers: int = item['subreddit_subscribers']
        self.numComments: int = item['num_comments']

        # Then Lists and dicts
        self.modReports: list = item['mod_reports']
        self.reportReasons: list | None = item['report_reasons']  # Not sure what this should be so I mapped it as a list

        # Then the rest
        self.media = item['media']  # TODO: Set Type
        self.createdUTC: datetime = datetime.fromtimestamp(item['created_utc'], tz=timezone.utc)
        self.approvedAtUTC: datetime | None = datetime.fromtimestamp(item['approved_at_utc'], tz=timezone.utc) if item['approved_at_utc'] else None

    def __str__(self) -> str:
        return self.id

    def __repr__(self):
        return f'Post(id={self.id})'
