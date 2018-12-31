import tkinter as tk
from computer_monitor import Monitor
import time
monitor=Monitor()

def main():
    window=tk.Tk()
    window.title('Computer_Monitor-v1.0')
    window.geometry('800x400')
    logging_user_title=tk.Label(window,text='User',font=('Arial',12),width=15,height=1)
    logging_user_title.place(x=10,y=30,anchor='nw')
    cpu_title=tk.Label(window,text='CPU',font=('Arial',12),width=15,height=1)
    cpu_title.place(x=10,y=80,anchor='nw')
    memory_title=tk.Label(window,text='RAM',font=('Arial',12),width=15,height=1)
    memory_title.place(x=10,y=130,anchor='nw')
    gpu_title=tk.Label(window,text='GPU',font=('Arial',12),width=15,height=1)
    gpu_title.place(x=10,y=180,anchor='nw')
    disk_title=tk.Label(window,text='Disk',font=('Arial',12),width=15,height=1)
    disk_title.place(x=10,y=230,anchor='nw')
    network_title=tk.Label(window,text='Int',font=('Arial',12),width=15,height=1)
    network_title.place(x=10,y=280,anchor='nw')
    logging_user_description=tk.Label(window,text='username  host',font=('Arial',10),width=15,height=1)
    logging_user_description.place(x=160,y=10,anchor='nw')
    cpu_description=tk.Label(window,text='percent  frequence',font=('Arial',10),width=15,height=1)
    cpu_description.place(x=160,y=60,anchor='nw')
    memory_description=tk.Label(window,text='percent  used/total',font=('Arial',10),width=15,height=1)
    memory_description.place(x=160,y=110,anchor='nw')
    gpu_description=tk.Label(window,text='percent  used/total',font=('Arial',10),width=15,height=1)
    gpu_description.place(x=160,y=160,anchor='nw')
    disk_description=tk.Label(window,text='percent  used/total',font=('Arial',10),width=15,height=1)
    disk_description.place(x=160,y=210,anchor='nw')
    network_description=tk.Label(window,text='send    recv',font=('Arial',10),width=15,height=1)
    network_description.place(x=140,y=260,anchor='nw')
    tk.Label(window,text=
             '''    该程序模拟任务管理器实时监控电脑的情况，包
    括登陆用户，CPU，GPU，硬盘，内存使用情况
    以及带宽。程序猿：杨靖宇。github链接为
    https://github.com/enduranceever/computer_monitor.git
             ''',
             justify='left',font=('Arial',10),width=45,height=5).place(x=40,y=310,anchor='nw')


    logging_user_var=tk.StringVar()
    cpu_var=tk.StringVar()
    memory_var=tk.StringVar()
    gpu_var=tk.StringVar()
    disk_var=tk.StringVar()
    network_var=tk.StringVar()
    logging_user_info=tk.Label(window,textvariable=logging_user_var,font=('Arial',12),width=15,height=1)
    logging_user_info.place(x=150,y=30,anchor='nw')
    cpu_info=tk.Label(window,textvariable=cpu_var,font=('Arial',12),width=15,height=1)
    cpu_info.place(x=150,y=80,anchor='nw')
    memory_info=tk.Label(window,textvariable=memory_var,font=('Arial',12),width=15,height=1)
    memory_info.place(x=150,y=130,anchor='nw')
    gpu_info=tk.Label(window,textvariable=gpu_var,font=('Arial',12),width=15,height=1)
    gpu_info.place(x=150,y=180,anchor='nw')
    disk_info=tk.Label(window,textvariable=disk_var,font=('Arial',12),width=15,height=1)
    disk_info.place(x=150,y=230,anchor='nw')
    network_info=tk.Label(window,textvariable=network_var,font=('Arial',12),width=20,height=1)
    network_info.place(x=130,y=280,anchor='nw')
    cpu_flag=tk.Label(window,width=3,height=1,bg='green')
    cpu_flag.place(x=290,y=80,anchor='nw')
    memory_flag=tk.Label(window,width=3,height=1,bg='green')
    memory_flag.place(x=290,y=130,anchor='nw')
    gpu_flag=tk.Label(window,width=3,height=1,bg='green')
    gpu_flag.place(x=290,y=180,anchor='nw')
    disk_flag=tk.Label(window,width=3,height=1,bg='green')
    disk_flag.place(x=290,y=230,anchor='nw')


    process_title=tk.Label(window,text='Process',font=('Arial',12),width=6,height=1)
    process_title.place(x=340,y=155,anchor='nw')
    process_var=tk.StringVar()
    process_listbox=tk.Listbox(window,listvariable=process_var,height=15,width=40)
    process_listbox.place(x=420,y=30,anchor='nw')
    sort_var=tk.StringVar()
    process_sort_cpu=tk.Radiobutton(window,text='CPU',variable=sort_var,value='cpu_percent',command=None)
    process_sort_cpu.place(x=710,y=30,anchor='nw')
    process_sort_ram=tk.Radiobutton(window,text='RAM',variable=sort_var,value='memory_percent',command=None)
    process_sort_ram.place(x=710,y=60,anchor='nw')


    def flag_color(percent):
        if percent<=40:
            return 'green'
        if percent>40 and percent<=80:
            return 'yellow'
        else:
            return 'red'


    while 1:
        monitor.get_logging_user()
        logging_user_var.set(monitor.logging_user_dict['name']+'  '+monitor.logging_user_dict['host'])
        monitor.get_cpu()
        cpu_var.set('%0.1f'%(monitor.cpu_information['percent'])+'%'+'  %0.2fGHz' % monitor.cpu_information['freq'])
        cpu_flag.configure(bg=flag_color(monitor.cpu_information['percent']))
        monitor.get_disk()
        disk_var.set('%0.1f'%(monitor.disk_information['percent'])+'%'+'  %d/%dG'%(monitor.disk_information['used'],\
                                                                                    monitor.disk_information['total']))
        disk_flag.configure(bg=flag_color(monitor.disk_information['percent']))
        monitor.get_gpu()
        gpu_var.set('%0.1f'%(monitor.gpu_information['percent'])+'%'+'  %0.1f/%0.1fG'%(monitor.gpu_information['used'],\
                                                                                          monitor.gpu_information['total']))
        gpu_flag.configure(bg=flag_color(monitor.gpu_information['percent']))
        monitor.get_memory()
        memory_var.set('%0.1f'%(monitor.memory_information['percent'])+'%'+'  %0.1f/%0.1fG'%(monitor.memory_information['used'],\
                                                                                    monitor.memory_information['total']))
        memory_flag.configure(bg=flag_color(monitor.memory_information['percent']))
        monitor.get_network()
        network_var.set(monitor.network_information['send']+'    '+monitor.network_information['recv'])
        monitor.get_pid()
        if sort_var.get() == 'cpu_percent':
            monitor.pid_information.sort(key=lambda x: x['cpu_percent'], reverse=True)
        else:
            monitor.pid_information.sort(key=lambda x: x['memory_percent'], reverse=True)
        process_list=['name    status    cpu_perc     memory_perc']
        for process in monitor.pid_information:
            process_str=process['name']+'    '+process['status']+'    '+'%0.2f'%(process['cpu_percent'])+'%    '+\
                        '%0.2f'%(process['memory_percent'])+'%'
            process_list.append(process_str)
        process_var.set(process_list)
        window.update()
        time.sleep(1)

if __name__=='__main__':
    main()