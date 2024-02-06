#An Email Simulation
inbox = []
outbox = []
class Email :
# defining the init properties of the class 
    def __init__(self, email_contents, from_address):

        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address
# defining some functions of the class 
    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True
    
    def __str__(self):
        output = f"From: {self.from_address}\n\n"
        output += f"Content: {self.email_contents}"

        return output
    
    
# adding an email to the inbox
def add_email(from_address, email_contents):
    email_object = Email(from_address, email_contents)
    inbox.append(email_object)
add_email("g@gyg.com", "gfghfhgjhg")
add_email("g@g.com", "hbjbhkbhjbk")

# returning the amount of emails in the inbox
def get_count():
    count = 0
    for email in inbox:
        count += 1
        return count

# reading a specific email from the inbox
def get_email():

    for index, email in enumerate(inbox, 1):
        print(f"{index}. {email.from_address}")

    choice = int(input("Please select the index of the email you would like to read: ")) - 1

    email = inbox[choice]
    print(email)
    email.mark_as_read()

def get_unread_emails():
    for email_obj in inbox:
        if not email_obj.has_been_read:
            print(email_obj)

def get_spam_emails():
    for email in inbox:
        if email.is_spam:
            print(email)

def delete():
    for index, email in enumerate(inbox):
        print(f"{index}. {email.from_address}")

        choice = int(input("which email would you like to delete? "))
        inbox.remove(inbox[choice])


def send_email(from_address, email_contents):
    new_email = Email(from_address, email_contents)
    outbox.append(new_email)

# we use a loop to execute some of the functions
while True:
    user_choice = input("What would you like to do - read/mark spam/send/quit?").lower()

    if user_choice == "read":
        get_email()

    elif user_choice == "mark spam":
        
        for index, email in enumerate(inbox, 1):
            print(f"{index}. {email.from_address}")

        choice = int(input("Please select the index of the email you would like to mark as spam: ")) - 1

        email = inbox[choice]
        
        email.mark_as_spam()
            
    elif user_choice == "send":
        send_email(input("what is your email address: "), input("contents: "))

    elif user_choice == "quit":
        print("Goodbye")
        break

    else:
        print("oops! try again.")
        continue

