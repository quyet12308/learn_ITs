import os


def rename_images_in_subfolders(parent_folder):
    # Duyệt qua các thư mục con trong thư mục cha
    for subdir, _, files in os.walk(parent_folder):
        # Lấy tên thư mục con
        folder_name = os.path.basename(subdir)

        # Lọc ra các file ảnh (có đuôi .jpg, .jpeg, .png)
        image_files = [
            f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        # Đổi tên các file ảnh
        for i, filename in enumerate(image_files, start=1):
            # Lấy phần mở rộng của file
            file_extension = os.path.splitext(filename)[1]
            # Tạo tên mới cho file
            new_name = f"{folder_name}_{i}{file_extension}"
            # Đường dẫn đầy đủ của file hiện tại và file mới
            old_file_path = os.path.join(subdir, filename)
            new_file_path = os.path.join(subdir, new_name)
            # Đổi tên file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{old_file_path}' to '{new_file_path}'")


# Ví dụ sử dụng hàm
parent_folder_path = r"F:\AI\BTL_hau\datasets\new_datasets"
rename_images_in_subfolders(parent_folder_path)
