from models.user import User

from datetime import datetime
class Answer:
    def __init__(self, user: User, content: str):
        self.user = user
        self.content = content
        self.timestamp = datetime.now()
        self.votes: int = 0

    def upvote(self):
        self.votes += 1

    def downvote(self):
        self.votes -= 1