"""E

Here are a few more things about arithmetic and doctest in Python. You may be
able to complete one or more complete courses about programming without needing
to know anything beyond the first examples of "**" and "import", but there are
more details given here in case you are curious or having trouble with something
like rounding errors, and needing to understand what's going on and why.



==============   exponentiation   ==============

Raising a number to a power can be done via the ** operation, e.g., 3**5 means 3
to the 5th power:

>>> 3**5
243

Or, if you like, some more obvious examples:

>>> 10**3
1000
>>> 10**-3
0.001

Note that numbers with magnitudes very close to zero or very far from zero will
be represented with "scientific notation", though the notation may be
unfamiliar: 6e30 means 6 times 10 to the 30th power:

>>> 4 * 3 * 10**15 / (2*10**-15)
6e+30

This works for input as well as output:

>>> 4*3e15 / 2e-15
6e+30




==============   importing math   ==============

Python's "import" statement can be used to access additional functions that are
not built into python, for example, logarithms and trigonometry:

>>> import math
>>> math.log10(1000)
3.0
>>> math.log2(2**12)
12.0
>>> math.log2(10)
3.321928094887362
>>> math.log(10)   # natural log, base e (2.718...)
2.302585092994046

>>> math.e
2.718281828459045
>>> math.log(math.e)
1.0

>>> math.sin(math.pi/2)   # sine of an angle given in radians
1.0

>>> math.isclose(0.1, 0.1000000001)
True
>>> math.isclose(0.1, 0.10000001)
False

More information about Python's math library can be found in the documentation
on python.org, e.g., https://docs.python.org/3/library/math.html



============== non-integer values ==============

When we are writing out rational numbers by hand, there may be several choices,
e.g., 1/4, 2/8, -1/-4, and 0.25 are all different ways of representing (writing
down) the same number ("zero point two four nine-repeating" is another way).

Python, like many languages, provide for quick manipulation of _approximations_
of rational/real numbers, by using the "binary floating-point hardware" that is
included on most modern microprocessors. So, 1/4 is essentially always written
in a way that is analogous to the 0.25 above.

>>> 1/4
0.25


The phrase "floating point" means that we keep a standard number of "significant
digits", even if the number is very close to, or very far from, zero. So, we can
represent, for example, 1/4 * 10**40 and 1/2 * 10**-40 without any trouble, even
without keeping 80 digits of each answer:

>>> 1/4 * 10**40
2.5e+39
>>> 1/2 * 10**-40
5e-41


But, to represent their sum, we would need about 80 digits of the answer, and
information will be lost here:

>>> (1/4 * 10**40 + 1/2 * 10**-40)
2.5e+39

Mathematically, the following is _not_ zero, but look:

>>> (1/4 * 10**40 + 1/2 * 10**-40) - 1/4 * 10**40
0.0


As you may recall from the time when you first learned to write things like 1/4
as "decimals", some rational numbers have a finite exact representation in this
form (like 1/2, 1/4, 1/5, and 1/10), but others, like 1/3 and 1/7, do not.
Writing 0.3333... with any finite number of 3's gives an _approximation_ of 1/3,
but, of course, if we multiply 0.3333 by 3, we get 0.9999 rather than 1.

>>> 1/3
0.3333333333333333

As with many pocket calculators, Python secretly computes more digits than it
prints, so that you don't immediately notice any error if you compute 1/3 * 3.
Imaginine that Python represents 1/3 with a "0." followed by eightteen 3's,
i.e., with the numerals  0.333333333333333333, but only shows you the first
_sixteen_ of them, i.e., 0.3333333333333333.  Then, when we multiply by 3, the
_eightteen_ numerals would be 0.999999999999999999, which gets rounded to 1.0:

>>> 1/3 * 3
1.0

We can reveal the limits, though, by subtracting some of those 3's after the
decimal point, to reveal that eventually our representation runs out of 3's:

>>> (1/3 - 0.3333)  # we expect 3.333333333333333e-05, but look at the end!
3.333333333332966e-05

This can cause problems when comparing floating-point numbers with "=="
 --->  So it is probably best never to use == on floating-point numbers  <--
but instead use math.isclose:

>>> 1 - 1/3 - 1/3 - 1/3 == 0
False
>>> 1 - 1/3 - 1/3  ==  1/3
False
>>> math.isclose(1 - 1/3 - 1/3, 1/3)
True

Unfortunately, sometimes "isclose" is too strict, especially near zero,
and we need to tell it to use a diffent "absolute tolerance" (abs_tol):

>>> math.isclose(1 - 1/3 - 1/3 - 1/3, 0.0)
False
>>> math.isclose(1 - 1/3 - 1/3 - 1/3, 0.0, abs_tol=1e-8) # check 8 digits past the "0."
True


Floating-point hardware is limited not only in its ability to account for
small differences in value, but also in the total range of numbers it can
represent. The limit is quite large, so you can comput things like 3.0 to the
600th power, but eventually you will get _either_ an "Overflow Error" or a
special value "inf" meaning "a number too big to represent":

>>> 3.0**600
1.873927703884794e+286

>>> 3.0**700
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OverflowError: (34, 'Numerical result out of range')

>>> 3.0**600 * 3.0**100
inf


If you want to know how big numbers can get without being "too big" on your
computer, here's how to do that:

>>> import sys
>>> sys.float_info.max    # biggest number we can record as a "float"
1.7976931348623157e+308

>>> sys.float_info.min    # smallest _positive_ float we can record
2.2250738585072014e-308

>>> -sys.float_info.max   # usually this is the smallest (most negative) float
-1.7976931348623157e+308


Note that "max" can provide good "starting values" if you are going through a
bunch of numbers and find the smallest or largest, and need a starting point
as (as is the case with a "for" loop doing an accumulation/selection, if
you're familiar with that).

In other words, just as we can add a "0.0+" without changing a floating-point
result, or a "1.0*", we can add a "min(sys.float_info.max, " or
"max(-sys.float_info.max, ". The following should be true for any value of x:

>>> x=6.022e+23
>>> 1.0*x
6.022e+23
>>> 1.0*x == x
True
>>> 0.0+x == x
True

>>> import sys
>>> min(sys.float_info.max, x) == x
True
>>> max(-sys.float_info.max, x) == x
True


One thing that may be surprising is that the _binary_ floating point used in the
computer doesn't have an exact finite representation for all the numbers that
are "terminating" decimals. Python has exact representations for negative powers
of two, e.g., 1/2, 1/4, 1/8, etc. (out to a limit), as well as integer multiples
thereof, e.g., 3/4, 5/8, etc., but _not_ for 1/5 and 1/10. Look, this should be 0!

>>> 1/10 - 1/100 - 1/100 - 1/100 - 1/100 - 1/100 - 1/100 - 1/100 - 1/100 - 1/100 - 1/100
1.0408340855860843e-17

>>> 1/10 == (1/100 + 1/100 + 1/100 + 1/100 + 1/100 + 1/100 + 1/100 + 1/100 + 1/100 + 1/100)
False

>>> math.isclose(1/10, 10*1/100)
True


Perhaps unsurprisingly, 1/3 must be approximated _both_ in binary floating point
and in decimal form (though, not if you write things in base three).


Note that precision and range limitations impact floating-point
representations of values, but not integers, which can get bigger and bigger
as long as the computer has memory to record all the digits and time to finish
the calculation:

>>> 3**100
515377520732011331036461129765621272702107522001
>>> 3**200
265613988875874769338781322035779626829233452653394495974574961739092490901302182994384699044001
>>> 3**300
136891479058588375991326027382088315966463695625337436471480190078368997177499076593800206155688941388250484440597994042813512732765695774566001
>>> 3**400
70550791086553325712464271575934796216507949612787315762871223209262085551582934156579298529447134158154952334825355911866929793071824566694145084454535257027960285323760313192443283334088001
>>> 3**500
36360291795869936842385267079543319118023385026001623040346035832580600191583895484198508262979388783308179702534403855752855931517013066142992430916562025780021771247847643450125342836565813209972590371590152578728008385990139795377610001
>>> 3**600
18739277038847939886754019920358123424308469030992781557966909983211910963157763678726120154469030856807730587971859910379069087693119051085139566217370635083384943613868029545256897117998608156843699465093293765833141309526696357142600866935689483770877815014461194837692223879905132001
>>> 3**700
9657802140591758043812442031522928437371194636776843099838260055342219733688083412928987321682880332396927287242805644548901834234972280564072880735127568242460394336247761481999342991210220561304479523441956128812808859393388776484808811910915541232693035534590226711458043242074211993816993921587180335757972232760635320184916654001
>>> 3**800
4977414122938492192881464029729961679802517669640314331069754317413863193300588672960378941038799444233797200629740876278809425638436874294137213623651683084623545115805694417048191856898335577690331770093271154442020977681305435856437590481321498962517248672813060123683011804992094505499691756946329466238029256908317387659245893361869285485179777099016847012698558309358412176001
>>> 3**900
2565247350336538756158496029089399488342665074148586598191338322780709497564665831661451831933344895389619261270654023564506356253988331756965350599112541694997814930496466779507741289971109725554444907690651495042175769213189807845030495164348486442317181026874535610643331227069289920564720047434146322527875184136842319748464686354974891958289182069083961091717150518771893164820785391432554475730404353788016234328048391698001
>>> 3**1000
1322070819480806636890455259752144365965422032752148167664920368226828597346704899540778313850608061963909777696872582355950954582100618911865342725257953674027620225198320803878014774228964841274390400117588618041128947815623094438061566173054086674490506178125480344405547054397038895817465368254916136220830268563778582290228416398307887896918556404084898937609373242171846359938695516765018940588109060426089671438864102814350385648747165832010614366132173102768902855220001

Python doesn't "mind" going to larger numbers, but it makes this file hard to read, e.g. 3**10000 is 4772 digits long, so we'll only print the number of digits (i.e., the log base 10):

>>> math.log10(3**10000)
4771.212547196625
>>> math.log10(3**10000)
4771.212547196625
>>> math.log10(3**100000)
47712.12547196625
>>> math.log10(3**1000000)
477121.2547196625

You can start Python and continute this process, but not that it will keep
slowing down ... floating-point gives us approximate answers quickly, rather
than precise answers eventually.



======== doctest and non-integer values =========

If we're only concered about those extra decimal places during _doctest_, we can
tell doctest to ignore some of the actual answer: if we add the text

    doctest: +ellipsis

as a comment on a test, that tells doctest to accept anything else on that line
as a match for the "..." (this mark is called ellipsis):

>>> math.e    # doctest: +ELLIPSIS
2.718...

>>> 1+(1/3 - 0.3333)   # doctest: +ELLIPSIS
1.000033333...

"""




# If we had written some Python software ourselves, it would usually go here.


#############################################################################################
# The following gets the DocTest system to check test cases in the documentation comments.  #
# In this course, you won't need to modify the stuff below, or even understand the details. #
#############################################################################################

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print(("Congratulations! You have passed all "+str(result[1])+" tests"))
    else:
        print("Rats!")
