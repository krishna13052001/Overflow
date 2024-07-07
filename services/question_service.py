from models.questions import Question
from services.topic_service import TopicService
from services.user_service import UserService


class QuestionService:
    _instance = None

    def __init__(self):
        self.questions: list[Question] = []

    @staticmethod
    def get_instance():
        if QuestionService._instance is None:
            # print("QuestionService instance created")
            QuestionService._instance = QuestionService()
        return QuestionService._instance

    def add_question(self, content: str, topics: list[str]):
        current_user = UserService.get_instance().get_current_user()
        if not current_user:
            raise Exception("No user logged in")
        question = Question(current_user, content, topics)
        self.questions.append(question)
        topic_service = TopicService.get_instance()
        topic_service.add_question(question)


    def get_questions(self) -> list[Question]:
        return self.questions

    def get_question_by_contents(self, content: str) -> Question:
        for question in self.questions:
            if question.content == content:
                return question