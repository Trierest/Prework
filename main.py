

name_input = input('Welcome to Quode!\nYou are talking to the owner of this space, "Me".\nTalk to Me. What is your name?\n')

print('Hey there, %s, that is a name.' %name_input)
age = int(input('Me belives that Me thinks differently than you, but Me is here for just you.\n\nSo, lets talk about you.\n\nHow old are you?\n'))

if age <= 13:
  joke_question = input('Well arent you young. Me bets that you would like to play a game.\nYou are the clown, tell me a joke, so Me can try to answer it.\n')
  joke_answer = input("Hmmm, Me doesn't know about that. What's the answer?\n")
  print("Well, Me would've thought it was funny if Me got it before you explained it.")

elif age < 18:
  print("That's cool. You are probably a student in high school.")
  response = input("How's school going for you?")
  print("Well, Me hopes that you still enjoy your school years.")

else:
  print("Oh, so you aren't young. Well, that doesn't stop you from talking to me does it?")

print("Well, it's nice talking to you, but Me is incomplete, because Me doesn't know when its creator will decide whether or not to continue building me, so this is the last thing Me does.\n\n")

num = 0

while True:
  add = int(input("Give Me a number to add that's not zero: "))
  if add == 0:
    break
  num += add

print("The total is %d. Well, Me's job is done here, goodbye!" % num)