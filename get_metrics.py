import os
import re
import pandas as pd
df = pd.DataFrame({'epoch': [], 'training_f1': [], 'dev_f1': []})
with open(r'RucocoAncor_rubertb_a150_s20_sw04.log', encoding='utf-8') as file:
    logs = file.read()
    file.close()
finder = "allennlp.training.callbacks.console_logger - coref_f1"
for num, instance in enumerate(re.finditer(finder, logs)):
    current_metrics = logs[instance.end():instance.end() + 35]
    train_f1 = float(current_metrics.split()[1])
    dev_f1 = float(current_metrics.split()[3])
    df.loc[num] = list([num, train_f1, dev_f1])

loss_finder = 'allennlp.training.callbacks.console_logger - loss'
ovtrain_loss = []
ovdev_loss = []
for loss in re.finditer(loss_finder, logs):
    current_loss = logs[loss.end():loss.end() + 40]
    train_loss = float(current_loss.split()[1])
    dev_loss = float(current_loss.split()[3])
    ovtrain_loss.append(train_loss)
    ovdev_loss.append(dev_loss)
df["training_loss"] = ovtrain_loss
df["dev_loss"] = ovdev_loss
print(df)

df.to_csv('metrics_and_loss.csv')


