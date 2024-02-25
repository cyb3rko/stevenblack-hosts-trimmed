import os
import pathlib
import glob
import shutil


def cleanup():
    if os.path.isdir("alternates"):
        shutil.rmtree("alternates")
    if os.path.isdir("hosts"):
        shutil.rmtree("hosts")
    prev_files = glob.glob("hosts*")
    for old_file in prev_files:
        print("Remove", old_file)
        os.remove(old_file)


def extract_comment(next_line):
    if next_line[0] == "#":
        return next_line, next_line
    elif next_line.startswith("0.0.0.0") and next_line.__contains__("#"):
        comment_index = next_line.index("#")
        return next_line[comment_index:], next_line[:comment_index]
    else:
        return None, next_line


def extract_host(next_line):
    if next_line.startswith("0.0.0.0"):
        return next_line[8:]
    else:
        return None


def get_new_file_name(filename):
    return filename.replace("stevenblack-hosts/", "") + str(file_index)


def get_file_directory(filename):
    filename = get_new_file_name(filename)
    print(filename[:filename.rfind("/")])
    return filename[:filename.rfind("/")]


cleanup()
files = glob.glob('stevenblack-hosts/alternates/**/hosts', recursive=True)
files.append("stevenblack-hosts/hosts")
for file in files:
    process_description = True
    process = False
    last_line_empty = False
    lines = 0
    file_index = 0
    input_file = open(file, "r")
    pathlib.Path(get_file_directory(file)).mkdir(parents=True, exist_ok=True)
    output_file = open(get_new_file_name(file), "w")

    for index, line in enumerate(input_file.readlines()):
        # Copy file description
        if process_description and not line.startswith("# ==="):
            output_file.write(line)
            continue
        elif process_description:
            output_file.write(line)
            process_description = False

        # Exit after last entry
        if line == "# blacklist\n":
            break

        # Ignore lines before first entry
        if not process:
            if line == "# End of custom host records.\n":
                process = True
                print("Start processing")
            continue

        # Copy empty lines
        if line == "\n":
            if not last_line_empty:
                last_line_empty = True
                output_file.write("\n")
            continue

        last_line_empty = False
        if line.endswith("\n"):
            line = line[:-1]

        # Processing line
        comment, line = extract_comment(line)
        if comment is not None:
            comment_found = True
            output_file.write(comment + "\n")
        else:
            comment_found = False
        host = extract_host(line)
        if host:
            host_found = True
            if lines == 130000:
                file_index += 1
                output_file = open(get_new_file_name(file), "w")
                lines = 0
            output_file.write(host + "\n")
            lines += 1
        else:
            host_found = False

        if not host_found and not comment_found:
            print(f"Ignoring line {index}: {line}")