#!/bin/python3

import shutil
import sys
import os


def fileAlreadyExists(file, directory):
    path_file = os.path.join(directory, file)
    return os.path.exists(path_file)


status = {
    "failed": "\033[91m",
    "sucessfull": "\033[92m",
    "warning": "\033[93m",
    "normal": "\033[0m"
}

try:
    service_name = input("Service name: ")
    description = input("Service description: ")
    executable = input("Executable comand: ")
    path_creation_file = input("Create service in path: [default: /etc/systemd/system/] ")

    service_name = service_name.split(".")[0] + ".service"

    if len(path_creation_file) == 0 :
        path_creation_file = "/etc/systemd/system/"

    if fileAlreadyExists(service_name, path_creation_file):
        fail_status = status.get("failed")
        realpath = os.path.realpath(path_creation_file)
        print(f"{fail_status}\n\n>>> File already exists in path: {realpath}\n")
        sys.exit(1)

    comand = executable.split(" ")[0] 
    executable_path = shutil.which(comand) or sys.executable
    executable = executable.replace(comand, executable_path)

    service_file_path = path_creation_file + service_name

    service_file = open(service_name, "w")
    service_file.write(f"[Unit]\nDescription={description}\n\n")
    service_file.write(f"[Service]\nExecStart={executable}\n\n")
    service_file.write(f"[Install]\nWantedBy=multi-user.target\n\n")
    service_file.close()

    sucess = status.get("sucessfull")
    print(f"{sucess}\n==================================")
    print(f"{sucess}\n>>> Service created...")
    print(f"{sucess}\n==================================")

    warn = status.get("warning")
    start_service = input(f"{warn}\n>>> Start the service [y] - Yes or [n] - No (default: n): ")

    if start_service.lower() == "y" :
        start_service_comand = f"systemctl start {service_name}"
        running_comand = os.system(start_service_comand)

        if running_comand != 0:
            fail = status.get("failed")
            reset = status.get("normal")
            print(f"{fail}\n>>> Fail to start the service;")
            print(f"{reset}run comand 'sudo systemctl status {service_name}' to learn more")
            sys.exit(1)

        sucess = status.get("sucessfull")
        print(f"{sucess}\n>>> Service started...")
        sys.exit(0)
except KeyboardInterrupt:
    print("\nCtr-C interrupt comand ...")
