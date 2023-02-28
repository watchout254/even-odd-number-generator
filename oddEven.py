import sys

print(f"\t\t\t\t\tWelcome to odd/even number determiner.\n"
      f"\tChoose 1/2\n"
      f"1. Yes to continue\n"
      f"2. No to close program\n")

biggie = 100
ori = 0
chagua = int(input("Your option: "))
if chagua == 1:
   while ori <= biggie:
       if ori % 2 == 0:
           print(f"{ori} is an even number")
           ori+=1
       else :
           print(f"{ori} is an odd number")
           ori +=1

else:
    print("ciaooo....")
    sys.exit()
print("There you go ma mehn, i got you")