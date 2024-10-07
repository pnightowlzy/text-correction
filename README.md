# text-correction
ASR文本纠错实验


## Dataset
https://github.com/tzyll/ChineseHP

### Data samples
```
[aishell-1]
train_data: 120098
test_data: 7176
dev_data: 14326

[sample]
{'id': 'BAC009S0039W0150', 'nbest': ['一线城市土地合计成交三百二十五宗', '一线城市土地合计成交三百二十五纵', '一线城市土地合计成交三百二十五座', '一线城市土地核计成交三百二十五宗', '依线城市土地合计成交三百二十五宗', '一线城市土地合计成交三百二十五踪', '一线城市土地合计成交三百十五宗', '一线城市土地合计成交三百二十五中', '一线城市土地合计成交三百二十五公', '一线城市土地合计成交三百二十五宵'], 'nbest_pinyin': ['y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai er sh i w u z ong', 'y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai er sh i w u z ong', 'y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai er sh i w u z uo', 'y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai er sh i w u z ong', 'y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai er sh i w u z ong', 'y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai er sh i w u z ong', 'y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai sh i w u z ong', 'y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai er sh i w u zh ong', 'y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai er sh i w u g ong', 'y i x ian ch eng sh i t u d i h e j i ch eng j iao s an b ai er sh i w u x iao'], 'text': '一线城市土地合计成交三百二十五宗'}
```

## Evaluate
### Top 1 
|数据集	|WER|	SER	|BLEU|
|----	|---	|----	|----|
|aishell-1	|0.0584	|0.5407	|90.003|
|aishell-4	|0.2528	|0.1905	|54.891|
|kespeec	|0.2984	|0.1531	|62.342|
|wenetspeech	|0.1217	|0.3488	|77.622|

### NBest Selection LLM 




# References
https://arxiv.org/pdf/2407.01909
