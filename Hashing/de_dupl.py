users = {
    "ravi@gmail.com",
    "priya@gmail.com",
    "ravi@gmail.com",
    "priya@gmail.com",
    "prema@gmail.com",
    "ravi@gmail.com",
    "Nanu@gmail.com"
}


def remove_dupl(emails):
    seen = set()
    unique = []
    for email in emails:
        if email not in seen:
            unique.append(email)
            seen.add(email)
    return unique

clean = remove_dupl(users)
print(clean)