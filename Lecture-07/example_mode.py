def example_w_plus():
    with open('example_w+.txt', 'w+') as file:
        file.write('Hello, World!\n')
        file.write('This is a test file.\n')

        file.seek(0)

        content = file.read()
        print("Content of the file:")
        print(content)

example_w_plus()