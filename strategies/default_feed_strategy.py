from services.question_service import QuestionService

class DefaultFeedStrategy:
    def get_feed(self, **kwargs):
        # print("[DefaultFeedStrategy]: get_feed")
        return QuestionService.get_instance().get_questions()
