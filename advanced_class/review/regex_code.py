import re

a = ['AKSJH', "09133764536", "asgdjha 09133764536 asdas", "ajhsdg 09133764536", "fs 09133764536 sdfg"]

def check_real_phone(numbers):
    real_numbers = []
    for number in numbers:
        print(number)
        if number[0:2] == "09":
            real_numbers.append(number)
            print(real_numbers)
    return real_numbers

def check_window(s):
    if len(s) < 11:
        return False
    
    numbers = []
    for i in range(len(s)): # window roller
        n = s[i : i + 11]

        if len(n) < 11:
            continue
        
        if n.isdigit():
            numbers.append(n)
    return check_real_phone(numbers)

# without re

patt = "09\d{9}"

for i in a:
    nums = check_window(i)
    print(nums)


# with regex
patt = "09\d{9}"
for i in a:
    m = re.findall(patt, i)
  
