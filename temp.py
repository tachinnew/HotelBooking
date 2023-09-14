import allRoom as room

tempmemory = ""

delete_array = {}
temp_array = {}

def add_array(tmp):
    temp_array.append(tmp)

def check_true():
    temp_array = delete_array
    for element in room.roomAll:
        if room.roomStatus[element]:
            add_array(element)

def set_temp(text):
    tempmemory = text

def get_temp(text):
    tempmemory = text