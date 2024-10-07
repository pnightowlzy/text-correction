import sys
import os
from utils import *



def process(parent_path, bus):        
    bus_path = os.path.join(parent_path, bus)
    if "aishell" in bus:
        train = os.path.join(bus_path, "train")
        test = os.path.join(bus_path, "test")
        dev = os.path.join(bus_path, "dev")
    elif "wenetspeech" == bus:
        train = os.path.join(bus_path, "train_200k")
        test = os.path.join(bus_path, "test_net")
        dev = os.path.join(bus_path, "dev")
    elif "kespeech" == bus:
        train = os.path.join(bus_path, "train_200k")
        test = os.path.join(bus_path, "test")
        dev = os.path.join(bus_path, "dev")

    train_data = process_raw_data(train)
    test_data = process_raw_data(test)
    dev_data = process_raw_data(dev)

    print(f"[{bus}]\ntrain_data: {len(train_data)}\ntest_data: {len(test_data)}\ndev_data: {len(dev_data)}\n")
    print(f"[sample]\n{train_data[0]}\n")
    return train_data, test_data, dev_data


def process_raw_data(parent_path):
    nbest = os.path.join(parent_path, "nbest.txt")
    nbest_pinyin = os.path.join(parent_path, "nbest_pinyin.txt")
    text = os.path.join(parent_path, "text")

    nbest_dict = load_data(nbest)
    nbest_pinyin_dict = load_data(nbest_pinyin)
    text_dict = load_text(text)

    assert len(nbest_dict) == len(nbest_pinyin_dict) == len(text_dict)

    data = []

    for key, val in nbest_dict.items():
        nbest_ele = [v.strip() for v in val]
        nbest_pinyin_ele = [v.strip() for v in nbest_pinyin_dict[key]]
        text_ele = text_dict[key].strip()

        data.append({ 
            "id": key, 
            "nbest": nbest_ele,
            "nbest_pinyin": nbest_pinyin_ele,
            "text": text_ele
            })

    return data
    


def load_data(data_path):
    lines = read_text_list(data_path)
    lines = {line.split()[0]: (" ".join(line.split()[1:])).split("|") for line in lines}
    return lines


def load_text(data_path):
    lines = read_text_list(data_path)
    lines = {line.split()[0]: " ".join(line.split()[1:]) for line in lines}
    return lines


def load_bus_data():
    # 获取当前文件所在的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取上层目录
    parent_dir = os.path.join(current_dir, '..')

    root_path = os.path.join(parent_dir, "data/ChineseHP/data")

    bus_list = os.listdir(root_path)
    
    store_path = os.path.join(parent_dir, "data/processed")
    
    data_dict = {}
    
    if os.path.exists(store_path) is False:
        print('create dir: ', store_path)
        os.mkdir(store_path)
    
    for bus in bus_list:
        train_data, test_data, dev_data = process(root_path, bus)
        bus_data = {
            'train': train_data,
            'test': test_data,
            'dev': dev_data
        }
    
        write_json(os.path.join(store_path, f'{bus}.json'), bus_data)
        
    return data_dict

def main(): 
    load_bus_data()

if __name__ == "__main__":
    main()