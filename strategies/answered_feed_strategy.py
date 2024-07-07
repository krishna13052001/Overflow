from services.question_service import QuestionService

class AnsweredFeedStrategy:
    def get_feed(self, **kwargs):
        questions = QuestionService.get_instance().get_questions()
        return [q for q in questions if q.answers]