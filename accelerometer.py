import time
import board
import adafruit_adxl34x
import smbus
try:
    from typing import Tuple, Dict

    # This is only needed for typing
    import busio
except ImportError:
    pass
from struct import unpack
i2c = board.I2C()  # uses board.SCL and board.SDA
accelerometer = adafruit_adxl34x.ADXL345(i2c)
print(accelerometer.acceleration)
while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(0.1)
# print(accelerometer.data_rate)
# print(accelerometer.range)

ADXL345_I2C_ADDR = 0x53
POWER_CTL = 0x2D
DATA_FORMAT = 0x31
DATAX0 = 0x32
bus_num = 1
G=9.8
measure_mode = True
def __init__(self, bus_num=1):
    self.bus = smbus.SMBus(bus_num)
    # Set range to +/- 16g and FULL_RES bit
    self.bus.write_byte_data(ADXL345_I2C_ADDR, DATA_FORMAT, 0x0B)
    # Turn on the acscelerometer
    self.bus.write_byte_data(ADXL345_I2C_ADDR, POWER_CTL, 0x08)

buffer = DATAX0 & 0xFF
# i2c_device.I2CDevice(i2c, address)
if measure_mode:
    command = int('00001000',2)
    smbus.SMBus(bus_num).write_i2c_block_data(ADXL345_I2C_ADDR,0x2D,[command])
    time.sleep(0.5)
elif measure_mode == False:
    # print('hello')
    command = int('00000100',2)
    smbus.SMBus(bus_num).write_i2c_block_data(ADXL345_I2C_ADDR,0x2D,[command])
    time.sleep(0.5)

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

BW_PRW_command = int('00000010',2)
write_BW_PWR_Mode = smbus.SMBus(1).write_i2c_block_data(ADXL345_I2C_ADDR,0x2C,[BW_PRW_command])

query_BW_PWR_Mode = smbus.SMBus(1).read_i2c_block_data(ADXL345_I2C_ADDR,0x2C,1)

activity_command = int('00010000',2)
# print(activity_command)
write_activity_Mode = smbus.SMBus(1).write_i2c_block_data(ADXL345_I2C_ADDR,0x27,[activity_command])
query_activity = smbus.SMBus(1).read_i2c_block_data(ADXL345_I2C_ADDR,0x27,1)

threshold_acceleration = 7
# threshold_acceleration_binary = '{0:08b}'.format(threshold_acceleration/62.5e-3)
threshold_acceleration_command = int(threshold_acceleration//62.5e-3)#int(threshold_acceleration_binary,2)
print(threshold_acceleration_command)
write_activity_threshold = smbus.SMBus(1).write_i2c_block_data(ADXL345_I2C_ADDR,0x24,[threshold_acceleration_command])
query_activity_threshold = smbus.SMBus(1).read_i2c_block_data(ADXL345_I2C_ADDR,0x24,1)

interupt_command = int('00010000',2)
write_interupt_status = smbus.SMBus(1).write_i2c_block_data(ADXL345_I2C_ADDR,0x2E,[interupt_command])
query_interupt_status = smbus.SMBus(1).read_i2c_block_data(ADXL345_I2C_ADDR,0x2E,1)
print(query_interupt_status)