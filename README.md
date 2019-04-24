# late-night-cafe

## Dataset
Preprocessed Poe's texts, Witkin Kmeans results and crawled Pinterest eye pictures downloadable [here](https://drive.google.com/drive/folders/1pqzuOnkmRIbD-v8B59v2DMCAcs1vajty?usp=sharing).

## Usage
### Poe's Text Generator
```bash
source activate tensorflow_p36
pip3 install --user --upgrade tensorflow-probability
git clone https://github.com/asyml/texar.git
cd texar
pip install -e .
```

#### Train
```bash
python prepare_data.py --data [data_name]
python vae_train.py --config [config_file]
```
``data_name`` can be ``poe-v15000-l-1``, ``poe-v15000-l100``, ``poe-v15000-l140``, ``poe-v18000-l-1``, ``poe-v18000-l100``, ``poe-v18000-l140``.
``config_file`` can be ``config_trans_poem`` or ``config_lstm_poem``.

You need to change one line in config.py every time you change the data set!

#### Generate
```bash
python vae_train.py --config [config_file] --mode predict --model [model/path/to/model.ckpt]
```
``[model/path/to/model.ckpt`` Check the ``models/`` folder. An example is ``poe-v15000-l-1_transformerDecoder.ckpt``.

### Pinterest Scrapper
Please refer to README inside the folder.

### Kmeans
Provide the image folder path in ``IMAGE_PATH`` and the code will try to create folders for each cluster and copy images there.

### KNN 
All dependencies and steps described in detail in the notebook.
