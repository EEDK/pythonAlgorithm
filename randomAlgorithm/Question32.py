b = ord('Z')
while b >= ord('A'):
    a = ord('A')
    while a <= b :
        print("%2c"%(a), end ="")
        a += 1;
    print()
    b -= 1;

## 이번엔 ord에 관해서 배워봤다.