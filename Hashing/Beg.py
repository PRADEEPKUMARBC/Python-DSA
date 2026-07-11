users = {
    "pradeepkumarbc138@gmail.com",
    "pradeepkumarbc716@gmail.com",
    "pbc@gmail.com"
}

def login(email):
    for user in users:
        if user == email:
            return "Login successful"
    return "User not found"

print(login("pbc@gmail.com"))