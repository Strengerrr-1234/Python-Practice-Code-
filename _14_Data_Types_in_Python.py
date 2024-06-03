a = 5
print(a,type(a))

a = 5.5
print(a,type(a))

a = 2+5j
print(a,type(a))

# s = 'helo'
# s = "heloo@34"
s = ''' hello
        welcom back to system!
        you are hack   
    '''
print(type(s))

# --- list
l = [10,'ws',5.5]
print(l,type(l))

l[2]=10
print(l,type(l))


# -- tuple
t = (10,20,'Hello')
print(t,type(t))
t = (10)
print(t,type(t))


# -- dictionary
d = {
    'course_name': 'python',
    'course_duration':'2 Month'
}
print(d['course_name'])
print(d,type(d))

# --- set

my_set = {1,2,3}
print(my_set,type(my_set))