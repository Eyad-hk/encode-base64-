import base64
while True:
    print("*"*65)
    print('Encryption pressure:(2')
    print('To decrypt:(1')
    nambr=input("        ?:")
    if nambr=='2':
        user=input("Enter the text to be encrypted")#has encode
        e = user.encode('utf-8')
        d = base64.b64encode(e)
        print(format(">>>>>>>>"),d)
    elif nambr=='1':
        cc = input("Enter the Hash to be decrypted:")#has decode
        x = base64.b64decode(cc)
        print(format(">>>>>>>>"),x)
    else:
        print("Error")
        break
