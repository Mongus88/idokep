import csv
from datetime import datetime


def time_stamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def save_txt(txt_data, prefix):
    filename = f"{prefix}_{time_stamp()}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Mit vegyek fel ma? : {txt_data}")


def save_csv(csv_data, prefix):
    filename = f"{prefix}_{time_stamp()}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Dátum", "Fog esni az eső?"])
        writer.writeheader()
        writer.writerows(csv_data)


def save_screenshot(image, prefix):
    filename = f"{prefix}_{time_stamp()}.png"
    image.screenshot(path=filename)
