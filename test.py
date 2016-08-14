from subprocess import Popen, PIPE, STDOUT

f = open('tests.txt', 'r')

for command in f:
    command = command.rstrip('\r\n')
    # first run our program
    p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read().decode('utf-8')
    
    # which file did we want to open
    filename = command.split(" ")
    filename = filename[1]
    # now open the file with what it should be
    answer = open(filename + ".txt", 'r')
    if output != answer.read():
        print (command + " failed")
    else:
        print (command + " passed")
    
    