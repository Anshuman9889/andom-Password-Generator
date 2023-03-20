import random

symbol=['!','@','#','$','%','&','^','*','(',')']
letters=['A','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','q','w','e','r','t','y','u','i','o','p','S','D','F','G','H','J','K','L','Z','X','C','V',
      'B','N','M','Q','W','E','R','T','Y','U','I','O','P']
number=['1','2','3','4','5','6','7','8','9','0']


print("welcome to pypassword generator!")
#print(letters)
nr_letter=int(input("how many letter would u like\n"))

#print(symbol)
nr_symbol=int(input("how many symbol u would like\n"))

#print(number)
nr_number=int(input("how many number would u like\n"))

password=""

for char in range(1, nr_letter+1):
   # random_char=random.choice(letters)
   # print(random_char)
   #random_char=random.choice(letters)
   password+=random.choice(letters)
# for symbol
for char in range(1, nr_symbol+1):
    password+=random.choice(symbol)
    
for char in range(1,nr_number+1):
    password+=random.choice(number)

print(f" your random generator password {password}")
   
