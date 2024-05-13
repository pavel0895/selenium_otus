import subprocess
import re
import time
from collections import defaultdict

result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')

lines = output.split('\n')[1:]

processes = []
for line in lines:
    data = re.split(r'\s+', line.strip())
    if len(data) < 11:
        continue
    username, pid, cpu_percent, memory, *_, command = data
    processes.append({
        'username': username,
        'pid': pid,
        'cpu_percent': cpu_percent,
        'memory': memory,
        'command': command
    })

process_count = len(processes)

user_process_count = defaultdict(int)
for process in processes:
    user_process_count[process['username']] += 1

total_memory = sum(float(process['memory']) for process in processes)

total_cpu_percent = sum(float(process['cpu_percent']) for process in processes)

highest_memory_process = max(processes, key=lambda x: float(x['memory']))

highest_cpu_process = max(processes, key=lambda x: float(x['cpu_percent']))

report = '''Отчёт о состоянии системы:
Пользователи системы: {}
Процессов запущено: {}
Пользовательских процессов: 
{}
Всего памяти используется: {:.1f} MB
Всего CPU используется: {:.1f}%
Больше всего памяти используется: {} ({} MB)
Больше всего CPU используется: {} ({}%)
'''.format(
    ", ".join(user_process_count.keys()),
    process_count,
    '\n'.join([f"{user}: {count}" for user, count in user_process_count.items()]),
    total_memory,
    total_cpu_percent,
    highest_memory_process['command'][:20],
    highest_memory_process['memory'],
    highest_cpu_process['command'][:20],
    highest_cpu_process['cpu_percent']
)

print(report)

timestamp = time.strftime("%d-%m-%Y-%H:%M", time.localtime())
filename = f"{timestamp}.txt"
with open(filename, 'w') as file:
    file.write(report)
