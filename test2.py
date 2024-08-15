# import requests
# import json


# def login_api(url, user_name, password):
#     login_data = {"user_name": user_name, "password": password}
#     headers = {"Content-Type": "application/json"}

#     print(f"Đang gửi yêu cầu đến: {url}")
#     print(f"Dữ liệu gửi đi: {json.dumps(login_data, indent=2)}")
#     print(f"Headers: {headers}")

#     try:
#         response = requests.post(url, json=login_data, headers=headers)
#         print(f"Mã trạng thái: {response.status_code}")
#         print(f"Headers phản hồi: {dict(response.headers)}")
#         print(f"Nội dung phản hồi: {response.text}")

#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Lỗi khi đăng nhập: {e}")
#         if hasattr(e.response, "text"):
#             print(f"Chi tiết lỗi: {e.response.text}")
#         return None


# # Sử dụng hàm
# api_url = "http://113.190.240.134:8010/api/v1/login"
# username = "mrquyet"
# password = "123456"

# result = login_api(api_url, username, password)

# if result:
#     print("Đăng nhập thành công:", result)
# else:
#     print("Đăng nhập thất bại")

# import os


# def add_readme_to_subdirs(grandparent_dir):
#     # Nội dung của file README.md
#     readme_content = "# This is a README file\n\nPlease provide detailed information about this directory."

#     # Duyệt qua tất cả các thư mục con trong thư mục "ông nội"
#     for parent_dir in os.listdir(grandparent_dir):
#         parent_path = os.path.join(grandparent_dir, parent_dir)
#         if os.path.isdir(parent_path):  # Kiểm tra xem đó có phải là thư mục không

#             # Tạo README.md trong thư mục "cha"
#             readme_path = os.path.join(parent_path, "README.md")
#             if not os.path.exists(readme_path):
#                 with open(readme_path, "w") as f:
#                     f.write(readme_content)
#                 print(f"Added README.md to {parent_path}")
#             else:
#                 print(f"README.md already exists in {parent_path}")

#             # Duyệt qua các thư mục "con" trong thư mục "cha"
#             for child_dir in os.listdir(parent_path):
#                 child_path = os.path.join(parent_path, child_dir)
#                 if os.path.isdir(
#                     child_path
#                 ):  # Kiểm tra xem đó có phải là thư mục không

#                     # Tạo README.md trong thư mục "con"
#                     readme_path = os.path.join(child_path, "README.md")
#                     if not os.path.exists(readme_path):
#                         with open(readme_path, "w") as f:
#                             f.write(readme_content)
#                         print(f"Added README.md to {child_path}")
#                     else:
#                         print(f"README.md already exists in {child_path}")


# # Đường dẫn tới thư mục "ông nội"
# grandparent_directory = "documents"

# # Gọi hàm
# add_readme_to_subdirs(grandparent_directory)

import os


def print_directory_structure(path, max_depth=4, current_depth=1, prefix=""):
    if current_depth > max_depth:
        return

    if not os.path.isdir(path):
        print(f"{prefix}├── {os.path.basename(path)}")
        return

    print(f"{prefix}{'└── ' if current_depth > 1 else ''}{os.path.basename(path)}/")

    items = sorted(os.listdir(path))
    for index, item in enumerate(items):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if index == len(items) - 1:
                print_directory_structure(
                    item_path, max_depth, current_depth + 1, prefix + "    "
                )
            else:
                print_directory_structure(
                    item_path, max_depth, current_depth + 1, prefix + "│   "
                )
        else:
            if index == len(items) - 1:
                print(f"{prefix}    └── {item}")
            else:
                print(f"{prefix}    ├── {item}")


# Sử dụng hàm
project_path = r"F:\learn_ITs"
print_directory_structure(project_path)
