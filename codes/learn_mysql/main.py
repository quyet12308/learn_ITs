import mysql.connector
from mysql.connector import Error

try:
    # Kết nối tới database
    connection = mysql.connector.connect(
        host="113.190.240.134",  # Thay bằng IP server của bạn, ví dụ: 'localhost' nếu chạy local
        port=8051,  # Cổng mà bạn đã ánh xạ
        database="my_database",  # Tên database đã tạo trong Dockerfile
        user="my_user",  # Tên người dùng đã đặt trong Dockerfile
        password="my_password",  # Mật khẩu đã đặt trong Dockerfile
    )

    if connection.is_connected():
        print("Kết nối thành công tới MySQL Database")

        # Lấy thông tin server
        db_Info = connection.get_server_info()
        print("Phiên bản MySQL Server:", db_Info)

        # Tạo một con trỏ để thực thi câu lệnh SQL
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("Đang kết nối tới database:", record)

except Error as e:
    print("Lỗi khi kết nối tới MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Đã đóng kết nối MySQL")
