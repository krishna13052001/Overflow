from models.topic import Topic
from models.user import User
from typing import Dict
class TopicService:
    _instance = None

    def __init__(self):
        self.topics: Dict[str, Topic] = {}

    @staticmethod
    def get_instance():
        if TopicService._instance is None:
            TopicService._instance = TopicService()
        return TopicService._instance


    def add_topic(self, name: str):
        if name not in self.topics:
            self.topics[name] = Topic(name)

    def get_topic(self, name: str) -> Topic:
        return self.topics.get(name, None)

    # def get_all_topics(self) -> list[Topic]:
    #     return list(self.topics.values())

    """def subscribe(self, topic_name: str, user: User):
        topic = self.get_topic(topic_name)
        print("[subscribe ], is topic subscribe? ", topic)
        if topic:
            topic.subscriber(user)
            user.subscribe(topic_name)
        else:
            self.add_topic(topic_name)
            self.subscribe(topic_name, user)"""

    def subscribe(self, topic_name: str, user: 'User'):
        self.add_topic(topic_name)
        topic = self.get_topic(topic_name)
        topic.subscribe(user)
        user.subscribe(topic_name)

    def unsubscribe(self, topic_name: str, user: 'User'):
        if topic_name in self.topics:
            topic = self.topics[topic_name]
            topic.unsubscribe(user)
            user.unsubscribe(topic_name)

    def add_question(self, question: 'Question'):
        for topic_name in question.topics:
            if topic_name in self.topics:
                self.topics[topic_name].add_question(question)
