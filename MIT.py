cube=-8
#for guess in range(cube+1):
    #if guess**3 == cube:
      #  print("Cube root of", cube, "is", guess)

#abs= absolute value because you may want to find the cube root of negative numbers
#for guess in range(abs(cube)+1):
   # if guess**3 >= abs(cube):
    #    break
    #if guess**3 !=abs(cube):
       # print(cube, "is not a perfect cube")
    #else:
     #   if cube<0:
      #      guess= -guess
       # print("Cube root of" + str(cube)+ "is" + str(guess))


#this only works for positive cubes
cube=3456
epsilon= 0.01
num_guesses=0
low=0
high=cube
guess= (high+low)/2.0
while abs(guess**3-cube) >= epsilon:
    if guess**3< cube:
        low=guess
    else:
        high=guess
    guess= (high+low)/2.0
    num_guesses +=1
print ("num_guess=", num_guesses)
print (guess, "is close to the cube root of", cube)

#approx. solutions start with a guess an increment by small value