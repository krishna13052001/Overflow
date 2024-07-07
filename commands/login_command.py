from services.user_service import UserService
class LoginCommand:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self, email: str):
        user = self.user_service.get_user(email)
        if user:
            self.user_service.login(user)
            print(f"User {email} logged in")
        else:
            print("User not found")
