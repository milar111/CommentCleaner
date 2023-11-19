def remove_comments(input_file):
    in_comment_block = False
    output_lines = []

    with open(input_file, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if not in_comment_block:
                if stripped_line.startswith("'''") or stripped_line.startswith('"""'):
                    in_comment_block = True
                elif stripped_line.startswith("#"):
                    continue
                else:
                    output_lines.append(line)
            else:
                if stripped_line.endswith("'''") or stripped_line.endswith('"""'):
                    in_comment_block = False

    with open(input_file, 'w') as file:
        file.writelines(output_lines)

if __name__ == "__main__":
    file_name = "test.py"  # Paste your file name here
    remove_comments(file_name)
    print("The comments have been successfully removed from :", file_name)
