class UserSignupCommand:
    def __init__(self, user_service: 'UserService'):
        self.user_service = user_service

    def execute(self, email: str, name: str, profession: str):
        user = self.user_service.signup(email, name, profession)
        print(f"User email {email}, name: {name} signed up as {profession}")
        return user
