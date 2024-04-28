def check(password):
    accept=True
    message = ""
    if len( password)<8 :
        message="password must be more then 8 letter"
        return message, accept= False ; # type: ignore
    
    has_degit=False
    for char in  password:
        if char.isdigit():
            has_degit=True
            break


        if  not has_degit:
             message ="password must contain number"
             accept=False
    return message , accept
           
         
            
