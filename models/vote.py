class Vote:
    def __init__(self, user: User, item: 'Question' or 'Answer', value: int):
        self.user = user
        self.item = item
        self.value = value