# late-night-cafe

Install libraries
```bash
source activate tensorflow_p36

pip3 install --user --upgrade tensorflow-probability

git clone https://github.com/asyml/texar.git
cd texar
pip install -e .
```

Get this repo
```bash
cd ~
git clone https://github.com/zxyao/late-night-cafe.git
```

## Train

Make sure you are in ``late-night-cafe/vae_text/`` which can be done by
```bash
cd ~/late-night-cafe/vae_text/
```

Then download data sets and start training!
```bash
python prepare_data.py --data [data_name]
python vae_train.py --config [config_file]
```
``data_name`` can be ``poem-v18000-n1`` and more...

``config_file`` can be ``config_trans_poem`` or ``config_lstm_poem``.

An example runnable command is 
```bash
python prepare_data.py --data poem-v18000-n1
python vae_train.py --config config_trans_poem
```

**You need to change one line in config.py every time you change the data set!!!!**

## Generate
```bash
python vae_train.py --config [config_file] --mode predict --model [model/path/to/model.ckpt]
```

``[model/path/to/model.ckpt`` Check the ``models/`` folder. An example is ``poem-v18000-n1_transformerDecoder.ckpt``.

An example runnable command is
```bash
python vae_train.py --config config_trans_poem --mode predict --model models/poem-v18000-n1/poem-v18000-n1_transformerDecoder.ckpt
```
