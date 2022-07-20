#Chatbot Project

#Greeting
print('Greetings earthling I am Groot!')
print('I like traveling the galaxy and eating pizza')
name=input('What is your name?: ')
print('Hello', name,', it is a pleasure to eat you. I mean meet you!')

#Age
userage=input('Sooo anyways, how old are you little earthling?:')
print("Wow!", userage, "is still young. You should venture out to the galaxy")

myage=input('Can you guess my age?: ')
print ('Great guess! Yes, I am', myage, 'years old in earth years')
myage=int(myage)
alienyears=myage * 500
alineyears=int(alienyears)
print(',but in planet Xian I am', alienyears, 'years old')

#Earth year
earthyear=input("What year is it on earth?:")
earthyear=int(earthyear)
xianyear=earthyear * alienyears
print("I've been traveling through different galaxies and I've lost track of time. That means on planet xian it must be the year", xianyear,)



#Pizza

userslices=input('I love earth pizza. How many slices of pizza can you eat?')
print(userslices, "is a fair amount of slices to eat")
gslices=input('can you guess how many slices I can eat?:')
userslices=int(userslices)
gslices=int(gslices)
myslices=userslices+gslices
print("I guess you're not earth's mind reader! I could eat", myslices, "you have a small stomach compared to xian's" )


