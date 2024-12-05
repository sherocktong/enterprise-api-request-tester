import os
import json
import time

def parse_http_payload(http_payload):
    lines = http_payload.split('\n')
    method, url, _ = lines[0].split()
    headers = []
    body = ""
    is_body = False
    host = lines[1:].pop(0).split(": ")[1]

    for line in lines[2:]:
        if line == "":
            is_body = True
            continue
        if is_body:
            body += line + "\n"
        else:
            key, value = line.split(": ", 1)
            if key != "Content-Length":
                headers.append({"key": key, "value": value})

    return {
        "id": str(int(time.time() * 1000)),
        "name": "",
        "url": "https://" + host + url,
        "method": method,
        "headers": headers,
        "body": body.strip(),
        "authType": "none",
        "bearerToken": "",
        "username": "",
        "password": ""
    }

def main():
    source_dir = './source/'
    target_dir = './target/'

    # Check if source and target directories exist, if not create them
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for folder_name in os.listdir(source_dir):
        json_data = []
        output_file = os.path.join(target_dir, folder_name + '.json')
        input_directory = os.path.join(source_dir, folder_name)
        for file_name in os.listdir(input_directory):
            file_path = os.path.join(input_directory, file_name)
            with open(file_path, 'r') as file:
                http_payload = file.read()

            request_data = parse_http_payload(http_payload)
            request_data["name"] = file_name.split('.')[0]
            json_data.append(request_data)
            time.sleep(0.001)

        with open(output_file, 'w') as file:
            json.dump(json_data, file, indent=2)

if __name__ == "__main__":
    main()
