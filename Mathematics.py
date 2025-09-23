import math 

operations = {
    "plus":"+",
    "minus":"-",
    "multipy":"*",
    "into":"*",
    "x":"*",
    "divide":"/",
    "divided":"/",
    "floor division":"//",
    "mod":"%",
    "modulus":"%",
    "square":"**2",
    "power":"**",
    "sr":"**1/"
}


def offline(command):
    command = command.split()
  
    data = ""
    i=0
    while i<len(command):
        if(i+3 < len(command) and command[i].strip() =='square' and command[i+1].strip() =='root' and command[i+2].strip()=='of' and command[i+3].strip().isdigit()):
            data += f"math.sqrt({command[i+3].strip()})"
            i=i+3
        else:
            data+=operations.get(command[i].strip() ,  command[i].strip() )  

        i=i+1

    try:
        result = eval(data)
    except Exception as e:
        return("Error recognising the values , please try again")
            
    return("result is : " + str(result))