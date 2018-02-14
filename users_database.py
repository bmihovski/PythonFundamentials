"""
You have been tasked to create a database for several users, using … Text files.
The client will give you several input commands. There are two main commands:
"	register {username} {password} {confirmPassword}
"	login {username} {password}
"	logout
If you receive the register command, you must store the user in your database of users, with the given password.
"	If there is already a user with the given username, you must print "The given username already exists.",
and ignore the command.
"	If the password and confirmPassword, do NOT match, print on the console "The two passwords must match.",
and ignore the command.
If you receive the login command, you must log in the user with the given username and password.
"	If there is already a logged in user, you must print "There is already a logged in user.", and ignore the command.
"	If there is NO user, with the given username you must print "There is no user with the given username.",
and ignore the command.
"	If the password is does NOT match the one with which the user was registered,
you must print "The password you entered is incorrect.", and ignore the command.
If you receive the logout command, you must logout the, currently logged in, user.
"	If there is NO currently logged in user, you must print "There is no currently logged in user.",
and ignore the command.
When you receive the command "exit", the input sequence ends. You must store the current database of REGISTERED users,
in a file called "users.txt". The way you store them is up to you. You must load it, every time the program is ran.

Examples

Input
register Simo 123 123
register Ivo 123 132
login Simo 132
login Simo 123
logout
register pesho pesho pesho
login Ivo 123
login pesho pesho
exit

Output
The two passwords must match.
The password you entered is incorrect.
There is no user with the given username.

The second example test, DEPENDS on the first one.
Run the first one, save the resulting database from it, and then run the second one, in order to get correct results.

Input
register Merry 123456 123456
register pesho pesho pesho
logout
login Simo 123
logout
exit

Output
The given username already exists.
There is no currently logged in user.
"""
