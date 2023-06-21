from datetime import datetime, timezone


class Post:
    """
        Post Object
    """

    # TODO: Check if there is a better way of mapping these vars
    # This will scale poorly
    def __init__(self, itemDict: dict, id: str = '', ) -> None:
        self.raw = itemDict  # Allow viewing the raw json

        self.item = item = itemDict['data']  # Wierd Mapping because the json is wierd

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
        self.removedBy: str | None = item['removed_by']
        self.authorFlairText: str | None = item['author_flair_text']
        self.suggestedSort: str | None = item['suggested_sort']
        self.selftextHTML: str | None = item['selftext_html']
        self.domain: str = item['domain']
        self.authorFlairType: str = item['author_flair_type']
        self.bannedBy: str | None = item['banned_by']
        self.removedByCategory: str | None = item['removed_by_category']
        self.linkFlairType: str = item['link_flair_type']
        self.modNote: str | None = item['mod_note']
        self.authorFlairCSSClass: str | None = item['author_flair_css_class']
        self.thumbnail: str = item['thumbnail']
        self.approvedBy: str | None = item['approved_by']
        self.linkFlairText: str | None = item['link_flair_text']
        self.category: str | None = item['category']
        self.secureMedia: str | None = item['secure_media']  # just a guess
        self.authorFlairTemplateID: str | None = item['author_flair_template_id']
        self.linkFlairTextColor: str = item['link_flair_text_color']
        self.name: str = item['name']
        self.subredditType: str = item['subreddit_type']
        self.subredditNamePrefixed: str = item['subreddit_name_prefixed']
        self.modReasonTitle: str | None = item['mod_reason_title']
        self.linkFlairCSSClass: str | None = item['link_flair_css_class']
        self.topAwardedType: str | None = item['top_awarded_type']
        self.authorFlairBackgroundColor: str | None = item['author_flair_background_color']
        self.postHint: str | None = self._getFluxVar('post_hint')

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
        self.visited: bool = item['visited']
        self.locked: bool = item['locked']
        self.spoiler: bool = item['spoiler']
        self.canGild: bool = item['can_gild']
        self.mediaOnly: bool = item['media_only']
        self.over18: bool = item['over_18']
        self.pinned: bool = item['pinned']
        self.isCrosspostable: bool = item['is_crosspostable']
        self.noFollow: bool = item['no_follow']
        self.archived: bool = item['archived']
        self.allowLiveComments = item['allow_live_comments']
        self.edited: bool = item['edited']
        self.authorPremium: bool = item['author_premium']
        self.isCreatedFromAdsUI: bool = item['is_created_from_ads_ui']
        self.canModPost: bool = item['can_mod_post']
        self.isMeta: bool = item['is_meta']
        self.isRedditMediaDomain: bool = item['is_reddit_media_domain']
        self.isOriginalContent: bool = item['is_original_content']
        self.clicked: bool = item['clicked']
        self.hidden: bool = item['hidden']
        self.quarantine: bool = item['quarantine']
        self.hideScore: bool = item['hide_score']

        # Then Ints
        self.score: int = item['score']
        self.numCrossposts: int = item['num_crossposts']
        self.subredditSubscribers: int = item['subreddit_subscribers']
        self.numComments: int = item['num_comments']
        self.numReports: int | None = item['num_reports']
        self.viewCount: int | None = item['view_count']
        self.likes: int | None = item['likes']  # Another guess IDK what this is
        self.wls: int = item['wls']  # Not sure what this is but it was an int when I saw its
        self.ups: int = item['ups']
        self.gilded: int = item['gilded']
        self.downs: int | None = item['downs']
        self.upvoteRatio: float = item['upvote_ratio']
        self.pwls: int = item['pwls']  # WTF is this there are so many vars that don't seem to mean shit
        self.totalAwardsReceived: int = item['total_awards_received']
        self.thumbnailHeight: int | None = item['thumbnail_height']
        self.thumbnailWidth: int | None = item['thumbnail_width']

        # Then Lists and dicts
        self.modReports: list = item['mod_reports']
        self.reportReasons: list | None = item['report_reasons']  # Not sure what this should be so I mapped it as a list
        self.treatmentTags: list = item['treatment_tags']  # ?? what is this
        self.awarders: list = item['awarders']
        self.allAwardings: list = item['all_awardings']
        self.contentCategories: list | None = item['content_categories']
        self.gildings: dict = item['gildings']
        self.secureMediaEmbed: dict = item['secure_media_embed']
        self.authorFlairRichtext: list = item['author_flair_richtext']
        self.userReports: list = item['user_reports']
        self.linkFlairRichtext: list = item['link_flair_richtext']
        self.mediaEmbed: dict = item['media_embed']
        self.preview: dict | None = self._getFluxVar('preview')

        # Then the rest
        self.media = item['media']  # TODO: Set Type
        self.createdUTC: datetime = datetime.fromtimestamp(item['created_utc'], tz=timezone.utc)
        self.created: datetime = datetime.fromtimestamp(item['created'])
        self.approvedAtUTC: datetime | None = datetime.fromtimestamp(item['approved_at_utc'], tz=timezone.utc) if item['approved_at_utc'] else None
        self.bannedAtUTC: datetime | None = datetime.fromtimestamp(item['banned_at_utc'], tz=timezone.utc) if item['banned_at_utc'] else None

    def __str__(self) -> str:
        return self.id

    def __repr__(self):
        return f'Post(id={self.id})'

    def _getFluxVar(self, varName: str):
        """Gets Variables that might not always be present

        Args:
            varName (str): The name of the variable to get
        Returns:
            Any | None: Return the variable if found else returns None
        """
        try:
            var = self.item[varName]
        except KeyError:
            var = None

        return var
