import re
print('Loading the files and preparing the system...')
print('The system is ready. Enter your text, ("close" to close the system):')
text = input("")
buffer = ""
while text != 'close':
    buffer += text
    # using regex( findall() )
    # to extract words from string
    res = re.findall(r'\w+', buffer)
    res = [x.lower() for x in res]
    print('Here are 5 suggestions: ' + " ".join(res))
    text = input(buffer)
    if text[-1] == '#':
        buffer = ""
        text = input("Enter your text: ")
print('System closed')
