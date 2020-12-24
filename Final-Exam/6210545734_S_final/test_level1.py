from package import *
from office import Office


num_packages = 1
p1 = Package(num_packages,101,102)
num_packages += 1
p2 = Package(num_packages,101,102)
num_packages += 1
p3 = Package(num_packages,201,101)
num_packages += 1
p4 = Package(num_packages,201,101)
num_packages += 1
p5 = Package(num_packages,201,101)

print('### Printing some packages')
print(p1)
print(p2)
print(p5)

print('----------------------')

o101 = Office(101)
o102 = Office(102)
o201 = Office(201)


print('### Office 101 wants to mail out 2 packages to Office 102')
o101.add_package_to_mailout(p1)
o101.add_package_to_mailout(p2)
print(o101)

print('----------------------')

print('### Office 201 wants to mail out 3 packages to Office 101')
o201.add_package_to_mailout(p3)
o201.add_package_to_mailout(p4)
o201.add_package_to_mailout(p5)
print(o201)

print('----------------------')

print('### 2 packages from Office 101 are traveling to Office 102')
o101.transfer(o102)
print(o101)

print('----------------------')

print('### 2 packages from Office 101 are delivered at Office 102')
o101.deliver(o102)
print(o102)
print(o101)

print('----------------------')

print('### 3 packages from Office 201 are traveling to Office 101')
o201.transfer(o101)
print(o201)

print('----------------------')

print('### 3 packages from Office 201 are delivered at Office 101')
o201.deliver(o101)
print(o101)
print(o201)

print('----------------------')

print('### After mail delivery')
print(o101)
print(o102)
print(o201)

print('----------------------')

print('### Clear delivered packages')
o101.clear()
o102.clear()
print(o101)
print(o102)

print('----------------------')

