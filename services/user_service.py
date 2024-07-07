from models.user import User
class UserService:
    _instance = None
    _current_user: 'User' = None

    def __init__(self):
        self.users: Dict[str, User] = {}

    @staticmethod
    def get_instance():
        if UserService._instance is None:
            UserService._instance = UserService()
        return UserService._instance

    def signup(self, email: str, name: str, profession: str) -> User:
        if email in self.users:
            raise Exception("User already exists")
        user = User(email, name, profession)
        self.users[email] = user
        return user

    def get_user(self, email: str) -> User:
        return self.users.get(email, None)

    def login(self, user: 'User'):
        self._current_user = user

    def logout(self):
        self._current_user = None

    def get_current_user(self):
        return self._current_user


