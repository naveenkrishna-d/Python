# file = open('fundata.txt','w')

# file.write('Hello\n')
# file.write('how are you\n')

# file = open('fundata.txt','a')

# file.write('Hello\n')
# file.write('how are you')

# file = open('fundata.txt','r')
# content = file.read()
# print(content)

# file.close()

# context manager('with' statement)

with open('fundata.txt','r') as file:
    content = file.read()
    print(content)

#read content from source file and write it to destination file
with open('source.txt','r') as source_file:
    content = source_file.read()

with open('destination.txt','w') as dest_file:
    dest_file.write(content)