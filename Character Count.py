import pprint
string = 'Hello world'

def characterCount(countString):
    count = {}
    for char in countString:
        count.setdefault(char, 0)
        count[char] += 1
    pprint.pprint(count)

characterCount(string)
