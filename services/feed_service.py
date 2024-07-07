from strategies.answered_feed_strategy import AnsweredFeedStrategy
from strategies.default_feed_strategy import DefaultFeedStrategy
from strategies.filter_feed_strategy import FilterFeedStrategy
class FeedService:
    def __init__(self):
        self.strategies = {
            'default': DefaultFeedStrategy(),
            'filter': FilterFeedStrategy(),
            'answered': AnsweredFeedStrategy()
        }

    def show_feed(self, strategy: str = 'default', **kwargs):
        # print("[show_feed] strategy : ", strategy)
        return self.strategies[strategy].get_feed(**kwargs)
