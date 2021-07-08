import time, sys
indent = 0
indentInc = True

try:
    while True:
        print('$' * indent, end = '')
        print('********')
        time.sleep(0.1)
    
        if indentInc:
            indent = indent + 1
            if indent == 20:
                indentInc = False
        else:
            indent = indent - 1
            if indent == 0:
                indentInc = True
except KeyboardInterrupt:
    print("program is stopped")
    sys.exit()