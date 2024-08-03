# import os
# import matplotlib.pyplot as plt


# def count_images_in_subfolders(parent_folder):
#     total_images = 0
#     subfolder_image_counts = {}

#     # Duyệt qua các thư mục con trong thư mục cha
#     for subdir, _, files in os.walk(parent_folder):
#         # Lấy tên thư mục con
#         folder_name = os.path.basename(subdir)

#         # Lọc ra các file ảnh (có đuôi .jpg, .jpeg, .png)
#         image_files = [
#             f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))
#         ]

#         # Đếm số lượng ảnh trong thư mục con hiện tại
#         image_count = len(image_files)
#         if image_count > 0:
#             subfolder_image_counts[folder_name] = image_count
#             total_images += image_count

#     return subfolder_image_counts, total_images


# def plot_image_distribution(image_counts):
#     # Vẽ biểu đồ cột
#     subfolders = list(image_counts.keys())
#     counts = list(image_counts.values())

#     plt.figure(figsize=(10, 6))
#     plt.bar(subfolders, counts, color="skyblue")
#     plt.xlabel("Subfolder")
#     plt.ylabel("Number of Images")
#     plt.title("Number of Images per Subfolder")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()

#     # Vẽ biểu đồ tròn
#     plt.figure(figsize=(8, 8))
#     plt.pie(counts, labels=subfolders, autopct="%1.1f%%", startangle=140)
#     plt.title("Distribution of Images across Subfolders", pad=20)
#     plt.axis("equal")
#     plt.show()


# # Ví dụ sử dụng hàm
# parent_folder_path = r"F:\AI\BTL_hau\datasets\new_dataset_image"
# image_counts, total_images = count_images_in_subfolders(parent_folder_path)

# # In ra số lượng ảnh trong từng thư mục con và tổng số ảnh
# for folder_name, count in image_counts.items():
#     print(f"Folder '{folder_name}' contains {count} image(s)")
# print(f"Total number of images: {total_images}")

# # Vẽ biểu đồ
# plot_image_distribution(image_counts)

import os
from PIL import Image
import matplotlib.pyplot as plt


def count_images_in_subfolders(parent_folder):
    total_images = 0
    subfolder_image_counts = {}
    resolution_data = []

    # Duyệt qua các thư mục con trong thư mục cha
    for subdir, _, files in os.walk(parent_folder):
        # Lấy tên thư mục con
        folder_name = os.path.basename(subdir)

        # Lọc ra các file ảnh (có đuôi .jpg, .jpeg, .png)
        image_files = [
            f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        # Đếm số lượng ảnh trong thư mục con hiện tại
        image_count = len(image_files)
        if image_count > 0:
            subfolder_image_counts[folder_name] = image_count
            total_images += image_count

            # Lấy độ phân giải và kích thước ảnh
            for image_file in image_files:
                image_path = os.path.join(subdir, image_file)
                with Image.open(image_path) as img:
                    width, height = img.size
                    file_size = (
                        os.path.getsize(image_path) / 1024
                    )  # Kích thước tính bằng KB
                    resolution_data.append((width, height, file_size))

    return subfolder_image_counts, total_images, resolution_data


def plot_image_distribution(image_counts, resolution_data):
    # Vẽ biểu đồ cột
    subfolders = list(image_counts.keys())
    counts = list(image_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(subfolders, counts, color="skyblue")
    plt.xlabel("Subfolder")
    plt.ylabel("Number of Images")
    plt.title("Number of Images per Subfolder")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Vẽ biểu đồ tròn
    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=subfolders, autopct="%1.1f%%", startangle=140)
    plt.title("Distribution of Images across Subfolders", pad=20)
    plt.axis("equal")
    plt.show()

    # Vẽ biểu đồ phân tán cho độ phân giải và kích thước ảnh
    widths, heights, file_sizes = zip(*resolution_data)
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(widths, heights, c=file_sizes, cmap="viridis", alpha=0.6)
    plt.colorbar(scatter, label="File size (KB)")
    plt.xlabel("Width (pixels)")
    plt.ylabel("Height (pixels)")
    plt.title("Resolution and File Size of Images")
    plt.tight_layout()
    plt.show()


# Ví dụ sử dụng hàm
parent_folder_path = r"F:\AI\BTL_hau\datasets\new_dataset_image"
image_counts, total_images, resolution_data = count_images_in_subfolders(
    parent_folder_path
)

# In ra số lượng ảnh trong từng thư mục con và tổng số ảnh
for folder_name, count in image_counts.items():
    print(f"Folder '{folder_name}' contains {count} image(s)")
print(f"Total number of images: {total_images}")

# Vẽ biểu đồ
plot_image_distribution(image_counts, resolution_data)
