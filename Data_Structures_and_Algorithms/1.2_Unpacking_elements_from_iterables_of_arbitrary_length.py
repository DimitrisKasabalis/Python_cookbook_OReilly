record = ('Dave', 'deva@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print(name)
print(email)
print(phone_numbers)


records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)
    
def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
        

# Star unpacking can also be useful when combined with certain kinds of string processing operations such as splitting.
line = 'nobody:*:-2:-2:Uprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# Unpack and trhow values away
record = ('ACNE', 50, 123,45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

# Split a list in head and tail
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


sum(items)