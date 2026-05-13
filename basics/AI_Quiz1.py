#" Salary Input
#salary = int(input("Apni salary likhein: "))

#if salary < 30000:
    #tax_rate = 0.05  # 5%
#elif salary >= 30000 and salary <= 70000:
   # tax_rate = 0.15  # 15%
#else:
   # tax_rate = 0.25  # 25%

# Final Tax calculation
#final_tax = salary * tax_rate

#print(f"Tax rate on your salary is {tax_rate * 100}%.")
#print(f"Your total tax is : {final_tax} rupees.")



#Given a list of words: words = ["apple", "banana", "kiwi", "cherry", "mango"]  Create a dictionary that maps each word to its corresponding length. Example Output: ({"apple": 5, "banana": 6, "kiwi": 4, "cherry": 6, "mango": 5})


# List of words
#words = ["apple", "banana", "kiwi", "cherry", "mango"]

#empty dictionary to store the results
#word_lengths = {}

#for loop
#for word in words:
    #word_lengths[word] = len(word) #Caculate length

#print(word_lengths)

#3. Create a Chat System using Object-Oriented Programming (OOP) concepts. You need to create the following classes:  • User  • Message  • ChatRoom  The system should implement the following functionalities:  • Sending messages  • Viewing chat history  • User joining and leaving the chat room


# 1. Message Class
class Message:
    def __init__(self, sender, content):
        self.sender = sender # Name of the user who sent it
        self.content = content # The actual text message

# 2. User Class
class User:
    def __init__(self, name):
        self.name = name

# 3. ChatRoom Class to manage everything
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []  # users currently in the room
        self.history = [] # Message objects

    def join(self, user):
        self.users.append(user)
        print(f"{user.name} joined the {self.room_name}.")

    def leave(self, user):
        self.users.remove(user)
        print(f"{user.name} left the {self.room_name}.")

    def send_message(self, user, text):
        if user in self.users:
            new_msg = Message(user.name, text)
            self.history.append(new_msg)
        else:
            print(f"Error: {user.name} is not in the room!")

    def view_history(self):
        print(f"\n--- {self.room_name} Chat History ---")
        for msg in self.history:
            print(f"[{msg.sender}]: {msg.content}")
#Objects
# Creating Users
ali = User("Ali")
sara = User("Sara")

# Creating ChatRoom
my_room = ChatRoom("Python Developers")

# Users joining
my_room.join(ali)
my_room.join(sara)

# Sending Messages
my_room.send_message(ali, "Hello everyone!")
my_room.send_message(sara, "Hi Ali, how are you?")

# Viewing History
my_room.view_history()

# User leaving
my_room.leave(ali)



























