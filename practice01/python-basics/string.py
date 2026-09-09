x = "Hello world"
y = "FAAA"

print(len(x)) #length of string x

print(x[4])   #get the character at pos 4
print(x[2:6]) #get the characters from pos 2 to 6
print(x[:5])  #get the characters from the start to pos 5
print(x[2:])  #get the characters from pos 2 to the end

print(x.upper()) #returns the string in upper case
print(x.lower()) #returns the stirng in lower case
print(x.strip()) #removes any gaps from the beginning and the end
print(x.replace('H', 'W')) #replace all substring 'H' to 'W'
print(x + y) #merge x and y