

# 导入需要的模块
from AppRecorder import Recorder
import tkinter as tk
from tkinter import filedialog, messagebox
import time
process_list = []
base_path =''
frequency = 10

def add_process():
	process_name = entry_process.get()
	if process_name:
		process_list.append(process_name)
		entry_process.delete(0, tk.END)
		listbox_process.insert(tk.END, process_name)
	else:
		messagebox.showerror("错误", "进程名不能为空")


def select_base_path():
	base_path = filedialog.askdirectory()
	entry_base_path.delete(0, tk.END)
	entry_base_path.insert(0, base_path)


def start_monitor():
	global base_path
	global frequency
	base_path = entry_base_path.get()
	frequency = int(entry_frequency.get())
	# 关闭窗口
	window.destroy()
	# 创建Recorder对象

	# 在这里处理你的逻辑，例如启动监控进程的功能
	# exit(0)

def center_window(window):
	window.update_idletasks()
	width = window.winfo_width()
	height = window.winfo_height()
	x = (window.winfo_screenwidth() // 2) - (width // 2)
	y = (window.winfo_screenheight() // 2) - (height // 2)
	window.geometry(f"+{x}+{y}")


def gui():
	global window, entry_base_path, entry_frequency, entry_process, listbox_process, process_list

	window = tk.Tk()
	center_window(window)
	window.title("日志监控设置")
	center_window(window)
	# 日志文件保存根路径
	label_base_path = tk.Label(window, text="日志文件保存根路径:")
	label_base_path.grid(row=0, column=0, sticky=tk.W)

	entry_base_path = tk.Entry(window)
	entry_base_path.grid(row=0, column=1)

	# button_select_base_path = tk.Button(window, text="...", command=select_base_path)
	# button_select_base_path.grid(row=0, column=2)

	# 监控的App进程名字列表
	label_process = tk.Label(window, text="监控的App进程:")
	label_process.grid(row=1, column=0, sticky=tk.W)

	entry_process = tk.Entry(window)
	entry_process.grid(row=1, column=1)

	button_add_process = tk.Button(window, text="添加进程", command=add_process)
	button_add_process.grid(row=1, column=2)

	label_process_list = tk.Label(window, text="进程列表:")
	label_process_list.grid(row=2, column=0, sticky=tk.W, padx=(30, 0))

	listbox_process = tk.Listbox(window)
	listbox_process.grid(row=2, column=1, columnspan=2, padx=(0, 60), pady=10)

	# 日志写文件的频率
	label_frequency = tk.Label(window, text="日志写文件的频率(秒):")
	label_frequency.grid(row=3, column=0, sticky=tk.W)

	entry_frequency = tk.Entry(window)
	entry_frequency.grid(row=3, column=1)

	button_start_monitor = tk.Button(window, text="开始监控", command=start_monitor)
	button_start_monitor.grid(row=4, column=0, columnspan=3, pady=20)
	window.mainloop()
if __name__ == '__main__':
	gui()
	# 创建Recorder对象
	# print(process_list,base_path)
	recorder = Recorder(base_path,process_list)

	# 开始录制
	# while True:
	while True:
		recorder.start_recording()
		time.sleep(frequency)
		filename = recorder.stop_recording()
	recorder.quit()


