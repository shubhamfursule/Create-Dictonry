dicts={}
while True:
    try:
        key,value=map(str,input().split(","))        
    except:
        print("Please Enter proper way")
        
    else:
        if key=="STOP":
            break
        else:
            try:
                dicts.update({key:int(value)}) 
            except:
                print("please Enter proper type!")

print(dicts)               

