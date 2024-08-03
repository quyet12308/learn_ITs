import os


def create_folders(folder_names, base_path):
    for folder_name in folder_names:
        folder_path = os.path.join(base_path, folder_name)
        try:
            os.mkdir(folder_path)
            print(f'Thư mục "{folder_path}" đã được tạo.')
        except FileExistsError:
            print(f'Thư mục "{folder_path}" đã tồn tại.')


def create_folders_from_file(file_path, base_path):
    with open(file_path, "r") as file:
        for folder_name in file:
            folder_name = folder_name.strip()  # Loại bỏ dấu xuống dòng
            folder_path = os.path.join(base_path, folder_name)
            try:
                os.mkdir(folder_path)
                print(f'Thư mục "{folder_path}" đã được tạo.')
            except FileExistsError:
                print(f'Thư mục "{folder_path}" đã tồn tại.')


# Danh sách tên thư mục cần tạo
folders_to_create = []

# Đường dẫn tuyệt đối cho thư mục gốc
base_directory = r"F:\learn_ITs\documents\Computer Science Fundamentals"

# Gọi hàm để tạo thư mục
# create_folders(folders_to_create, base_directory)

create_folders_from_file(base_path=base_directory, file_path="test.txt")
