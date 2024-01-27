import sys
import getopt
print(sys.argv)
#python argument_parsing.py -f "log_msg.txt" -m "hello message"
opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename','message'])
message=''
for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg
with open(filename, 'w+') as f:
    f.write(message)

'''
def myfunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(kwargs["KEYONE"])
    print(kwargs["KEYTWO"])

myfunction('hey', True, 19, 'wow', KEYONE=1234,KEYTWO=4)
'''
