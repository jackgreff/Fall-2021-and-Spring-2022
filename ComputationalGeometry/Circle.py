#Jack Greff - Circle/Circle intersection - done by myself (no help at all)
"""
Here are some examples of the circle-overlap problem,
in which we give the "x", "y", and radius for one circle and then the other,
and need to know if there are any points that line in/on both circles.
(Note that we don't allow a circle with negative radius.)


# An obvious overlap (Sample answer #3 got this wrong):
>>> circleOverlap(100,100,30, 125,100,30)
True

# An obvious non-overlap (Sample answer #1 gets this one wrong):
>>> circleOverlap(100,100,30, 225,100,30)
False

# An example copied from the "Console" window during a run of overlap-test-graphics
>>> circleOverlap( 160 ,  152 ,  82.8070045346 ,  198 ,  167 ,  93.813645063 )
True


##############################################################################
#
>>> circleOverlap( 82 ,  298 ,  69.00724599634447 ,  304 ,  303 ,  73.06161783043132 )#clear overlap
False
>>> circleOverlap( 92 ,  292 ,  80.0 ,  281 ,  292 ,  118.01694793545543) #not close to touch
True

>>> circleOverlap( 102 ,  228 ,  44.28317965096906 ,  106 ,  164 ,  12.36931687685298 )#close miss top
False
>>> circleOverlap( 206 ,  255 ,  58.0 ,  301 ,  267 ,  30.0 )#close miss right
False
>>> circleOverlap( 183 ,  250 ,  60.03332407921454 ,  163 ,  337 ,  22.02271554554524 )#close miss bottom
False
>>> circleOverlap( 204 ,  249 ,  72.0 ,  69 ,  248 ,  40.19950248448356 )#close miss left
False

>>> circleOverlap( 206 ,  282 ,  109.01834707974616 ,  202 ,  129 ,  51.419840528729765 ) #little intersection top
True
>>> circleOverlap( 219 ,  225 ,  137.01459776242822 ,  435 ,  248 ,  82.00609733428362 ) #little intersection right
True
>>> circleOverlap( 222 ,  183 ,  141.4213562373095 ,  233 ,  404 ,  88.36288813749809 ) #little intersection bottom
True
>>> circleOverlap( 234 ,  283 ,  180.13605968822566 ,  30 ,  281 ,  28.284271247461902 ) #little intersection left
True

>>> circleOverlap( 229 ,  166 ,  145.0 ,  231 ,  156 ,  67.0 )#Circle in circle
True

##############################################################################
"""
import math
from math import *

################## your code here ##############

def CircleCircle(x1: float,y1: float,r1: float,x2: float,y2: float,r2: float) -> bool:

    dist_1 = math.sqrt((x2-x1)**2 + (y2-y1)**2) #distance between centers of circles
    if (r1+r2 >= dist_1): #if sum of radii is greater than the dist_1 
        return True
    else:
        return False;


################## your code here ##############

    
def circleOverlap(x1: float,y1: float,r1: float,x2: float,y2: float,r2: float) -> bool:
    assert (r1 >= 0 and r2 >= 0)
    # postcondition: return true iff there exists x,y in both circular regions, including being on the edge

    MODE: str = '2021'  # set to 'test samples' or 'mine'
    
    if MODE =='2021':
        return CircleCircle(x1,y1,r1,x2,y2,r2)
    elif MODE =='test samples':
        from CircleSamples import circleOverlapSamples
# the line below only works in the QuaCS lab computers
#        from sample_answers.cs105.Intersect.Ci5rcleSamples import circleOverlapSamples
        answer: bool = circleOverlapSamples(x1,y1,r1,x2,y2,r2)
        return answer
    else:
        print('ERROR: You need to set MODE correctly in circleRectangleOverlap in circleRectangle.py')
        raise Exception

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!")
    else:
        print("Rats!")

if __name__ == "__main__": _test()
