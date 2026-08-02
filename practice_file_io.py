with open("data.txt", "a") as f:
    f.write("Hello, this is a test\n")

with open("data.txt","r") as f:
    x=f.read()
    print(x)