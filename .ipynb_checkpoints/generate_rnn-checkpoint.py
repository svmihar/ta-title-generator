from textgenrnn import textgenrnn
from keras import backend as K
import tensorflow as tf
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
K.tensorflow_backend._get_available_gpus()

model_cfg = {
    'rnn_size':128, 
    'rnn_layers':4, 
    'rnn_bidirectional':True, 
    'max_length':40,
    'dim_embeddings':30,
    'word_level':False
}

train_cfg = {
    'line_delimited':True, 
    'num_epochs':10,
    'gen_epochs':2, 
    'batch_size':512, 
    'train_size':.8,
    'dropout':0.0,
    'max_gen_length':300,
    'validation':False, 
    'is_csv':False
}

tg = textgenrnn(name='judul_TA')
tg.train_from_file('titles.txt',new_model=False,
rnn_bidirectional=True,
rnn_layers=4,
rnn_size=128,
dim_embeddings=300,
num_epochs=100, gen_epochs=2, batch_size=1024)
print(tg.model.summary())
print('\n\n\n',tg.generate_samples())
tg.generate_to_file('judul_ta_generator_texts.txt', n=5)