from time import sleep
some_variable = 42

def reader():
    other_var = 10
    print("[reader] somevar: ", some_variable)
    other_var +=1
    print("[reader] othervar: ", other_var)
    
def writer():
    global some_variable
    print("[writer] somevar: ", some_variable)
    some_variable += 1
    print("[writer (2) ] somvar: ", some_variable)
    

reader()
sleep(0.5)
writer()
sleep(0.5)
reader()
sleep(0.5)
writer()
