from manager.passwords import add_password, list_passwords

def test_add_password():
    add_password("test", "user", "pass")
    assert len(list_passwords()) > 0
