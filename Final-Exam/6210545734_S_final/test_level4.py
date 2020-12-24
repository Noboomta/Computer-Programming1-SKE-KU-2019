from package import *
from office import *

############## Level 4 ##################

def find_package(office_list, package_id):
    # fill in your code
    pass

def print_found_package(package):
    # fill in your code
    pass

##########################################

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
num_packages += 1
p6 = Package(num_packages,101,201)
num_packages += 1
p7 = Package(num_packages,201,102)

o101 = Office(101)
o102 = Office(102)
o201 = Office(201)

############## Level 4 ##################
office_list = []
office_list.append(o101)
office_list.append(o102)
office_list.append(o201)
##########################################

print('----------------------')

#print('### Office 101 wants to mail out 2 packages to Office 102')
#print('### Office 101 wants to mail out 1 packages to Office 201')
o101.add_package_to_mailout(p1)
o101.add_package_to_mailout(p2)
o101.add_package_to_mailout(p6)
print(o101)

print('----------------------')

#print('### Office 201 wants to mail out 3 packages to Office 101')
#print('### Office 201 wants to mail out 1 packages to Office 102')
o201.add_package_to_mailout(p3)
o201.add_package_to_mailout(p4)
o201.add_package_to_mailout(p5)
o201.add_package_to_mailout(p7)
print(o201)

############## Level 4 ##################
print('======== Level 4 ==========')

print('@@@ Look for package id 2')
found_package = find_package(office_list, 2)
print_found_package(found_package)
print()
print('@@@ Look for package id 10')
found_package = find_package(office_list, 10)
print_found_package(found_package)

print('===========================')
##########################################

print('----------------------')

#print('### 2 packages from Office 101 are traveling to Office 102')
o101.transfer(o102)
print(o101)

print('----------------------')

############## Level 4 ##################
print('======== Level 4 ==========')

print('@@@ Look for package id 2')
found_package = find_package(office_list, 2)
print_found_package(found_package)

print('===========================')
##########################################


#print('### 2 packages from Office 101 are delivered at Office 102')
o101.deliver2(o102)
print(o102)
print(o101)

print('----------------------')

############## Level 4 ##################
print('======== Level 4 ==========')

print('@@@ Look for package id 2')
found_package = find_package(office_list, 2)
print_found_package(found_package)

print('===========================')
##########################################

print('----------------------')

#print('### 1 package from Office 101 are traveling to Office 201')
o101.transfer(o201)
print(o101)

print('----------------------')


#print('### 1 package from Office 101 is delivered at Office 201')
o101.deliver2(o201)
print(o201)
print(o101)

############## Level 4 ##################
print('======== Level 4 ==========')

print('@@@ Look for package id 4')
found_package = find_package(office_list, 4)
print_found_package(found_package)

print('===========================')
##########################################

print('----------------------')

#print('### 3 packages from Office 201 are traveling to Office 101')
o201.transfer(o101)
print(o201)

############## Level 4 ##################
print('======== Level 4 ==========')

print('@@@ Look for package id 4')
found_package = find_package(office_list, 4)
print_found_package(found_package)

print('===========================')
##########################################

print('----------------------')

#print('### 3 packages from Office 201 are delivered at Office 101')
o201.deliver2(o101)
print(o101)
print(o201)

############## Level 4 ##################
print('======== Level 4 ==========')

print('@@@ Look for package id 4')
found_package = find_package(office_list, 4)
print_found_package(found_package)

print('===========================')
##########################################

print('----------------------')

#print('### 1 package from Office 201 are traveling to Office 102')
o201.transfer(o102)
print(o201)

print('----------------------')

#print('### 1 package from Office 201 is delivered at Office 102')
o201.deliver2(o102)
print(o102)
print(o201)

print('----------------------')

print('### After mail delivery')
print(o101)
print(o102)
print(o201)

############## Level 4 ##################
print('======== Level 4 ==========')

print('@@@ Look for package id 5')
found_package = find_package(office_list, 5)
print_found_package(found_package)

print('===========================')
##########################################

print('----------------------')

print('### Clear delivered packages')
o101.clear()
o102.clear()
o201.clear()
print(o101)
print(o102)
print(o201)

############## Level 4 ##################
print('======== Level 4 ==========')

print('@@@ Look for package id 5')
found_package = find_package(office_list, 5)
print_found_package(found_package)

print('===========================')
##########################################

print('----------------------')

