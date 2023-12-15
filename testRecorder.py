# 导入需要的模块
from pywinauto_recorder import Recorder

import time

if __name__ == '__main__':
# 创建Recorder对象
	recorder = Recorder()

# 开始录制
	recorder.start_recording()

	time.sleep(8)
	filename = recorder.stop_recording()

	print(filename)

# 退出Recorder
	recorder.quit()
