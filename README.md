# RuCo-BERT

This repository contains code and data for training and inference of a new coreference resolution model trained on the RuCoCo corpus (see https://github.com/vdobrovolskii/rucoco). <br><br>
First, to install dependcies run <code>pip install -r requirements.txt</code>. Although the recommended pytorch version for AllenNLP 2.2.0 is 1.8.1, it is better to additionally run <code>pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html</code>. This will ensure support of 48 anf 80 GB GPUs that is necessary for training with the command below. Coreference resolution is notorious for its extreme computational complexity.<br><br>
To inference the model, download weights from: https://dl.dropbox.com/s/2m0c4o220pr1rfn/RucocoAncor_rubertb_a150_s20_sw04.tar.gz?dl=0 <br><br>
Then run: <br>
<code>allennlp evaluate --include-package rucoref RucocoAncor_rubertb_a150_s20_sw04.tar.gz data\test.conll --output-file metrics_on_test.json --predictions-output-file predictions.json</code><br><br>
In order to train the model from scratch, use the command:<br>
<code>allennlp train --include-package rucoref coref_bertbase_lstm.jsonnet -s output_models</code>.<br>
<h1>Results</h1>
Results are calculated by default allennlp functions and tend to be slightly lower than the AVG scores computed with reference coreference scores (https://github.com/conll/reference-coreference-scorers).<br><br>

| Set           | PRECISION | RECALL    | F1-SCORE|
|---------------|-----------|-----------|---------|
| train         | 96.1      | 89.3      | 92.5    |
|development    | 77.8      | 72.8      | 75.2    |
|test           | 81.1      | 78.2      | 79.6    |

<h1>Training process</h1>
Development F1 never exceeds the threshold of around 75%, even though training F1 increases steadily.

![alt text](https://github.com/gleb-skobinsky/RuCo-BERT/blob/master/training.jpg?raw=true)
