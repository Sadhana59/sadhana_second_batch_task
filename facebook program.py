import fbchat 
from fbchat  import Client
from getpass import getpass 
username = "sadhu3dharsiny@gmail.com"
client = fbchat.Client(username, getpass()) 
no_of_friends = int("Number of friends: ")
for i in range(no_of_friends): 
	name = str("Name: ")
	friends = client.getUsers(name) 
	friend = friends[0] 
	msg = str("Message: ")
	sent = client.send(fbchat.models.Message(msg),friend.uid) 
	if sent: 
		print("Message sent successfully!") 