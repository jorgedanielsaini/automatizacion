import pyautogui, time, os, webbrowser, pyperclip

print("Iniciando sistemas")

urls = ["https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox", "https://web.whatsapp.com/"]
aux = 0

os.startfile("C:\Program Files\Fortinet\FortiClient\FortiClient.exe")
time.sleep(3)
pyautogui.moveTo(599,482)
pyautogui.click()
pyperclip.copy('@')
pyautogui.hotkey('ctrl', 'v')
pyautogui.write("lioymaite", interval=0.8)
time.sleep(1)
pyautogui.press("enter")
time.sleep(4)
pyautogui.moveTo(1008,26)
pyautogui.click()
pyautogui.moveTo(314,742)
pyautogui.click()
time.sleep(2)

for url in urls:
	webbrowser.register("chrome", None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
	webbrowser.get("chrome").open(urls[aux])
	aux += 1
	time.sleep(1)

print("Sistemas iniciados")
time.sleep(1)