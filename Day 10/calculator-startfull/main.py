

from art import logo


def add(n1,n2):
  return n1+n2


def sub(n1,n2):
  return n1-n2


def div(n1,n2):
  return n1/n2


def mult(n1,n2):
  return n1*n2


calc_dict={
  "+":add,
  "-":sub,
  "/":div,
  "*":mult,
}
print(logo)

def calc():

  n1=int(input("Enter the first number: "))

  n2=int(input("Enter the second number: "))
  #operation=input("Which operation do you want to perform:\n+\n-\n/\n* ")

  continue_eq= True
  while continue_eq==True:
    for i in calc_dict:
        print(i)
    operation=input("Which of this operation do you want to perform: ")
    if operation in calc_dict:
      answer_fn=calc_dict[operation]
      answer=answer_fn(n1,n2)
      print(f"{n1} {operation} {n2} = {answer}")
    else:
      print("Wrong operation")
    ask_prompt=input(f"wanna continue? with {answer} 'y' or 'n'").lower()
    if ask_prompt=='y':
      n1=answer
      n2=int(input("Enter another number: "))
    else:
      continue_eq=False
      calc()
calc()



