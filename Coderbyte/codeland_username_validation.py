
def CodelandUsernameValidation(strParam):
  import re

  if (len(strParam) > 25 or len(strParam) < 4):
    return "false"
  elif (not strParam[0].isalpha()):
    return "false"
  elif (strParam[len(strParam)-1] == '_'):
    return "false"
  elif not re.match('^[a-zA-Z0-9_]+$', strParam):
    return "false"
  else:
    return "true"

# keep this function call here 
CodelandUsernameValidation("123aabc_")



def username(rk):
    import re
    if len(rk)> 25 or len(rk) <4:
        return "Flase"
    elif ( not rk[0].isalpha()):
        return "Flase"
    elif (rk[len(rk)-1] =="_"):
        return "Flase"
    elif not re.match('^[a-zA-Z0-9_]+$',rk):
        return "Flase"
    else:
        return "True"
username("__1234")
