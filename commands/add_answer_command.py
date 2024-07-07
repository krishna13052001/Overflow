from services.question_service import QuestionService
from services.user_service import UserService
from models.questions import Question
from models.answer import Answer

from datetime import datetime
class AddAnswerCommand:
    def __init__(self, question_service: QuestionService, user_service: UserService):
        self.question_service = question_service
        self.user_service = user_service

    def execute(self, question: Question, content: str):
        current_user = self.user_service.get_current_user()
        if not current_user:
            raise Exception("No user logged in")
        if not any(topic in current_user.subscriptions for topic in question.topics):
            raise Exception("User not subscribed to question topics")
        answer = Answer(current_user, content)
        question.add_answer(answer)
        print(f"Answer added to question: {question.content}")
