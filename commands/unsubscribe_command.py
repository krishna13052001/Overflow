from services.topic_service import TopicService
from models.user import User
class UnsubscribeCommand:
    def __init__(self, topic_service: TopicService, user: User):
        self.topic_service = topic_service
        self.user = user

    def execute(self, topic_name: str):
        self.topic_service.unsubscribe(topic_name, self.user)
        print(f"User {self.user.name} unsubscribed from {topic_name}")
