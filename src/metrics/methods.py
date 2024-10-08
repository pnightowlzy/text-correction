import distance
import jieba

jieba.initialize()

def edit_distance(s1, s2):
    return distance.levenshtein(s1, s2)

def evaluate_by_edit_distance(hypothesis, references):
    """Evaluate the model by calculating its edit distance to a reference"""    
    total_distance, total_length = 0, 0
    total_correct = 0 
    for i in range(len(references)):
        dist = edit_distance(hypothesis[i], references[i])
        total_distance += dist
        total_length += len(references[i])

        if dist == 0:
            total_correct += 1
    
    WER = total_distance / total_length
    SER = total_correct / len(references)

    return WER.__format__("0.4f"), SER.__format__("0.4f")

def evaluate_by_bleu(hypothesis, references):
    from nltk import bleu_score
    references = [jieba.lcut(r) for r in references]
    hypothesis = [jieba.lcut(h) for h in hypothesis]
    
    def bleu(ref, candidates):
        return bleu_score.sentence_bleu([ref], candidates, weights=(0.25, 0.25, 0., 0))
    
    scores = []
    for i in range(len(references)):
        score = bleu(references[i], hypothesis[i])
        scores.append(score)
        
    
    return "{:.3f}".format(sum(scores) / len(scores) * 100)
    
    
if __name__ == '__main__':
    hypothesis = ['你好，再见', '你好世界']
    references = ['您好吗，再见', '你好世界']
    print(evaluate_by_bleu(hypothesis, references))
    print(evaluate_by_edit_distance(hypothesis, references))