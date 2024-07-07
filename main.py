from models.user import User
from services.user_service import UserService
from services.question_service import QuestionService
from services.feed_service import FeedService
from services.topic_service import TopicService
from commands.user_signup_command import UserSignupCommand
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.subscribe_command import SubscribeCommand
from commands.unsubscribe_command import UnsubscribeCommand
from commands.add_question_command import AddQuestionCommand
from commands.show_feed_command import ShowFeedCommand
from commands.add_answer_command import AddAnswerCommand

class FlipkartOverflow:
    def __init__(self):
        self.user_service = UserService().get_instance()
        self.question_service = QuestionService.get_instance()
        self.feed_service = FeedService()
        self.topic_service = TopicService.get_instance()

    def user_signup(self, name: str, profession: str, email: str):
        user_signup_command = UserSignupCommand(self.user_service)
        user = user_signup_command.execute(email, name, profession)
        return user

    def login(self, email: str):
        login_command = LoginCommand(self.user_service)
        login_command.execute(email)

    def logout(self):
        logout_command = LogoutCommand(self.user_service)
        logout_command.execute()

    def subscribe(self, topics: list[str]):
        user = self.user_service.get_current_user()
        if not user:
            raise Exception("No user logged in")
        subscribe_command = SubscribeCommand(self.topic_service, user)
        for topic in topics:
            subscribe_command.execute(topic)

    def unsubscribe(self, topics: list[str]):
        user = self.user_service.get_current_user()
        if not user:
            raise Exception("No user logged in")

        unsubscribe_command = UnsubscribeCommand(self.topic_service, user)
        for topic in topics:
            unsubscribe_command.execute(topic)

    def add_question(self, content: str, topics: list[str]):
        add_question_command = AddQuestionCommand(self.question_service, self.user_service)
        add_question_command.execute(content, topics)

    def show_feed(self, filter: list[str] = [], answered: bool = False):
        show_feed_command = ShowFeedCommand(self.feed_service)
        feed = show_feed_command.execute(filter=filter, answered=answered)
        for question in feed:
            print(f"Question: {question.content}, Topics: {question.topics}, Votes: {question.votes}")
            for answer in question.answers:
                print(f"Answer: {answer.content}, Votes: {answer.votes}")

    def add_answer(self, question: 'Question', content: str):
        add_answer_command = AddAnswerCommand(self.question_service, self.user_service)
        add_answer_command.execute(question, content)

    def get_question_object(self, contents: str):
        return self.question_service.get_question_by_contents(contents)

    def upvote_question(self, question: 'Question'):
        user = self.user_service.get_current_user()
        if not user:
            raise Exception("No user logged in")
        question.upvote()
        print(f"Question upvoted: {question.content}")

    def upvote_answer(self, answer: 'Answer'):
        user = self.user_service.get_current_user()
        if not user:
            raise Exception("No user logged in")
        answer.upvote()
        print(f"Answer upvoted: {answer.content}")

def main():
    app = FlipkartOverflow()
    sachin = app.user_signup('Sachin', 'Developer', 'sachin.dev@gmail.com')
    app.login('sachin.dev@gmail.com')
    app.subscribe(['java', 'hadoop', 'jdk'])
    # print(app.topic_service)
    app.add_question("What are new open source jdks?", topics=['java', 'jdk'])
    app.add_question("Does Hadoop work on JDK 11?", topics=['hadoop', 'jdk'])
    print("Displaying the feed without any filter: ")
    app.show_feed()
    print("End of displaying")
    print("=====================")
    print("Displaying the feed with filter: [Java] ")
    app.show_feed(filter=['java'])
    print("=====================")
    print("Displaying the feed with filter: [JDK]")
    app.show_feed(filter=['jdk'])
    print("=====================")
    print("***********************")
    question = app.get_question_object("What are new open source jdks?")
    app.add_answer(question, "List of details are new in open source")
    print("=====================")
    print("*********************")
    app.show_feed(answered=True)
    print("********************* Before")
    print(sachin.subscriptions)
    app.show_feed(filter=['python'])


    # print()
    # print()
    try:
        app.add_question(None, topics = ["python"])
    except Exception as e:
        print(e)
    print("After")
    app.show_feed(filter=['python'])
    print()
    # question = app.get_question_object(None)
    # app.add_answer(question, None)
    app.logout()


    app.show_feed()
    try:
        app.add_question("What are new open source jdks?", topics=['java', 'jdk'])
    except Exception as e:
        print("add_question: ", e)
    # app.upvote_question()

if __name__ == "__main__":
    main()