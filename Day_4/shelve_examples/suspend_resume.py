import shelve

state = shelve.open("state.dat")

count = state.setdefault("count", 0)

for i in range(count, count+10): 
    print "Counting", i
    state["count"] = i

state.close()



