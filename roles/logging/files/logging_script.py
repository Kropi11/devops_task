import os
import re
import time
import json
import requests
import datetime
import subprocess

# Function to get the headers from the Nginx access.log file
def get_nginx_headers(start_time):
    # Read the access.log file
    with open('/var/log/nginx/access.log', 'r') as file:
        # Extract the headers from the new content
        headers = []
        lines = file.readlines()
        for line in lines:
            time_str = line.split("[")[1].split()[0]  # Extracting the timestamp string
            log_time = datetime.datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S")
            if log_time >= start_time:  # Check if the log entry falls within the time interval
                headers.append(line.split(' "-" ')[1].strip('"'))
        return headers
    
# Function to get Nginx status from the stub_status module
def get_nginx_status(url):
    # Send a GET request to the URL and retrieve the response
    response = subprocess.check_output(["curl", url]).decode("utf-8")
    
    # Parse the response to extract the desired information
    active_connections = None
    accepts = None
    handled = None
    requests = None
    reading = None
    writing = None
    waiting = None
    
    lines = response.split("\n")
    for line in lines:
        if line.startswith("Active connections:"):
            active_connections = line.split(":")[1].strip()
        elif re.match(r'\s*\d+\s+\d+\s+\d+', line):
            values = line.split()
            accepts = values[0]
            handled = values[1]
            requests = values[2]
        elif line.startswith("Reading:") and "Writing:" in line and "Waiting:" in line:
            values = re.findall(r'\d+', line)
            reading, writing, waiting = values
    
    # Construct the nginx_status string  
    nginx_status = {
        'ActiveConnections': int(active_connections),
        'ServerAccepts': int(accepts),
        'ServerHandled': int(handled),
        'ServerRequests': int(requests),
        'Reading': int(reading),
        'Writing': int(writing),
        'Waiting': int(waiting)
    }
    
    return nginx_status

# Function to get Docker container load
def get_docker_container_load(url, container_id):
    # Make a GET request to the Docker API to get container stats
    response = requests.get(f"http://{url}/containers/{container_id}/json")
    container_stats = response.json()
    
    # Extract the desired information from the container stats
    cpu_usage = container_stats["HostConfig"]["CpuPercent"]
    memory_usage = container_stats["HostConfig"]["Memory"]
    swap_usage = container_stats["HostConfig"]["MemorySwap"]
    
    # Construct the container_load string
    container_load = {
        'CpuUsage': cpu_usage,
        'MemoryUsage': memory_usage,
        'SwapUsage': swap_usage
    }
      
    return container_load

# Function to save the output to a JSON file
def save_json_to_file(data, file_path):
    with open(file_path, 'a') as file:
        if os.stat(file_path).st_size == 0:
            file.write('[')
        else:
            file.seek(file.tell() - 1, os.SEEK_SET)
            file.truncate()
            file.write(',\n')
        
        json.dump(data, file)
        
        file.write(']')

# Function to get all running container names
def get_container_names(ip):
    # Get the list of all running containers
    response = requests.get(f"http://{ip}:4243/containers/json")
    containers = response.json()
    
    # Extract the container names from the response
    container_names = []
    for container in containers:
        container_names.append(container["Names"][0].strip("/"))
    
    return container_names

def main():
    ip = "10.0.2.15" # IP address of the Docker host
    start_time = datetime.datetime.now()
    while True:    
        docker_container_load = {}
        
        for container in get_container_names(ip):    
            docker_container_load[container] = get_docker_container_load(f'{ip}:4243', container)
        nginx_status = get_nginx_status(f'{ip}/nginx_status')
        headers = get_nginx_headers(start_time)

        # Construct the output dictionary
        output = {
            "Date-TimeStamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "DockerContainerLoad": docker_container_load,
            "NginxStatus": nginx_status,
            "NginxHeaders": headers
        }

        # Save the output to a JSON file
        save_json_to_file(output, '/var/log/logging_script/metrics.json')

        # Wait for 20 seconds before the next iteration
        start_time = datetime.datetime.now()
        time.sleep(20)

if __name__ == "__main__":
    main()