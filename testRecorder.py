# from pywinauto_recorder import Recorder
#
# import flask
# import time
#
#
#
# from flask import Flask, render_template, request, redirect
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return 'hello'
#
# @app.route('/start', methods=['GET'])
# def start():
#     recorder.start_recording()
#     return 'start'
#
# @app.route('/stop', methods=['GET'])
# def stop():
#    filename=recorder.stop_recording()
#    return 'stop'
#
# if __name__ == '__main__':
# 	recorder = Recorder()
#
# 	app.run(debug=False)

# 导入需要的模块
from pywinauto_recorder import Recorder

import time

if __name__ == '__main__':
	# 创建Recorder对象
	recorder = Recorder()

	# 开始录制
	recorder.start_recording()

	time.sleep(10)

	filename = recorder.stop_recording()

	# print(filename)

	# 退出Recorder
	recorder.quit()
