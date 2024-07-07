from services.question_service import QuestionService
from services.user_service import UserService

class AddQuestionCommand:
    def __init__(self, question_service: QuestionService, user_service: UserService):
        self.question_service = question_service
        self.user_service = user_service

    def execute(self, content: str, topics: list[str]):
        current_user = self.user_service.get_current_user()
        if not current_user:
            raise Exception("No user logged in")
        self.question_service.add_question(content, topics)
        print(f"Question added: {content} with topics {topics}")
