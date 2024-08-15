import os


def check_missing_numbers(input_list, start_range, end_range):
    all_numbers = set(range(start_range, end_range + 1))
    input_set = set(input_list)
    missing_numbers = sorted(list(all_numbers - input_set))

    if len(missing_numbers) == 0:
        print("Không có số nào bị thiếu.")
    else:
        print("Các số bị thiếu:")
        for number in missing_numbers:
            print(number)


# check_list = [i + 1 for i in range(50)]
# print(check_list)


def check_text_files(folder_path):
    list_file_name = []
    text_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # print(file)
            file_name = file.split(".")[0]
            # print(file_name)
            list_file_name.append(int(file_name))

            if file.endswith(".txt"):
                text_files.append(os.path.join(root, file))
    return text_files, list_file_name


# Sử dụng hàm
folder_path = r"C:\Users\Lenovo\Downloads\labels_my-project-name_2024-04-12-05-49-51"
text_files_list, list_file_name = check_text_files(folder_path)
# print(text_files_list)
# print(len(text_files_list))
print(list_file_name)
check_missing_numbers(input_list=list_file_name, end_range=50, start_range=1)
