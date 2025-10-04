OS = ["Ocelot", "Serval", "Lynx"]
X, Y = input().split()

if OS.index(X) >= OS.index(Y):
    print("Yes")
else:
    print("No")