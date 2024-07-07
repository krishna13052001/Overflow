from services.question_service import QuestionService

class FilterFeedStrategy:
    def get_feed(self, filter: list[str] = [], **kwargs):
        questions = QuestionService.get_instance().get_questions()
        return [q for q in questions if any(topic in q.topics for topic in filter)]