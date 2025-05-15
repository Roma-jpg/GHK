import json
import keyboard
import subprocess
import time
import threading
import os
from win10toast import ToastNotifier

last_called = {}

def cooldown(func_name, seconds=2):
	current_time = time.time()
	last_time = last_called.get(func_name, 0)
	if current_time - last_time >= seconds:
		last_called[func_name] = current_time
		return True
	return False

def function_name():
	if cooldown("function_name"):
		print("function_name was called!")

def another_function():
	if cooldown("another_function"):
		print("another_function was called!")

def test_notification():
	if cooldown("test_notification"):
		threading.Thread(target=show_test_notification, daemon=True).start()

def show_test_notification():
	notifier = ToastNotifier()
	notifier.show_toast("GHK Test", "This is your test notification.", duration=5)

def open_work_apps():
	if not cooldown("open_work_apps"):
		return
	program_paths = [
		r"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
		r"C:\\Users\\Ромэо\\AppData\\Local\\Programs\\YandexMusic\\Яндекс Музыка.exe",
		r"C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.3.5\\bin\\pycharm64.exe",
		r"C:\\Users\\Ромэо\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
	]
	for path in program_paths:
		try:
			subprocess.Popen(path)
			print(f"Launched: {path}")
		except Exception as e:
			print(f"Failed to launch {path}: {e}")

def show_notification():
	notifier = ToastNotifier()
	notifier.show_toast("Shortcut Listener", "Tool has started. Ready for shortcuts.", duration=5)

function_map = {
	"test_notification": test_notification,
	"function_name": function_name,
	"another_function": another_function,
	"open_work_apps": open_work_apps
}

def load_config(config_name="shortcuts.json"):
	script_dir = os.path.dirname(os.path.abspath(__file__))
	config_path = os.path.join(script_dir, config_name)
	with open(config_path, "r", encoding="utf-8") as f:
		return json.load(f)

def register_hotkeys(shortcuts):
	for hotkey, func_name in shortcuts.items():
		if func_name in function_map:
			keyboard.add_hotkey(hotkey, function_map[func_name])
			print(f"Registered hotkey: {hotkey} -> {func_name}")
		else:
			print(f"Warning: function '{func_name}' not found.")

if __name__ == "__main__":
	threading.Thread(target=show_notification, daemon=True).start()
	shortcuts = load_config()
	register_hotkeys(shortcuts)
	print("Listening for shortcuts...")
	keyboard.wait()
