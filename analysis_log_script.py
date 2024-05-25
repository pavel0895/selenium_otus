import os
import json
from collections import Counter
from operator import itemgetter


def analyze_logs(log_files):
    total_requests = 0
    methods = Counter()
    ip_addresses = Counter()
    slow_requests = []

    with open(log_files, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 7:
                continue
            total_requests += 1
            methods[parts[5].split()[0].strip('"')] += 1
            ip_addresses[parts[0]] += 1
            slow_requests.append({
                "method": parts[5].split()[0].strip('"'),
                "url": parts[6],
                "ip": parts[0],
                "duration": int(parts[-1]),
                "date_time": parts[3].strip('[]')
            })

    slow_requests = sorted(slow_requests, key=itemgetter("duration"), reverse=True)[:3]

    return {
        "total_requests": total_requests,
        "total_stat": dict(methods),
        "top_ips": dict(ip_addresses.most_common(3)),
        "top_longest": slow_requests
    }


def main():
    log_files = []
    directory = input("Введите директорию для поиска log-файлов или введите путь к конкретному log-файлу: ")

    if os.path.isfile(directory):
        log_files.append(directory)
    elif os.path.isdir(directory):
        for file_name in os.listdir(directory):
            if file_name.endswith(".log"):
                log_files.append(os.path.join(directory, file_name))
    else:
        print("Путь не существует или указан неверно!")
        return

    for log_file in log_files:
        result = analyze_logs(log_file)

        json_file = f"{log_file}.json"
        with open(log_file, 'w') as file:
            json.dump(result, file, indent=4)

    print(f"Результат анализа для {log_file} сохранён в файл {json_file}")
    print("Всего выполненных запросов: ", result["total_requests"])
    print("Количество запросов по методам: ", result["total_stat"])
    print("Top-3 IP-адресов: ", result["top_ips"])
    print("Top-3 самых долгих запроса: ")
    for i, request in enumerate(result["top_longest"]):
        print(
            f"{i + 1}. Метод: {request['method']}, URL: {request['url']}, IP: {request['ip']}, Продолжительность: {request['duration']}, Дата и время: {request['date_time']}")


if __name__ == "__main__":
    main()
