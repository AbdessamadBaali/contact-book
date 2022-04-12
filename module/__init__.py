import re 
txt = "212641336504" 
phonecheck = re.findall('^[+]', txt)

print(phonecheck) 