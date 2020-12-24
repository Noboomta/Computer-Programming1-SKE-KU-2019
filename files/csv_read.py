filename = 'plain.csv'

file = open(filename, mode='r') # r is to read
# file = open(filename, mode='w') # w is to write 
text = file.read()
file.close()

print(text)

# with open(filename, 'r') as fill:
#     print(file.read())