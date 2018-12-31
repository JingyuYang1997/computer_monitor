import psutil
import pynvml
import time


class Monitor(object):
    def __init__(self):
        self.logging_user_dict={}
        self.IP_Whitelist=['localhost']
        self.disk_information={}
        self.cpu_information = {}
        self.gpu_information={}
        self.memory_information = {}
        self.network_information = {}
        self.pid_information = []
        self.past_send_flow=0
        self.past_recv_flow=0
        self.current_send_flow=0
        self.current_recv_flow=0


    def get_logging_user(self):
        logging_users=psutil.users()
        logging_user_dict = {}
        for user in logging_users:
            if user.host not in self.IP_Whitelist:
                logging_user_dict['name']=user.name
                logging_user_dict['host']=user.host
        self.logging_user_dict= logging_user_dict

    def get_disk(self):
        disk_usage=psutil.disk_usage('/')
        disk_total=disk_usage.total/1024.0/1024.0/1024.0
        disk_used=disk_usage.used/1024.0/1024.0/1024.0
        disk_percent=disk_usage.percent
        # disk_information=str(disk_percent)+'%'+'  %0.1f/%0.1fG'%(disk_used,disk_total)
        disk_information={}
        disk_information['total']=disk_total
        disk_information['used']=disk_used
        disk_information['percent']=disk_percent
        self.disk_information= disk_information

    def get_cpu(self):
        cpu_percent= psutil.cpu_percent(interval=None,percpu=False)
        cpu_freq=psutil.cpu_freq(percpu=False).current/1000
        # cpu_information=str(cpu_percent)+'%'+'  %0.2fGHz'%cpu_freq
        cpu_information = {}
        cpu_information['percent'] = cpu_percent
        cpu_information['freq'] = cpu_freq
        self.cpu_information=cpu_information

    def get_gpu(self):
        pynvml.nvmlInit()
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        gpu_total = meminfo.total / 1024.0 / 1024.0 / 1024.0
        gpu_used = meminfo.used / 1024.0 / 1024.0 / 1024.0
        gpu_percent=gpu_used/gpu_total*100
        # gpu_information=str(gpu_percent)+'%'+'  %0.1f/%0.1fG'%(gpu_used,gpu_total)
        gpu_information = {}
        gpu_information['total'] = gpu_total
        gpu_information['used'] = gpu_used
        gpu_information['percent'] = gpu_percent
        self.gpu_information= gpu_information

    def get_memory(self):
        memory_total=psutil.virtual_memory().total
        memory_used=psutil.virtual_memory().used
        memory_percent=psutil.virtual_memory().percent
        # memory_information = str(memory_percent) + '%' + '  %0.1f/%0.1fG' % (memory_used, memory_total)
        memory_information = {}
        memory_information['total'] = memory_total/ 1024.0 / 1024.0 / 1024.0
        memory_information['used'] = memory_used/ 1024.0 / 1024.0 / 1024.0
        memory_information['percent'] = memory_percent
        self.memory_information= memory_information

    def get_network(self):
        self.past_send_flow=self.current_send_flow
        self.past_recv_flow=self.current_recv_flow
        self.current_send_flow=psutil.net_io_counters(pernic=False).bytes_sent
        self.current_recv_flow=psutil.net_io_counters(pernic=False).bytes_recv
        sk=float(self.current_send_flow-self.past_send_flow)/1024
        sm=float(self.current_send_flow-self.past_send_flow)/1024/1024
        rk = float(self.current_recv_flow - self.past_recv_flow) / 1024
        rm = float(self.current_recv_flow - self.past_recv_flow) / 1024 / 1024
        if sk < 1000 and rk < 1000:
            send = str(float('%0.2f' % sk)) + 'Kb/s'
            recv = str(float('%0.2f' % rk)) + 'Kb/s'
        elif sk < 1000 and rk > 1000:
            send = str(float('%0.2f' % sk)) + 'Kb/s'
            recv = str(float('%0.2f' % rm)) + 'M/s'
        elif sk > 1000 and rk < 1000:
            send = str(float('%0.2f' % sm)) + 'M/s'
            recv = str(float('%0.2f' % rk)) + 'Kb/s'
        else:
            send = str(float('%0.2f' % sm)) + 'M/s'
            recv = str(float('%0.2f' % rm)) + 'M/s'
        network_information={}
        network_information['send']=send
        network_information['recv']=recv
        self.network_information=network_information

    def get_pid(self):
        pid_info_list=[]
        pids=psutil.pids()
        for pid_id in pids:
            if psutil.pid_exists(pid_id):
                pid_info_dict = {}
                pid=psutil.Process(pid_id)
                pid_info_dict['name']=pid.name()
                pid_info_dict['status']=pid.status()
                pid_info_dict['memory_percent']=pid.memory_percent()
                pid_info_dict['cpu_percent']=pid.cpu_percent()
                pid_info_list.append(pid_info_dict)
        self.pid_information= pid_info_list

# monitor=Monitor()
# while 1:
#     monitor.get_gpu()   
#     monitor.get_memory()
#     monitor.get_network()
#     monitor.get_pid()
#     print(monitor.network_information['send'],monitor.network_information['recv'])
#     time.sleep(2)







