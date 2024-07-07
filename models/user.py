class User:
    def __init__(self, email: str, name: str, profession: str):
        self.name = name
        self.email = email
        self.profession = profession
        self.subscriptions: list[str] = []
        self.asked_questions: list['Question'] = []
        self.answered_questions: list['Answer'] = []

    def subscribe(self, topic: str):
        if topic not in self.subscriptions:
            self.subscriptions.append(topic)

    def unsubscribe(self, topic: str):
        if topic in self.subscriptions:
            self.subscriptions.remove(topic)
