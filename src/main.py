import sys
from communication import miner
from communication import miner_demo

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        argumentsWithValue = dict()
        argumentsWithNoValue = []
        for arg in sys.argv[1:]:
            mySplit = arg.split('=')
            if len(mySplit) == 1:
                argumentsWithNoValue.append(mySplit[0])
            else:
                argumentsWithValue[mySplit[0]] = mySplit[1]

        if "demo" in argumentsWithNoValue:
            miner_demo.mine_demo(argumentsWithNoValue, argumentsWithValue)
        else:
            miner.mine(argumentsWithNoValue, argumentsWithValue)   
    else:
        miner.mine([], dict())
