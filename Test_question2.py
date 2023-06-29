import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def process_data(data):
    numbers = data["numbers"]
    total_sum = sum(numbers)

    names = data["names"]
    filtered_names = [name for name in names if name.startswith("A")]
    return total_sum,filtered_names

#just add any json file in the current directory name data.json
file_path = "data.json"
json_data = read_json_file(file_path)
result_sum,result_names = process_data(json_data)

print("sum of numbers",result_sum)
print("names starting with 'A':", result_names)
