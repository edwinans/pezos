import sys
from communication import miner

if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        if (sys.argv[1] == 'demo'):
            print("Demo mode")

    else:
        print("Normal mode")
        miner.mine()
    
    