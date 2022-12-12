import numpy as np
challenge_input = "d6.txt"

with open(challenge_input, "r") as input_file:
    datastream_buffer = input_file.readline()

def find_packet_marker(datastream_buffer):
    start = 0
    end_of_4 = 4
    index_of_first_in_group = 0

    for i in datastream_buffer:
        sequence_of_4 = datastream_buffer[start : end_of_4]    
        array_of_4 = np.array(list(sequence_of_4))
        unique_of_4 = np.unique(array_of_4)
 
        if len(unique_of_4) == 4:
            chars_before_packet_marker = index_of_first_in_group + 4
            break
        else:
            start += 1
            end_of_4 += 1
            index_of_first_in_group += 1

    return chars_before_packet_marker

def find_msg_marker(datastream_buffer):
    start = 0
    end_of_14 = 14
    index_of_first_in_group = 0

    for i in datastream_buffer:
        sequence_of_14 = datastream_buffer[start : end_of_14]
        array_of_14 = np.array(list(sequence_of_14))
        unique_of_14 = np.unique(array_of_14)
      
        if len(unique_of_14) == 14:
            chars_before_message_marker = index_of_first_in_group + 14
            break
        else:
            start += 1
            end_of_14 +=1
            index_of_first_in_group += 1
           
    return chars_before_message_marker

chars_before_packet_marker = find_packet_marker(datastream_buffer)
chars_before_message_marker = find_msg_marker(datastream_buffer)

print(f"{chars_before_packet_marker} characters processed before detection of first start-of-packet marker; {chars_before_message_marker} processed before first start-of-message marker")
