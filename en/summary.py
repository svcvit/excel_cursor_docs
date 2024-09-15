import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                first_line = file.readline().strip()
            
            if first_line.startswith('# '):
                new_name = re.sub(r'[^\w\-]', '-', first_line[2:]) + '.md'
                new_path = os.path.join(directory, new_name)
                os.rename(file_path, new_path)

def update_summary(directory, summary_file):
    links = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                first_line = file.readline().strip()
            
            if first_line.startswith('# '):
                title = first_line[2:]
                link = f"* [{title}](Example/{filename})"
                links.append(link)
    
    with open(summary_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    example_section = "## Usage Examples\n\n" + "\n".join(links)
    new_content = re.sub(r'## Usage Examples.*', example_section, content, flags=re.DOTALL)
    
    with open(summary_file, 'w', encoding='utf-8') as file:
        file.write(new_content)

# 执行重命名操作
example_dir = 'Example'
rename_files(example_dir)

# 更新 SUMMARY.md 文件
summary_file = 'SUMMARY.md'
update_summary(example_dir, summary_file)

print("文件重命名和 SUMMARY.md 更新完成。")