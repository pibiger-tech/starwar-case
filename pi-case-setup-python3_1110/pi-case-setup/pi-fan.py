#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 INNOMAKER.
# http://www.inno-maker.com/
#
# Licensed under the GNU General Public License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.gnu.org/licenses/gpl-2.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# tutorials url: http://www.inno-maker.com/

__author__ = 'Jack'
__license__  = 'Copyright (c) 2021 INNOMAKER'

import time
#import smbus
import smbus2
# speed range 30 --- 100  
speed_base = 50
speed_step = 1.5
#speed_step = 2
threshold_temp = 40
address = 0x18
dc_current=50

def get_cpu_temp():
    temp_file = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = temp_file.read()
    temp_file.close()
    return float(cpu_temp) / 1000

def get_scaling_cur_freq():
    temp_file = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq" )
    scaling_cur_freq = temp_file.read()
    temp_file.close()
    return float(scaling_cur_freq) / 1000

def get_scaling_max_freq():
    temp_file = open( "/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq" )
    scaling_max_freq = temp_file.read()
    temp_file.close()
    return float(scaling_max_freq) / 1000

#if __name__ == "__main__":
# I2C BUS 1
#bus=smbus.SMBus(1)
bus=smbus2.SMBus(1)
scaling_max_freq = get_scaling_max_freq()
speed = 0
while True:
    current_temp = get_cpu_temp()
    scaling_cur_freq = get_scaling_cur_freq()

    if (current_temp < threshold_temp):
            speed = 0
    else:
            speed = speed_base + (current_temp - threshold_temp) * speed_step

    if (scaling_cur_freq == scaling_max_freq):
            pass
            speed = 100

    if speed > 100:
            speed = 100

    dc=int(speed)
    if(dc!=dc_current):
      bus.write_byte(address,0x8)
      bus.write_byte(address,dc)
      bus.read_byte(address)
      dc_current=dc


#    print("TEMP: %.2f, FREQ: %d/%d MHz, FAN SPEED: %d%%" % (current_temp, scaling_cur_freq, scaling_max_freq, speed))
    time.sleep(3)

