from library_app.user import User

def test_smoke_user_can_login():
    """ Tests user login capability """
    # Arrange
    users = {}

    # Act
    users["Nick"] = User("Nick")
    current_user = users["Nick"]

    # Assett
    assert current_user is not None
    assert current_user.name == "Nick"