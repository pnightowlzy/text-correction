from metrics.methods import evaluate_by_edit_distance, evaluate_by_bleu, edit_distance
import os
from utils import *
from llm.openai_client import run
import jinja2
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
    bus_path = os.path.join(root_path, f"{bus}.json")
    eval_data = load_evaluate_data(bus_path)
    
    test_data = eval_data["test"]
    
    total_distance, total_length = 0, 0
    total_correct = 0
    
    promptTmpl = jinja2.Template(open("prompts/pinyin_regularzation_zh.txt", "r").read())
    
    for k, sample in enumerate(test_data):
        nbest = [f"{i}. {s}" for i, s in enumerate(sample['nbest'])]
        nbest_pinyin = [f"{i}. {s}" for i, s in enumerate(sample['nbest_pinyin'])]
        text = sample['text']
        
        # nbest 和 nbest_pinyin 渲染到prompt内， 得到最后的答案，进行解析
        # 比较最后的答案和标准答案，计算WER和SER
        nbest_str = "\n".join(nbest)
        nbest_pinyin_str = "\n".join(nbest_pinyin)
        
        prompt = promptTmpl.render({'nbest': nbest_str, 'nbest_pinyin': nbest_pinyin_str})
        
        messages = [
            {"role":"system","content":"""基于提供的 N-best 文本候选和 N-best 拼音转录,纠正文本并直接输出结果。
(Based on the provided N-best text candidates and N-best Pinyin transcriptions, correct the text and output the result directly.)"""},
            {"role":"user","content":"""## N-best 文本候选: (N-best text candidates) 
1. 今天天气很好 
2. 今天天气很早 
3. 今天天其很好 
4. 今天甜气很好 
5. 景天天气很好  

## N-best 拼音转录: (N-best Pinyin transcriptions) 
1. j in t ian t ian q i h en h ao 
2. j in t ian t ian q i h en z ao 
3. j in t ian t ian q i h en h ao 
4. j in t ian t ian q i h en h ao 
5. j ing t ian t ian q i h en h ao

## 输出格式, 请直接给出你修正后的文本
{"text": "you corrected text"}"""},
            {"role":"assistant","content":"""{"text": "今天天气很好"}"""},
            {"role":"user","content":prompt}
        ]
        
        print(prompt)
        
        result = run(messages=messages, model="Bowen_14B", response_format={"type": "json_object"})  
        
        print(result, text)      
        
        infer_text = json.loads(result)["text"]        
        
        dist = edit_distance(infer_text, text)
        
        if dist == 0:
            total_correct += 1
            
        total_distance += dist
        total_length += len(text)
        
        if k % 50 == 0:
            WER = total_distance / total_length
            SER = total_correct / (k + 1)
            print(f"[Step]: {k}, [WER]: {WER}, [SER]: {SER}")
    
    WER = total_distance / total_length
    SER = total_correct / len(test_data)
    print(f"[Final]: {k}, [WER]: {WER}, [SER]: {SER}")
        
def load_evaluate_data(path):
    data = read_json(path)
    return data
    
if __name__ == "__main__":
    evaluate_with_llm_selection("aishell-4")