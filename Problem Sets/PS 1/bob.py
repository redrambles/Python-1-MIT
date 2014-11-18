s = 'azcbobobegghakl'
count = 0

while len(s) >= 3:
    
    if s[0] == 'b' and s[1] == 'o' and s[2] == 'b':
        count += 1
    s = s[1:]        

print count