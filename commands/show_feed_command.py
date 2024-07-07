from services.feed_service import FeedService
class ShowFeedCommand:
    def __init__(self, feed_service: FeedService):
        self.feed_service = feed_service

    def execute(self, filter: list[str] = [], answered: bool = False):
        if answered:
            return self.feed_service.show_feed('answered')
        elif filter:
            return self.feed_service.show_feed('filter', filter=filter)
        else:
            return self.feed_service.show_feed()
