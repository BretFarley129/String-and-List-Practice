print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
words = "It's thanksgiving day. It's my birthday too!"
print words.find("day")
print words.replace("day", "month")

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]

z = []
z.append(y[0])
z.append(y[len(y)-1])
print z

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
print len(x)

def split_list(aList):
    half = len(aList)/2
    return aList[:half], aList[half:]

a, b = split_list(x)
print a
print b