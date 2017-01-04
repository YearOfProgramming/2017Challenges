text = "This is a test."
txet = ""
for i in xrange(len(text)):
    txet = txet + text[len(text)-i-1]
print(txet)
