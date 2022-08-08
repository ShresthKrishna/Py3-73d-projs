from logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
conti="yes"
while conti=="yes":
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      if direction=="decode":
          shift*=(-1)
      def ceaser(text,shift, direction):
          word=""
          for i in text :
              position=ord(i) + shift
              print(position)
              if position>122:
                  position= 97 + 122 - ord(i) + shift
              if position<97:
                  position= 122 - (ord(i)-97 + shift)
              word+=chr(position)
              print(word)
          print(f"The {direction}d word is {word}")
      ceaser(text,shift,direction)
      conti=input("Type 'yes' if you want to continue else type 'no'\n").lower()
print("Thank oyu for using encoder and decoder")




