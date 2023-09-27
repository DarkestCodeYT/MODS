import subprocess, pyautogui, requests, time, os
path = os.path.join(os.path.expanduser('~'),'AppData','Roaming','.minecraft')
print(f'Default Path: {path}')
path = input('What path is your minecraft')
if path == '':
  path = path
if os.path.exists(os.path.join(os.getcwd(),'locationtoclick.txt')):
  #
urls = input('url: ')
if urls = '':
  urls = requests.get('https://raw.githubusercontent.com/DarkestCodeYT/MODS/main/server/mods.txt').text
elif ',' in urls:
  urls = urls.split(',')
for filename in os.listdir(os.path.join(path,'mods')):
  if os.path.isfile(os.path.join(os.path.join(path,'mods'), filename)):
    os.remove(os.path.join(os.path.join(path,'mods'), filename))
for url in urls:
  response = requests.get(url)
  with open(os.path.join(path,url.split(r'/')[-1]),'wb') as file:
    file.write(response.content)
# run minecraft
time.sleep(10)
subprocess.Popen(os.path.join(path,'MinecraftLauncher.exe'))
time.sleep(10)
pyautogui.click(x=mouse[0], y=mouse[1])
