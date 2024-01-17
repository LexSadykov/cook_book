import os

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()
    
def write_sorted_file(sorted_file, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for file_info in sorted_file:
            output_file.write(file_info["name"] + "\n")
            output_file.write(str(file_info["line_count"]) + "\n")
            output_file.writelines(file_info["content"])
            output_file.write("\n")

def merge_files(folder_path, output_file_path):
    files = os.listdir(folder_path)

    file_info_list = []
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            content = read_file(file_path)
            file_info_list.append({
                "name": file_name,
                "line_count": len(content),
                "content": content
            })

    sorted_files = sorted(file_info_list, key=lambda x: x["line_count"])

    write_sorted_file(sorted_files, output_file_path)

folder_path = r"C:\Users\Леша\Desktop\Git-проекты\cook_book\task_3"
output_file_path = r"C:\Users\Леша\Desktop\Git-проекты\cook_book\task_3\final.txt"

merge_files(folder_path, output_file_path)