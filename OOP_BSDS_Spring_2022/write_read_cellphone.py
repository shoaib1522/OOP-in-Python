import struct
import cellphone

FILENAME = 'cellphones.dat'

def main():
	again = 'y'
	output_file = open('cellphones.bin', 'wb+')
	output_file.write(cellphone.CellPhone('Sony', '123', 25000).get_binary_string())
	output_file.write(cellphone.CellPhone('Sony', '125', 35000).get_binary_string())
	output_file.write(cellphone.CellPhone('Sony', '124', 30000).get_binary_string())
	output_file.close()
	
	input_file = open('cellphones.bin', 'rb+')
	s =	input_file.read(34)
	print(cellphone.CellPhone(s[0:20],s[20:30],struct.unpack('i', s[30:34])[0]))
	s =	input_file.read(34)
	print(cellphone.CellPhone(s[0:20],s[20:30],struct.unpack('i', s[30:34])[0]))
	s =	input_file.read(34)
	print(cellphone.CellPhone(s[0:20],s[20:30],struct.unpack('i', s[30:34])[0]))
	input_file.close()

main()
