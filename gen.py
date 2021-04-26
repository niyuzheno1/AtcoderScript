import sys
import argparse
import os

def main():
    print("Please Enter Contest Round Name:")
    x = input()
    cmd1 = "atcoder-tools gen {}".format(x)
    os.system(cmd1)
    cmd2 = "xcopy .\\tmp\\ %USERPROFILE%\\atcoder-workspace\\{} /E /H /C /I".format(x)
    os.system(cmd2)
    cmd3 = "code %USERPROFILE%\\atcoder-workspace\\{}".format(x)
    os.system(cmd3)
    
    

if __name__ == "__main__":
    main()