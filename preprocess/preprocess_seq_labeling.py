import datasets
from datasets import ClassLabel, load_dataset
import os,json

def create_semi_seq_data(dataset_name='conll2003',dataset_config_name=None,dst_root='../data/'):
    
    dst_path = os.path.join(dst_root,dataset_name)
    if os.path.exists(dst_path) == False:
        os.mkdir(dst_path)

    raw_datasets = load_dataset(dataset_name, dataset_config_name)

    train_data = {}
    for i in range(raw_datasets['train'].num_rows-1):
        train_data[str(i)] = {}
        train_data[str(i)]['ori'] = raw_datasets['train'][i]['tokens']
        train_data[str(i)]['aug_0'] = raw_datasets['train'][i]['tokens'] # need to implement, e.g., mask words
        train_data[str(i)]['aug_1'] = raw_datasets['train'][i]['tokens'] # need to implement, e.g., synonyms
        train_data[str(i)]['label'] = raw_datasets['train'][i]['ner_tags']

    for i in train_data:
        print(train_data[i])
    with open(os.path.join(dst_path,'train.json'), 'w') as outfile:
        json.dump(train_data, outfile,indent=4)


    # test scripts
    with open(os.path.join(dst_path,'train.json'),'r') as json_data:
        check_data = json.load(json_data)
        print(check_data)
if os.path.exists('../data') == False:
    os.mkdir('../data')

create_semi_seq_data(dataset_name='conll2003',dataset_config_name=None,dst_root='../data/')
