from numpack import *

day1 = Numpack('1',1,[ [2,1,0,0],
                        [5,3,1,1],
                        [4,0,2,0],
                        [1,2,0,6]])
day2 = Numpack('2',1,[ [0,0,1,1],
                        [6,2,1,0],
                        [1,2,0,3],
                        [3,4,1,2]])
day3 = Numpack('3',1,[ [3,4,2,0],
                        [1,2,7,1],
                        [0,0,0,2],
                        [2,4,5,1]])

print('### Day1')
print(day1)

print('### Day2')
print(day2)

print('### Day1 + Day2')
result = day1.add(day2)
print(result)

###### Uncomment this to test overloading ########
print('### Day1 + Day2 Overloading')
result3 = day1 + day2
print(result3)
##################################################

print('### Day3')
print(day3)

print('### Day1 + Day2 + Day3')
result2 = result.add(day3)
print(result2)

###### Uncomment this to test get_zone_average ####
print('### Average_Zone(Day1)')
print(day1.get_zone_average())
print()

print('### Average_Zone(Day1 + Day2)')
print(result.get_zone_average())
print()

print('### Average_Zone(Day1 + Day2 + Day3)')
print(result2.get_zone_average())
##################################################

