from models.user import User

def greet_user(user: User) -> str:
    """Returns a greeting message for the user"""
    return f"Hello, {user.name}!"

def main() -> None:
    """Main entry point"""
    user = User(id=1, name="John Doe", email="johndoe@example.com")
    print(greet_user(user))

if __name__ == "__main__":
    main()