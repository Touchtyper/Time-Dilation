
c = 8.9875518e+16
#Speed of light squared
t = int(input("Please enter the time interval for the observer (s):"))
v = int(input("Enter the velocity of moving object relative to you(m/s):"))
vf = v*v
half = (1-vf/c)**(0.5)
yes = t/half

print yes


