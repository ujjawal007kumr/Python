def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data

def process_data(data):
    integers = list(data)
    manipulated_data = [num * 2 for num in integers]
    return manipulated_data

file_path = "binary.bin"
binary_data = read_binary_file(file_path)
result = process_data(binary_data)

print("manipulated_data:", result)