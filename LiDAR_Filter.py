from collections import deque
import numpy as np
np.set_printoptions(suppress=True,precision=2)

class Filter:
    
    def __init__(self, N):
	#Constructor in Filter class: __init__(self, N)
		self.N = N

    def update(self, scan):
	#update method defined as a function in Filter class: update(self, scan)
    #self.scan = scan
        pass


class RangeFilter(Filter):

    def __init__(self, N, range_min, range_max):
    #Constructor in RangeFilter class: __init__(self, N)
		Filter.__init__(self,N)
		self.range_max = range_max
		self.range_min = range_min

    def update(self, scan):
    #update method defined as a function in RangeFilter class: update(self, scan)
		temp = np.array(scan)
		temp[temp > self.range_max] = self.range_max
		temp[temp < self.range_min] = self.range_min
		return temp
    
class MedianFilter(Filter):

    def __init__(self, N, D):
	#Constructor in MedianFilter class: __init__(self, N, D)
        Filter.__init__(self,N)
        self.D = D
        self.scans = deque()


    def update(self, scan):
	#update method defined as a function in MedianFilter class: update(self, scan)
        if len(self.scans) >= self.D+1:
            self.scans.popleft()
        self.scans.append(scan)
        return np.median(self.scans, axis=0)

#Test case for RangeFilter

def test_ranger_filter():
    N = 5
    low = 0.03
    high = 50
    
    range_filter = RangeFilter(N, low, high)

    #Sample uniform distribution
    scan = np.random.uniform(-80,80,N)
    print 'Input scan:',scan,'\t','Output scan: ',range_filter.update(scan),"\n"
    
    
#Test case for MedianFilter
def test_median_filter():
    N = 5
    D = 3
    
    median_filter = MedianFilter(N, D)
    
    #Sample input
    scans = []
    scans.append([0.,1.,2.,1.,3.])
    scans.append([1.,5.,7.,1.,3.])
    scans.append([2.,3.,4.,1.,0.])
    scans.append([3.,3.,3.,1.,3.])
    scans.append([10.,2.,4.,0.,0.])
    
    for scan in scans:
        print 'Input scan:',scan,'\t','Output scan:',median_filter.update(scan)
    
print("Testing Range Filter\n")
test_ranger_filter()  
print("Testing Median Filter\n")
test_median_filter()
