import time
import board
import adafruit_adxl34x
import smbus
# i2c = board.I2C()  # uses board.SCL and board.SDA
# accelerometer = adafruit_adxl34x.ADXL345(i2c)

# while True:
#     print("%f %f %f"%accelerometer.acceleration)
#     time.sleep(0.1)
# print(accelerometer.data_rate)
# print(accelerometer.range)
ADXL345_I2C_ADDR = 0x53
POWER_CTL = 0x2D
DATA_FORMAT = 0x31
DATAX0 = 0x32
bus_num = 1
G=9.8
def __init__(self, bus_num=1):
    self.bus = smbus.SMBus(bus_num)
    # Set range to +/- 16g and FULL_RES bit
    self.bus.write_byte_data(ADXL345_I2C_ADDR, DATA_FORMAT, 0x0B)
    # Turn on the acscelerometer
    self.bus.write_byte_data(ADXL345_I2C_ADDR, POWER_CTL, 0x08)

byte = smbus.SMBus(bus_num).read_i2c_block_data(ADXL345_I2C_ADDR, 0x32, 6)
format_command = int('00001000',2)
print(type(format_command))
data_format = smbus.SMBus(1).write_i2c_block_data(ADXL345_I2C_ADDR,0x31,[format_command]) # Need to insert class int at the 3rd output. hex(int()) will return a string which is not what we want. 
print(smbus.SMBus(1).read_i2c_block_data(ADXL345_I2C_ADDR,0x31,1))
print(byte)
x = (byte[5] << 8 | byte[4])# Converts value into 16 bits. 
print(x)
if x & (1 << 15):
    x = x - (1 << 16)
    x = (x * (4e-3)) * 1 * G # When setting the max resolution = 4mG/LSB. 
else:
    x = (x * (4e-3)) * 1 * G

power_mode = smbus.SMBus(bus_num).read_i2c_block_data(ADXL345_I2C_ADDR,0x2C,1)
# print(hex(power_mode[0]))
device_ID = smbus.SMBus(bus_num).read_i2c_block_data(ADXL345_I2C_ADDR,0x00,1)
# print(hex(device_ID[0]))
query_data_format = smbus.SMBus(1).read_i2c_block_data(ADXL345_I2C_ADDR,0x31,1)
print(x)