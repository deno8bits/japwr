from .post import Post
from typing import Literal

sortTypes = Literal['best', 'hot', 'now', 'random', 'rising', 'top', 'controversial']
timeTypes = Literal['hour', 'day', 'week', 'month', 'year', 'all']


class ListingBase:
    """
    Base class for anything that generates what the API refers to as listings

    ref: https://www.reddit.com/dev/api#section_listings
    """
    def getPosts(
            self,
            sort: sortTypes,
            timeFrame: timeTypes = 'day',
            limit: int = 25,
            before: str = None,
            after: str = None,
            count: int = 0) -> list[Post]:
        """
        Used to get post from a specified place
        """
        url = f'{self.urlBase}/{sort}'

        req = self.connHandler.get(url, t=timeFrame, limit=limit, before=before, after=after, count=count)

        return [Post(itemDict=item) for item in req['data']['children']]

    def best(
            self,
            timeFrame: timeTypes = 'day',
            limit: int = 25,
            before: str = None,
            after: str = None,
            count: int = 0) -> list[Post]:
        """
        Alias for getPosts
        """

        return self.getPosts('best', timeFrame, limit, before, after, count)

    def hot(
            self,
            timeFrame: timeTypes = 'day',
            limit: int = 25,
            before: str = None,
            after: str = None,
            count: int = 0) -> list[Post]:

        return self.getPosts('hot', timeFrame, limit, before, after, count)

    def new(
            self,
            timeFrame: timeTypes = 'day',
            limit: int = 25,
            before: str = None,
            after: str = None,
            count: int = 0) -> list[Post]:

        return self.getPosts('new', timeFrame, limit, before, after, count)

    def random(
            self,
            timeFrame: timeTypes = 'day',
            limit: int = 25,
            before: str = None,
            after: str = None,
            count: int = 0) -> list[Post]:

        return self.getPosts('random', timeFrame, limit, before, after, count)

    def rising(
            self,
            timeFrame: timeTypes = 'day',
            limit: int = 25,
            before: str = None,
            after: str = None,
            count: int = 0) -> list[Post]:

        return self.getPosts('rising', timeFrame, limit, before, after, count)

    def top(
            self,
            timeFrame: timeTypes = 'day',
            limit: int = 25,
            before: str = None,
            after: str = None,
            count: int = 0) -> list[Post]:

        return self.getPosts('top', timeFrame, limit, before, after, count)

    def controversial(
            self,
            timeFrame: timeTypes = 'day',
            limit: int = 25,
            before: str = None,
            after: str = None,
            count: int = 0) -> list[Post]:

        return self.getPosts('controversial', timeFrame, limit, before, after, count)
