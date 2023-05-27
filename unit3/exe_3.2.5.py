def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return "__CONTENT_START__\n" + content + "\n__CONTENT_END__"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"


if __name__ == '__main__':
    print(read_file("D:\Desktop\python\one_lined_file.txt"))