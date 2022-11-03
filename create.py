import os
print('Введите дефолтное имя файла:')
dname = input()
print('Type Register Addr for all files')
dip = input()
print('Register Pswd')
dpwd = input()

print("Now let's create files")

while(True):
    i = 1
    print(f"Info for {i} file:")
    print('Type second part of name:')
    dname2 = input()
    
    print('Type Phone Number, Display Name, Sip Name:')
    dsip = input()

    path = dname + dname2 + ".cfg"
    file = open(path, "w")
    file.write(f'<<VOIP CONFIG FILE>>Version:2.4.7.6\n        <SIP CONFIG MODULE>\n        --SIP Line List--  :\n        SIP1 Phone Number  :{dsip}\n        SIP1 Display Name  :{dsip}\n        SIP1 Sip Name      :{dsip}\n        SIP1 Register Addr :{dip}\n        SIP1 Register User :{dsip}\n        SIP1 Register Pswd :{dpwd}\n        SIP1 Enable Reg    :1\n        SIP1 DTMF Mode     :2\n        SIP1 VoiceCodecMap :G711A\n        SIP2 line attachmen:1\n        <PHONE CONFIG MODULE>\n\t<DSSKEY CONFIG MODULE>\n\t--Dsskey Config1--:\n\tFkey1 Type               :1\n\tFkey1 Value              :165@1/f\n\tFkey1 Title              :\n\tFkey1 ICON               :Green\n\n       <<END OF FILE>>')
    i = i + 1
    file.close
    print("One more? y/n")
    stop = input()
    if(stop == 'n'): break