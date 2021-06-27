from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
import threading, time

cps = float(input("Enter the delay in seconds: "))

for i in range(3): print(f"\n	{i+1}"); time.sleep(1)
print("\n   GO\n\n   Press ESCAPE to stop.\n\n\n")

mouse = Controller()

Spam = True

def on_press(key):
	global Spam
	if key == Key.esc:
		Spam = False
		exit()

def ShortcutListener():
	with Listener(on_press=on_press) as listener:listener.join()



def SpamC():
	while Spam:
		mouse.press(Button.left)
		mouse.release(Button.left)
		time.sleep(cps)


tr1 = threading.Thread(target=SpamC)
tr2 = threading.Thread(target=ShortcutListener)

tr1.start()
tr2.start()
