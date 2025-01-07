import serial
import time

# UART settings
serial_port = "COM3"  # Replace with your COM port
baud_rate = 2400 
data_to_send = """
Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one.
In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs," Rajan said in the note." Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently.
"""  

ser = serial.Serial(serial_port, baud_rate, timeout=1)

def calculate_speed(start_time, num_bits_transferred):
    elapsed_time = time.time() - start_time  
    speed = num_bits_transferred / elapsed_time  
    return speed

def send_data(data):
    start_time = time.time()
    num_bits_transferred = 0
    for byte in data.encode('utf-8'):  
        ser.write(byte.to_bytes(1, 'little'))  
        num_bits_transferred += 8  
        time.sleep(1 / baud_rate)  
        
        speed = calculate_speed(start_time, num_bits_transferred)
        print(f"Data Transmission Speed: {speed:.2f} bits/sec", end='\r')

         print("\nData sent successfully.")

      send_data(data_to_send)

    def receive_data():
    start_time = time.time()
    num_bits_transferred = 0
    print("\nReceiving data from MCU...")

    print("\nSucessfully received")

    while True:
        data = ser.read(1)  
        if data:
            print(data.decode('utf-8'), end='')  
            num_bits_transferred += 8
            speed = calculate_speed(start_time, num_bits_transferred)
            print(f"\nData Reception Speed: {speed:.2f} bits/sec", end='\r')
        if data == b'\n':  
            break

receive_data()

ser.close()
