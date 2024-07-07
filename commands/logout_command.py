from services.user_service import UserService
class LogoutCommand:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def execute(self):
        self.user_service.logout()
        print("User logged out")
