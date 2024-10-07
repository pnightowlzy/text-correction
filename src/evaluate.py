from metrics.methods import evaluate_by_edit_distance, evaluate_by_bleu
import os
from utils import *
import sys
print(sys.path)
def main():
    path = "data/processed"
    bus_list = os.listdir(path)
    
    for bus in bus_list:
        print("Evaluating {}".format(bus))
        eval_data = load_evaluate_data(os.path.join(path, bus))
        
        test_data = eval_data["test"]
        
        
        # top1 score                
        hypothesis = ["".join(nb["nbest"][0]) for nb in test_data]
        references = [text["text"] for text in test_data]
        
        WER, SER = evaluate_by_edit_distance(hypothesis, references)
        BLEU = evaluate_by_bleu(hypothesis, references)
        
        print(f"[WER]: {WER}\n[SER]: {SER}\n[BLEU]: {BLEU}\n")

def evaluate_with_llm_selection(bus):
    root_path = "data/processed"
    bus_path = os.path.join(root_path, bus)
    eval_data = load_evaluate_data(bus_path)
    
    
    
        
def load_evaluate_data(path):
    data = read_json(path)
    return data
    
if __name__ == "__main__":
    main()