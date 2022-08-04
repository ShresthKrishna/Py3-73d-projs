from logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
conti="yes"
while conti=="yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def ceaser(text,shift, direction):
      word=""
      for i in text : 
          if direction=="decode":
              shift*=-1
          position=ord(i) + shift
          if position>122:
              position=position-26
          if position<97:
              position=position+26
          if i not in alphabet:
              word+=i
          elif i in alphabet:
            word+=chr(position)
      print(f"The {direction}d word is{word}")
  ceaser(text,shift,direction)
  conti=input("Type 'yes' if you want to continue else type 'no'\n").lower()
print("Thank oyu for using encoder and decoder")




