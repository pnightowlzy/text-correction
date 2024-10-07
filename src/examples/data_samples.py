import sys
import os
from utils import *

# 获取当前文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取上层目录
parent_dir = os.path.join(current_dir, '..')

root_path = os.path.join(parent_dir, "data/ChineseHP/data")

bus_list = os.listdir(root_path)

print("dataset:", bus_list)

def process_(parent_path, bus):
    bus_path = os.path.join(parent_path, bus)
    train = os.paht.join(bus_path, "train")


