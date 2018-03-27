import debugger                                                                    # Importing debugger file 
import initialization                                                              # Importing Initialization file
import registers                                                                   # Importing registers file


def start(isCmdLine=False):
    query = raw_input("Do you want to start in DEBUGGER mode(y/n/q to quit): ")
    if query == 'y' or query == 'Y':
        registers.dBugOn = True
        debugger.startDebugger(isCmdLine=isCmdLine)

    elif query == 'N' or query == 'n':
        initialization.memInit(isCmdLine=isCmdLine)

    elif query == 'Q' or query == 'q':
        exit(1)

    else:
        print "invalid command. Please Retry!"
        start()


if __name__ == "__main__":
    qw = raw_input(
        "Want to Write Program In Command Line?\n Y or y for start\n N or n for providing file name\nq or Q For quit :")
    if qw == 'y' or qw == 'Y':
        print "In Order To End The Progarm Write EOF ,last command of program Must Be HLT"
        f = open('input.asm', 'w')                          # All Instruction Are Written In A File
        while True:                                         # while(1)
            cmd = raw_input().strip()                       # remove white space for string
            if cmd == "EOF":
                f.close()
                start(isCmdLine=True)
                break
            else:
                f.write(cmd + "\n")
    elif qw == 'q' or qw == 'Q':
        exit(1)

    else:
        start()
