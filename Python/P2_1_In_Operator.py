my_answer=input("what is your answer ")
options=["rock", "paper", "scissors"]
if my_answer in options:
    print("that option is a viable options")
else:
    print("wrong answer try again")
print("\n")

key="name"
person={
    "name": "kailash",
    "profession": "coding",
}
if key in person:
    print("name is a valid dictionary key in the person object")
else:
    print("not invalid dictionary")
