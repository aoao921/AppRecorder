
# 导入需要的模块
from AppRecorder import Recorder
from AppRecorder.core import read_config_file
import time
process_list = []
base_path =''
frequency = 15


if __name__ == '__main__':
	process_list=read_config_file().process_list
	base_path=read_config_file().base_path
	frequency=int(read_config_file().frequency)
	# 创建Recorder对象
	recorder = Recorder(base_path,process_list)
	# 开始录制
	while True:
		recorder.start_recording()
		time.sleep(frequency)
		filename = recorder.stop_recording()
		print("完成一次日志写入")
		time.sleep(1)
	recorder.quit()


