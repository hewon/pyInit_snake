from pip._vendor.distlib.compat import raw_input
import django


for x in range(2, 10):
    print("------- [" + str(x) + "------")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("---------------------")


print('구구단')

base = input("몇단????") 
i= 2

while i<= 9:
    print( int(base) * i  ) 
    i += 1
    

print("version" + django.get_version() )
