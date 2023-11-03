class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []
info = input()
while info != 'Stop':
    sender, receiver, content = info.split()
    email_info = Email(sender, receiver, content)
    emails.append(email_info)
    info = input()
indexes = [int(index) for index in input().split(', ')]
for index in indexes:
    emails[index].send()
for current_email in emails:
    print(current_email.get_info())


