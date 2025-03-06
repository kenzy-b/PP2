import os
def checker(path):
    if os.path.exists(path):
        print(os.path.basename(path))
        print(os.path.dirname(path))
    else:
        print("Doesn'n exists")
        