# RuCo-BERT

This repository contains code and data for training and inference of a new coreference resolution model trained on the RuCoCo corpus (see https://github.com/vdobrovolskii/rucoco). <br>
First, to install dependcies run <code>pip install -r requirements.txt</code>. Although the recommended pytorch version for AllenNLP 2.2.0 is 1.8.1, it is better to additionally run <code>pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html</code>.<br><br>
To inference the model, download weights from: https://dl.dropbox.com/s/2m0c4o220pr1rfn/RucocoAncor_rubertb_a150_s20_sw04.tar.gz?dl=0 <br><br>
Then run: <br>
<code>allennlp evaluate --include-package rucoref RucocoAncor_rubertb_a150_s20_sw04.tar.gz data\test.conll --output-file metrics_on_test.json --predictions-output-file predictions.json</code><br><br>
In order to train the model from scratch, use the command:<br>
<code>allennlp train --include-package rucoref coref_bertbase_lstm.jsonnet -s output_models</code>.<br><br>
<hr>
# Training process <br>
![alt text](https://github.com/gleb-skobinsky/RuCo-BERT/blob/master/training.jpg?raw=true)
