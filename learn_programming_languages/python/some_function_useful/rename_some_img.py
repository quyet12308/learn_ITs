import os


def rename_images(directory):
    file_list = os.listdir(directory)
    image_extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
    ]  # Các phần mở rộng của tệp tin ảnh

    image_files = [
        file
        for file in file_list
        if any(file.lower().endswith(ext) for ext in image_extensions)
    ]

    for i, old_name in enumerate(image_files):
        extension = os.path.splitext(old_name)[1]
        new_name = f"{i+1}{extension}"
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")


# Sử dụng hàm với đường dẫn thư mục chứa ảnh của bạn
# path_folder_images = r"F:\AI\datasets\business_card_datasets"
path_folder_images = r"F:\AI\datasets\inbody_report_datasets"
rename_images(directory=path_folder_images)
