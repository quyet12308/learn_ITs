import os


def count_images(folder_path):
    """Đếm số lượng ảnh trong một thư mục.

    Nếu thư mục chứa các thư mục con, hàm sẽ tiếp tục đếm ảnh trong các thư mục con đó.

    Args:
      folder_path (str): Đường dẫn đến thư mục.

    Returns:
      int: Tổng số lượng ảnh trong thư mục.
      dict: Từ điển chứa số lượng ảnh của từng thư mục con.
    """

    # Kiểm tra xem đường dẫn có phải là thư mục không.
    if not os.path.isdir(folder_path):
        raise ValueError("Đường dẫn không phải là thư mục.")

    # Khởi tạo số lượng ảnh tổng cộng và từ điển chứa số lượng ảnh của từng thư mục con.
    total_count = 0
    subfolder_counts = {}

    # Duyệt qua các mục trong thư mục.
    for item in os.listdir(folder_path):
        # Lấy đường dẫn đầy đủ của mục.
        item_path = os.path.join(folder_path, item)

        # Kiểm tra xem mục là tệp hay thư mục.
        if os.path.isfile(item_path):
            # Nếu là tệp, kiểm tra xem đó có phải là ảnh không.
            if item_path.endswith((".jpg", ".JPG", ".jpeg", ".png")):
                # Nếu là ảnh, tăng số lượng ảnh tổng cộng.
                total_count += 1
        elif os.path.isdir(item_path):
            # Nếu là thư mục, đếm ảnh trong thư mục đó.
            subfolder_counts[item] = count_images(item_path)

    # Trả về số lượng ảnh tổng cộng và từ điển chứa số lượng ảnh của từng thư mục con.
    return total_count, subfolder_counts


# folder_path = r"F:\AI\dataset_cassava\dataset_download_from_kaggle_2"
folder_path = r"F:\AI\dataset_cassava\train_dataset_for_classtifion_with_5_class"
# folder_path = r"F:\AI\dataset_cassava\dataset_anh_hung_chup_4"
a, b = count_images(folder_path=folder_path)
print(a)
print(b)
