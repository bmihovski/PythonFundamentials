"""
Write a program that receives a list of username-password pairs in the format "{username} -> {password}".
If there's already a user with that username, replace their password. After you receive the command "login",
login requests start coming in, using the same format.
Your task is to print the status of user login, using different messages as per the conditions below:
    If the password matches with the user's password, print "{username}: logged in successfully".
    If the user doesn't exist, or the password doesn't match the user, print "{username}: login failed".
When you receive the command "end", print the count of unsuccessful login attempts,
using the format "unsuccessful login attempts: {count}".
Hints
    Parse the commands by splitting by space. The first element is the username, while the third element is the password.
    Store the user entries in dictionary with key {username} and value {password}.

Input
ivan_ivanov -> java123
pesh0 -> qwerty
stamat4e -> 111111
princess_penka -> MyPrince
login
pesh0 -> qwertt
ivan_ivanov -> java123
stamat4e -> 111112
princess_penka -> MyPrince
end

Output
pesh0: login failed
ivan_ivanov: logged in successfully
stamat4e: login failed
princess_penka: logged in successfully
unsuccessful login attempts: 2
"""
input_credentials = list()
stored_credentials = dict()
login_flag = None

while 'end' not in input_credentials:
    input_credentials = input().split(' ')

    if 'end' in input_credentials:
        continue
    elif 'login' in input_credentials:
        login_flag = 'login'
    elif login_flag == 'login':
        try:
            if (input_credentials[0] not in stored_credentials or stored_credentials[input_credentials[0]] !=
                    input_credentials[2]):
                stored_credentials.update({'failed': (stored_credentials['failed'] + 1)})
                print(f'{input_credentials[0]}: login failed')
            else:
                print(f'{input_credentials[0]}: logged in successfully')
        except KeyError:
            stored_credentials.update({'failed': 0})
            print(f'{input_credentials[0]}: login failed')
    else:
        stored_credentials.update({input_credentials[0]: input_credentials[2]})

print(f'unsuccessful login attempts: {stored_credentials["failed"] + 1}')
