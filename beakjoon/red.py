import sys;

input = sys.stdin.readline

star = int(input())

if(star >= 620 and star <= 780):
    print("Red")
elif(star >= 590):
    print("Orange")
elif(star >= 570):
    print("Yellow")
elif(star >= 495):
    print("Green")
elif(star >= 450):
    print("Blue")
elif(star >= 425):
    print("Indigo")
elif(star >= 380):
    print("Violet")