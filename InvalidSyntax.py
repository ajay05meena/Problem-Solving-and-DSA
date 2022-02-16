def match(ps):
    ps=list(ps)
    temp=[]
    dictt={"{":"}","(":")","[":"]"}
    for x in ps:
        if x in dictt.keys():
            temp.append(x)
        if x in dictt.values():
            try:
                t=temp.pop()
                if(dictt[t]!=x):
                    return False    
            except:
                return False           
    if(len(temp)==0):
        return True
    else:
        return False    


if __name__ == '__main__':
    testCases = ["{{}}", "{{{}}", "{{{{}}}","{{{}{}}}",  "}{","([][{({}){}}])",")[{({}){}}]())","([{})]"]
    results =   [True  ,   False,     False,      True, False,             True,           False,   False]
    for i in range(len(testCases)):
        if match(testCases[i]) == results[i]:
            print("Test Succeed ",i)
        else:
            print("Test Failed ", i)