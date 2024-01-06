from collections import namedtuple

import win32gui
import win32process
import psutil
import time
import codecs
import datetime
ElementEvent = namedtuple('ElementEvent', ['strategy', 'rectangle', 'path','time','id'])
SendKeysEvent = namedtuple('SendKeysEvent', ['line', 'time','id'])
MouseWheelEvent = namedtuple('MouseWheelEvent', ['delta','time','id'])
DragAndDropEvent = namedtuple('DragAndDropEvent', ['path', 'dx1', 'dy1', 'path2', 'dx2', 'dy2','time'])
ClickEvent = namedtuple('ClickEvent', ['button', 'click_count', 'path', 'dx', 'dy', 'time','id'])
FindEvent = namedtuple('FindEvent', ['path', 'dx', 'dy', 'time'])
MenuEvent = namedtuple('MenuEvent', ['path', 'menu_path','time','id'])


def get_process_id_from_window_title(title):
	handle = win32gui.FindWindow(None, title)
	thread_id, process_id = win32process.GetWindowThreadProcessId(handle)
	return process_id
def get_process_id_by_name(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return process.info['pid']
    return None
def get_parent_process_id(process_id):
    try:
        process = psutil.Process(process_id)
        parent_process = process.parent()
        parent_process_id = parent_process.pid
        return parent_process_id
    except psutil.NoSuchProcess:
        return None
def get_window_handle_by_title(title):
    handle = win32gui.FindWindow(None, title)
    return handle

def get_parent_window_handle(window_handle):
    parent_handle = win32gui.GetParent(window_handle)
    return parent_handle

def get_child_window_handles(window_handle):
    child_handles\
        = []
    win32gui.EnumChildWindows(window_handle, lambda handle, param: param.append(handle), child_handles)
    return child_handles

def get_process_id_from_window_handle(window_handle):
    thread_id, process_id = win32process.GetWindowThreadProcessId(window_handle)
    return process_id
def get_child_process_ids(parent_process_id):
    child_process_ids = []
    try:
        parent_process = psutil.Process(parent_process_id)
        child_processes = parent_process.children(recursive=True)
        child_process_ids = [child.pid for child in child_processes]
    except psutil.NoSuchProcess:
        pass

    return child_process_ids


def print_all_event_list(event_list):
    # print(event_list)
    with codecs.open("events.txt", 'a', 'utf-8') as file:
        for event in event_list:
            event_time = datetime.datetime.fromtimestamp(event.time)
            formatted_time = event_time.strftime("%Y-%m-%d %H:%M:%S")
       
            if isinstance(event, ElementEvent):
                
                file.write(f"{formatted_time} - ElementEvent: path={event.path} - id={event.id}\n")
            elif isinstance(event, SendKeysEvent):
                file.write(
                    f"{formatted_time} - SendKeysEvent: line={event.line} - id={event.id}\n")
            
            elif isinstance(event, MouseWheelEvent):
                file.write(
                    f"{formatted_time} - MouseWheelEvent: delta={event.delta} - id={event.id}\n")
            elif isinstance(event, DragAndDropEvent):
            	file.write(

            		f"{formatted_time} - DragAndDropEvent: path={event.path} - dx1={event.dx1} - dy1={event.dy1} - path2={event.path2} - dx2={event.dx2} - dy2={event.dy2}\n")
            elif isinstance(event, ClickEvent):
                file.write(
                    f"{formatted_time} - ClickEvent: button={event.button} - click_count={event.click_count} - path={event.path} id={event.id}\n")
            elif isinstance(event, FindEvent):
                file.write(
                    f"{formatted_time} - FindEvent: path={event.path} - dx={event.dx} - dy={event.dy} - time={formatted_time}\n")
            elif isinstance(event, MenuEvent):
                file.write(
                    f"{formatted_time} - MenuEvent: path={event.path} - menu_path={event.menu_path} - id={event.id}\n")
            else:
                pass
        # gbk_to_utf8("events.txt", "events.txt")
def print_certain_event_list(BasePath,event_list,process_name,process_id):
    # wireshark_id = get_process_id_by_name('Wireshark.exe')
    filename=BasePath+"\\events_"+process_name+".txt"
    
    with codecs.open(filename, 'a', 'utf-8') as file:
        for event in event_list:
            event_time = datetime.datetime.fromtimestamp(event.time)
            formatted_time = event_time.strftime("%Y-%m-%d %H:%M:%S")
            if hasattr(event, 'id') and event.id != process_id:
                continue
            if isinstance(event, ElementEvent):
                file.write(f"{formatted_time} - ElementEvent: path={event.path} - id={event.id}\n")
            elif isinstance(event, SendKeysEvent):
               
                file.write(
                    f"{formatted_time} - SendKeysEvent: line={event.line} - id={event.id}\n")
            
            elif isinstance(event, MouseWheelEvent):
                
                formatted_time = event_time.strftime("%Y-%m-%d %H:%M:%S")
                file.write(
                    f"{formatted_time} - MouseWheelEvent: delta={event.delta}- id={event.id}\n")

            elif isinstance(event, ClickEvent):
                file.write(
                    f"{formatted_time} - ClickEvent: button={event.button} - click_count={event.click_count} - path={event.path} id={event.id}\n")
            
            elif isinstance(event, FindEvent):
        
                file.write(
                    f"{formatted_time} - FindEvent: path={event.path} - dx={event.dx} - dy={event.dy} - time={formatted_time}\n")
            
            elif isinstance(event, MenuEvent):
                file.write(
                    f"{formatted_time} - MenuEvent: path={event.path} - menu_path={event.menu_path} - id={event.id}\n")
            else:
                pass
    


