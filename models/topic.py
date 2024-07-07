from models.user import User
from models.questions import Question

class Topic:
    def __init__(self, name: str):
        self.name = name
        self.subscribers: list['User'] = []
        self.questions: list['Question'] = []

    def subscribe(self, user: 'User'):
        if user not in self.subscribers:
            self.subscribers.append(user)

    def unsubscribe(self, user: 'User'):
        if user in self.subscribers:
            self.subscribers.remove(user)

    def add_question(self, question: 'Question'):
        self.questions.append(question)