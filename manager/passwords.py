passwords = []
def add_password(site, login, password):
    passwords.append({
        "site": site,
        "login": login,
        "password": password
    })
def list_passwords():
    return passwords
