import sys
import time
import random
import math
from Kmeans import Kmeans

def main():
	if len(sys.argv) != 7 :
		print("error parameter setting")
		sys.exit(2)	
	
	s = time.time()
	T = Kmeans(sys.argv[1] , int(sys.argv[2]) , int(sys.argv[3]) , int(sys.argv[4]) , int(sys.argv[5]) , int(sys.argv[6]))
	T.run()
	t = time.time() - s

	print('took {} secs'.format(round(t, 3)))
	
	f = open("result.txt",mode = 'a')
	f.seek(0,2)
	f.write("\n"+"took "+str(t)+" secs")
	f.close()
	
if __name__ == "__main__":
    main()
