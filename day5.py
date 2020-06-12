'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 

For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

'''
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
	'''https://stackoverflow.com/questions/52481607/dont-understand-the-inner-function-in-python 
	
	learning : 
	So nested functions can have access to names from the surrounding scope via closures. 
	(Side note: it's not the value that's stored in a closure, 
	it's the variable. The variable can change over time,
	and just like other variables accessing the name later will reflect the new value;
	if spam was changed later on, calling bar() again would return the new value).


	Next up are cdr() and car(), which will return either the first or last element of a pair. 

	If cons(a, b) produces pair(f) returning f(a, b), then cdr() and car() must each create a function to pass to pair() that'll extract either a or b.
	So create a nested function in each, and have cdr() and car() call pair() with that function.
	The nested function does the work of picking either a or b, and returns that value. 
	Then return the result of the call to the outside world:

	'''
	def return_first(a,b):
		return a
	return pair(return_first)

def cdr(pair):
	def return_last(a,b):
		return b
	return pair(return_last)

print(car(cons(3,4)))
print(cdr(cons(3,4)))
