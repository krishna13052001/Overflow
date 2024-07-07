from services.topic_service import TopicService
from models.user import User
class SubscribeCommand:
    def __init__(self, topic_service: TopicService, user: User):
        self.topic_service = topic_service
        self.user = user

    def execute(self, topic_name: str):
        self.topic_service.subscribe(topic_name, self.user)
        print(f"User {self.user.name} subscribed to {topic_name}")
