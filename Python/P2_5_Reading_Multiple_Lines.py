with open('P2_5_Reading_Email.txt', 'r') as emails:
    # print(emails.readlines())
    emails=emails.readlines()
print(emails)
for email in emails:
    if "gmail" in email:
        print(email.rstrip())
