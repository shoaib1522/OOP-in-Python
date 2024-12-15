def read_file1_and_write_into_file2_replace_numbers_with_hyphen(file1, file2):
    for line in file1:
        for c in line:
            if c >= '0' and c <= '9' :
                file2.write('-')
            else:
                file2.write(c)

def main():
    #in windows complete path may not required, however, it is required in Linux according to my settings
    file1 = open('/home/mateen/Documents/Python tuts/Solution Practice 08/text.txt','r')
    file2 = open('/home/mateen/Documents/Python tuts/Solution Practice 08/text_without_numbers.txt','w+')
    read_file1_and_write_into_file2_replace_numbers_with_hyphen(file1, file2)
    file1.close()
    file2.close()

main()