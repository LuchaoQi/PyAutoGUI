import pyautogui, sys


def mouse():
	pyautogui.moveTo(x=None, y=None, duration=0.0, tween=linear, logScreenshot=False, _pause=True)

	pyautogui.click(x=None, y=None, clicks=1, interval=0.0, button=PRIMARY, duration=0.0, tween=linear, logScreenshot=None, _pause=True)
	pyautogui.click(button='right')
	pyautogui.doubleClick()

def keyboard():


	pyautogui.write('hello!')


	pyautogui.press(keys, presses=1, interval=0.0, logScreenshot=None, _pause=True)
	pyautogui.press('enter')
	pyautogui.hotkey('ctrl','shift','t')
	pyautogui.hotkey('ctrl','c')


	pyautogui.PAUSE=0.5
	pyautogui.keyDown('alt')
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.press('tab')
	pyautogui.keyUp('alt')




if __name__=='__main__':

	print('Press Ctrl-C to quit.')
	try:
		while True:
			x, y = pyautogui.position()
			positionStr = 'X: ' + str(x) + ' Y: ' + str(y)
			print(positionStr, end='')
			# pretty interesting
			print('\b' * len(positionStr), end='', flush=True)
	except KeyboardInterrupt:
		print('\n')