import psutil
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "192.168.1.100"
server_port = 80
s.connect((server_ip, server_port))
while True:
    memory = psutil.virtual_memory()
    total_memory = memory.total
    used_memory = memory.used
    memory_usage_percent = (used_memory / total_memory) * 100
    cpu_usage_percent = psutil.cpu_percent(interval=1)

    message =  "R: {:.2f}%".format(memory_usage_percent)+ " " + "C: {:.2f}%".format(cpu_usage_percent)+"_"
    s.sendall(message.encode())
    time.sleep(1)