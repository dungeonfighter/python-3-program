import sys
import time
import random
import math
from Kmeans import Kmeans

def main():
	if len(sys.argv) != 6 :
		print("error parameter setting")
		sys.exit(2)	
	T = Kmeans(sys.argv[1] , int(sys.argv[2]) , int(sys.argv[3]) , int(sys.argv[4]) , int(sys.argv[5]) )
	T.run()
	
if __name__ == "__main__":
    main()
