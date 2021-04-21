def nameflipper(name):
    e=name.split()
    e=list(reversed(e))

    x=""
    y=""
    u=name
    z=""
    x=x+e[0]
    y=y+e[1]
    z=x+", "+y
    print (z)
    if u=="Bill Slater":
        if z=="Slater, Bill":
            print("Bill Slater Passed")
        else:
            print("Bill Slater Failed")
    elif u=="Michael Green":
        if z=="Green, Michael":
            print("Michael Green Passed")
        else:
            print("Michael Green Failed")
    elif u=="J Graff":
        if z=="Graff, J":
            print("J Graff Passed")
        else:
            print("J Graff Failed")
def main():
    a="Bill Slater"
    b="Michael Green"
    c="J Graff"
    nameflipper(a)
    nameflipper(b)
    nameflipper(c)

main()
