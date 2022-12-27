import sys
stdin_fileno = sys.stdin
# print(type(stdin_fileno)) # stdin file number is _io.TextIOwrapper object
# keep on accepting input from user until the user enter exit
for line in stdin_fileno:
    # terminate the program when the user enter exit
    if 'exit' == line.strip():
        print('found zero, terminating the program')
        exit(0)
    else:
        print(f'message from the console ------><---------{line}')