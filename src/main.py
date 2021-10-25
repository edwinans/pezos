import sys 
from communication import miner
from communication import miner_demo
if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == "demo":
            miner_demo.mine_demo()
    else:
        miner.mine()
