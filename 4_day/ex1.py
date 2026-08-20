# ex 1
a = 'thirty'
b = 'Days'
c = 'Python'
d = '{} {} {}'.format(a, b, c)
print(d)

# ex 2
a = 'coding'
b = 'for'
c = 'all'
d = "%s %s %s" %(a, b, c)
print(d)

# ex 3
company = 'Coding for all'
print(company)

# ex 4
print(len(company))

# ex 5
print(company.upper())

# ex 6
print(company.lower())

# ex 7
print(company.title())
print(company.swapcase())
print(company.title())

# ex 8
print(company[6:])

# ex 9
print(company.find('Coding'))

# ex 10
print(company.replace('Coding', 'Python'))

# ex 11
print(company.split())

# ex 12
kompani = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(kompani.split(","))

# ex 13
print(company[0])

# ex 14
print(company[len(company) - 1])

# ex 15
print(company[10])

# ex 16
c = 'Coding For All People'
p = 'Python For All'

# ex 17
print(c.index('C'))

# ex 18
print(p.index('F'))

# ex 19
print(c.index('l'))

# ex 20
a =  'You cannot end a sentence with because because because is a conjucion'
print(a.index('because'))

# ex 21
print(a.rindex('because'))

# ex 22
print(a.split('because'))

# ex 23
print(c.startswith('Coding'))

# ex 24
print(c.endswith('coding'))

# ex 25
d = '   Coding For All   '
print(d.strip())

# ex 26
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# ex 27
a = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(a))

# ex 28
print("I am enjoying the challenge. \n I wonder what is next!")

# ex 29
print('''Name\tAge\tCountry\tCity\nAnna\t20\tFinland\tRome ''')

# ex 30
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {}'.format(a, b, a/b))
print('{} % {} = {}'.format(a, b, a%b))
print('{} // {} = {}'.format(a, b, a//b))
print('{} ** {} = {}'.format(a, b, a**b))
