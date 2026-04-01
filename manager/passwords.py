from manager.storage import load, save

passwords = load()

passwords = []
def add_password(save(passwords)):
    passwords.append({
        "site": site,
        "login": login,
        "password": password
    })
def list_passwords():
    return passwords
if __name__ == "__main__":
    add_password("gmail", "user", "1234")
    print(list_passwords())
