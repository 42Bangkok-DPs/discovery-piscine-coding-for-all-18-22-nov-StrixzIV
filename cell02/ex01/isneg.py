#!/Users/jirayukaewsing/miniforge3/envs/conda310-venv/bin/python

number = int(input())

if number < 0:
    print("This number is negative.")
    
elif number == 0:
    print("This number is both positive and negative.")

elif number > 0:
    print("This number is positive.")