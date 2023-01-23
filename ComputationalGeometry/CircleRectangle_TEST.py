#Jack Greff -- Test Code ONLY (No help here)
"""
    Test to see if a circular area and a rectangular area overlap.
    The circle is defined by a center x and y, and a radius 
        and the rectangle by xmin, xmax, ymin, ymax
    The parameters are those seven values, in the order above:
        centerX,centerY,radius,xmin,xmax,ymin,ymax
        
some examples:

# An obvious overlap:
>>> circleRectangleOverlap(100,20,8, 80,120, 18,25)
True

# An obvious miss:
>>> circleRectangleOverlap(100,20,8, 180,220, 18,25)
False

(Note we can't have a circle with negative radius)

##############################################################################
#>>> circleRectangleOverlap( 278 ,  204 ,  51.62363799656123 ,  173 ,  400 ,  294 ,  346 )# circle over rect
False
>>> circleRectangleOverlap( 408 ,  343 ,  47.29693436154187 ,  165 ,  352 ,  308 ,  364 )# circle to the right of rect
False
>>> circleRectangleOverlap( 307 ,  415 ,  35.014282800023196 ,  232 ,  411 ,  321 ,  362 )# circle below rect
False
>>> circleRectangleOverlap( 134 ,  345 ,  86.03487664894976 ,  249 ,  435 ,  343 ,  383 )# circle to the left of rect
False

>>> circleRectangleOverlap( 297 ,  322 ,  57.584720195551874 ,  176 ,  420 ,  361 ,  420 )#circle in the top of rect
True
>>> circleRectangleOverlap( 453 ,  388 ,  60.0 ,  198 ,  396 ,  353 ,  420 )#circle in the right of rect
True
>>> circleRectangleOverlap( 289 ,  463 ,  59.64059020499378 ,  167 ,  451 ,  376 ,  421 )#circle in the bottom of rect
True
>>> circleRectangleOverlap( 172 ,  403 ,  10.198039027185569 ,  177 ,  441 ,  388 ,  435 )#circle in the left of rect
True

>>> circleRectangleOverlap( 239 ,  238 ,  7.280109889280518 ,  246 ,  331 ,  246 ,  318 )#top left corner miss
False
>>> circleRectangleOverlap( 390 ,  229 ,  42.95346318982906 ,  255 ,  340 ,  259 ,  323 )#top right corner miss
False
>>> circleRectangleOverlap( 376 ,  389 ,  36.89173349139343 ,  250 ,  344 ,  286 ,  344 )#bottom right corner miss
False
>>> circleRectangleOverlap( 242 ,  392 ,  21.400934559032695 ,  273 ,  395 ,  298 ,  369 )#bottom left corner miss
False
>>> circleRectangleOverlap( 258 ,  301 ,  25.80697580112788 ,  258 ,  418 ,  312 ,  378 )#top left corner make
True
>>> circleRectangleOverlap( 412 ,  308 ,  37.0 ,  273 ,  392 ,  322 ,  363 )#top right corner make
True
>>> circleRectangleOverlap( 373 ,  378 ,  19.313207915827967 ,  254 ,  364 ,  339 ,  369 )#bottom right corner miss
True
>>> circleRectangleOverlap( 230 ,  388 ,  25.80697580112788 ,  221 ,  367 ,  341 ,  376 )#bottom left corner miss
True
>>> circleRectangleOverlap( 241 ,  327 ,  228.89517251353294 ,  143 ,  420 ,  366 ,  428 )#rect in circle
True
>>> circleRectangleOverlap( 329 ,  370 ,  11.0 ,  174 ,  445 ,  346 ,  385 )#circle in rect
True

Testing: >>> circleRectangleOverlap( 265 ,  239 ,  86.53900854527974 ,  120 ,  437 ,  248 ,  297 )#tall skinny rect with intersection
True
Testing: >>> circleRectangleOverlap( 212 ,  230 ,  113.1591799192624 ,  291 ,  319 ,  115 ,  410 )#wide skinny rect with intersection
True
##############################################################################


"""

from math import *
from Logic import *
  
  
def circleRectangleOverlap(centerX: float,centerY: float,radius: float,xmin: float,xmax: float,ymin: float,ymax: float) -> bool:
    precondition(radius >= 0 and xmin <= xmax and ymin <= ymax)
    # postcondition: return true iff there exists x, y in both shapes...
    MODE:str = 'test samples'  # set to 'test samples', 'answer key', 'code review', or 'mine'
    
    if MODE=='mine':
        ####################### When writing circle-rectangle, write your code below #############
        # here's an example circle-rectangle algorithm that's a totally unsound idea but often works :-)
        if radius > 150:    # if the circle is Big
            return True        #  then it probably overlaps
        elif xmax-xmin > 150:     # also, if the rectangle is wide
            return True        #  then it probably overlaps
        elif ymax-ymin > 150:     # also, if the rectangle is tall
            return True        #  then it probably overlaps
        else:            # Otherwise, they're probably both small, so
            return False    #  let's hope they don't overlap
        ####################### When writing circle-rectangle, write your code above #############
    elif MODE=='code review':
        
        try:
            import CircleRectangleToReview as review
        except:
            print("Your CircleRectangleToReview.py file does not seem to be ready yet")
            return True
            
        return review.circleRectangleOverlap(centerX,centerY,radius,xmin,xmax,ymin,ymax)
        
    elif MODE=='answer key':
        return keyCircleRectangleOverlap(centerX,centerY,radius,xmin,xmax,ymin,ymax)
    elif MODE=='test samples':
        try:
            from CircleRectangleSamples import circleRectangleOverlapSamples
# the line below only works in the QuaCS lab computers
#           from sample_answers.cs105.Intersect.CircleRectangleSamples import circleRectangleOverlapSamples
            try:
                answer: bool = circleRectangleOverlapSamples(centerX,centerY,radius,xmin,xmax,ymin,ymax)
                return answer
            except:
                print("A sample solution had an error or failed a precondition.")
                print("This should have been caught by the lab files already, so please report it.")
                return True
        except:
            print("Hmmmm... can't find sample answers. This shouldn't happen on the CS teaching lab computers")
            print(" If you are running this program on another computer, you'll have to wait to check")
            print(" your test suite against the sample answers when you're back in the lab.")
            print(" (Remember to Team->Commit on your computer and Team->Update in the lab.)")
    
            return True  # Well, sometimes this is the right answer!            
    else:
        print('ERROR: You need to set MODE correctly in circleRectangleOverlap in circleRectangle.py')
        raise Exception
        return True

def keyCircleRectangleOverlap(centerX: float, centerY: float, radius: float, xmin: float, xmax: float, ymin: float, ymax: float) -> bool:

    return True  # The key will be released later, above this line

# The following gets the "doctest" system to check test cases in the documentation comments
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"))
    else:
        print("Rats!")

if __name__ == "__main__": _test()
