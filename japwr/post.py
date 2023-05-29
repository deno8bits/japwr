class Post:
    # TODO: Check if there is a better way of mapping these vars
    # This will scale poorly
    def __init__(self, item: dict) -> None:
        item = item['data']
        self.isVideo: str = item['is_video']
        self.title: str = item['title']
        self.score: int = item['score']
