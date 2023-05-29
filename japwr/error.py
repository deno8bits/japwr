class Unauthorized(Exception):
    def __init__(self, *args, **kwargs):
        msg = 'Your not allowed to view this. Did you authorize your Reddit Instance?'
        super().__init__(msg, *args, **kwargs)


class RateLimited(Exception):
    def __init__(self, *args, **kwargs):
        msg = 'Rate limit reached'
        super().__init__(msg, *args, **kwargs)
