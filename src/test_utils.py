import hfst
# load a transducer from the ones listed above
transducer = hfst.HfstInputStream('c:/Users/user/Compling/apertium-evn-master/evn.automorf.hfst').read()

# get the result for a wordform:
result = transducer.lookup("хороки")
print(result)