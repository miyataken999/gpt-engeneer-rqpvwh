import pytest
from src.main import greet_user
from src.models.user import User

def test_greet_user() -> None:
    """Tests the greet_user function"""
    user = User(id=1, name="John Doe", email="johndoe@example.com")
    assert greet_user(user) == "Hello, John Doe!"

def test_main(capsys) -> None:
    """Tests the main function"""
    import src.main
    src.main.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, John Doe!\n"