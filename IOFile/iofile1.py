# Write a Python program to read an entire text file. 
# f = open(filename, mode)
'''
Mode:
    - r: open an existing - for read                - Error when no existing
    - w: open an existing - for write - overriden   - Create a new one when no existing
    - a: open an existing - appending               - Create a new one when no existing
    - r+: read and write data into a file - overridden
    - w+: write and read data - override existing data
    - a+: append and read data from a file - wont override
'''
def file_input_processing():
    file = open("userInput.txt", 'a+')
    file.write(input("Input you number: "))
    # file.close()
    # print (file)
    return file
def file_output_processing(file):
    for each in file:
        print("Hell")
        print(each, end='')
    file.close()
if __name__ == '__main__':
    file = open('./sample.txt', 'r')
    content = 'Hello Every one\n'
    # for each in file:
    #     print(each, end='')
    # print(file.read())
    # print(file.readline(), end='')
    # print(file.readline(), end='')

    for each in file:
        content += each

    # content += file.readline()
    # content += file.readline()
    # content += file.readline()

    print (content)
    file1 = file_input_processing()
    file_output_processing(file1)
    file.close()