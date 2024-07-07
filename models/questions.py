from models.user import User
from models.answer import Answer

from datetime import datetime


class Question:
    def __init__(self, user: User, content: str, topics: list[str]):
        self.user = user
        self.content = content
        self.topics = topics
        self.timestamp = datetime.now()
        self.answers: list[Answer] = []
        self.votes: int = 0

    def add_answer(self, answer: 'Answer'):
        self.answers.append(answer)

    def upvote(self):
        self.votes += 1

    def downvote(self):
        self.votes -= 1