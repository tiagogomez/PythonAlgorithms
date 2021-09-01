# Dictionaries

voted = dict()

def checkVoter(name):
    if voted.get(name):
        print("kick him")
    else:
        voted[name] = True
        print("let him vote")

checkVoter("tom")
checkVoter("tim")
checkVoter("tim")