import struct
import cellphone

FILENAME = 'cellphones.dat'

def main1():
    output_file = open('cellphones.bin', 'wb+')
    output_file.write(cellphone.CellPhone('Sony', '123', 25000).get_binary_string())
    output_file.write(cellphone.CellPhone('Sony', '125', 35000).get_binary_string())
    output_file.write(cellphone.CellPhone('Sony', '124', 30000).get_binary_string())
    output_file.close()
    input_file = open('cellphones.bin', 'rb+')
    s = input_file.read(34)
    print(cellphone.CellPhone(str(s[0:20],'utf-8'),str(s[20:30],'utf-8'),struct.unpack('i', s[30:34])[0]))
    s = input_file.read(34)
    print(cellphone.CellPhone(str(s[0:20],'utf-8'),str(s[20:30],'utf-8'),struct.unpack('i', s[30:34])[0]))
    s = input_file.read(34)
    print(cellphone.CellPhone(str(s[0:20],'utf-8'),str(s[20:30],'utf-8'),struct.unpack('i', s[30:34])[0]))
    input_file.close()

def main():
    output_file = open('cellphones.bin', 'wb+')
    s = cellphone.CellPhone('Sony', '123', 25000).get_binary_string()
    s += cellphone.CellPhone('Sony', '125', 35000).get_binary_string()
    s += cellphone.CellPhone('Sony', '124', 30000).get_binary_string()
    output_file.write(s)
    output_file.close()
    input_file = open('cellphones.bin', 'rb+')
    s = input_file.read()
    input_file.close()
    for i in range(0, len(s), 34):
        print(cellphone.CellPhone(str(s[i:i+20],'utf-8'),str(s[i+20:i+30],'utf-8'),struct.unpack('i', s[i+30:i+34])[0]))
    
    
main()

        
