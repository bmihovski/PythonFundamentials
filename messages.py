from collections import defaultdict
from itertools import zip_longest

"""
Create a class User, which has a Username (string), and ReceivedMessages (Collection of Messages).
Create a class Message, which has a Content (string) and a Sender (User).
You will have to store a messaging history for every user. The input consists of 2 commands:
"register {username}"
"{senderUsername} send {recipientUsername} {content}"

The register command, registers a user with the given username.
The send command, sends a message, from the given sender, to the given recipient, with the given content.
That means that you must add the message to the recipient's ReceivedMessages.
If even one of the given names does NOT exist, ignore the command.
When you receive the command "exit" you must end the input sequence.
After that you will receive 2 usernames, separated by a space.
You must print all messages, sent, between the two users, corresponding to the given usernames.
The messages should be printed in a specified way. You should print first a message SENT from the first user,
then a message SENT from the second user, then a message from the first user, and so on.
If one of the collections of messages has more elements than the other, just print the remaining elements from it.
The first user's messages must be printed in the following way:
"{firstUser}: {content}"
The second user's message must be printed in the following way:
"{content} :{secondUser}"
When you print the whole output, it should look like this:
{firstUser}: {content1}
{content1} :{secondUser}
{firstUser}: {content2}
{content2} :{secondUser}
. . .
In case there are NO messages between the two users, print "No messages".

Examples

Input
register Ivan
register Pesho
Ivan send Pesho pesho
Ivan send Pesho pesho_tam_li_si?
Pesho send Ivan kaji_vanka
Pesho send Ivan tuk_sum
Pesho send Ivan chakai_che_bachkam
Ivan send Pesho kvo_stava
Ivan send Pesho kak_si
Ivan send Pesho deka_izbega_be?
Ivan send Pesho pecaaa!!!
exit
Ivan Pesho

Output
Ivan: pesho
kaji_vanka :Pesho
Ivan: pesho_tam_li_si?
tuk_sum :Pesho
Ivan: kvo_stava
chakai_che_bachkam :Pesho
Ivan: kak_si
Ivan: deka_izbega_be?
Ivan: pecaaa!!!
"""


class Message:
    def __init__(self, content, sender):
        """
        Constructs message object skeleton
        :param content: (Str) Chat message
        :param sender: (Str) Message sender
        """
        self.content = content
        self.sender = sender


user_chat = defaultdict()

while True:
    lines_input = input().split()
    if lines_input[0] == 'exit':
        break
    elif lines_input[0] == 'register':
        user_chat.update({lines_input[1]: []})
    elif lines_input[0] not in user_chat or lines_input[2] not in user_chat:
        continue
    elif lines_input[1] == 'send':
        recipient = lines_input[2]
        send_by = lines_input[0]
        message = lines_input[3]
        user_chat[recipient].append(Message(message, send_by))

users_chat_history = input().split()
first_user_received = [user.content for user in user_chat[users_chat_history[0]]
                       if user.sender == users_chat_history[1]]
second_user_received = [user.content for user in user_chat[users_chat_history[1]]
                        if user.sender == users_chat_history[0]]

if not first_user_received and not second_user_received:
    print('No messages')

for second_user_messages, first_user_messages in zip_longest(second_user_received, first_user_received):
    if second_user_messages is not None:
        print(f'{users_chat_history[0]}: {second_user_messages}')
    if first_user_messages is not None:
        print(f'{first_user_messages} :{users_chat_history[1]}')
