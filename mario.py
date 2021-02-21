# 1- ask the user to enter a height of the block in range 1 to 10
# 2- if statement to make sure that int is valid number
        # if not ask the user again for number
# 3- while loop to build a block of hashes increasing by 1 in each row
# 4- change block direction from left to right by adding dots

number= int(input('choose a number for the block height from 1 to 8: '))
if number >=1 and number <= 8:
    print('height is', number)
else: 
    int(input('please, choose a valid number for the height: '))
    
    count=1
    while count <= number:
         block= number + count
         print(block,'#')
         count= count + 1
range(number)
for number in range(number):
    number="#" * number
    print(number)




         

         

