import os


days_range = range(1, 26)
file_names = ["challenge1.py", "challenge2.py"]

# Create the folders and files
for day in days_range:
    folder_name = f"Day{day:02}"
    os.makedirs(folder_name, exist_ok=True)

    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as file:
            pass