# Copyright 2018 The Texar Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""VAE config.
"""

# pylint: disable=invalid-name, too-few-public-methods, missing-docstring

# MUST edit the line below!!!
dataset = "poem-v18000-n1"
num_epochs = 5
hidden_size = 550
dec_dropout_in = 0.5
dec_dropout_out = 0.5
enc_dropout_in = 0.
enc_dropout_out = 0.
batch_size = 32
embed_dim = 512

latent_dims = 32

lr_decay_hparams = {
    "init_lr": 0.001,
    "threshold": 2,
    "decay_factor": 0.5,
    "max_decay": 5
}


relu_dropout = 0.2
embedding_dropout = 0.2
attention_dropout = 0.2
residual_dropout = 0.2
num_blocks = 3

decoder_hparams = {
    "type": "lstm"
}

enc_cell_hparams = {
    "type": "LSTMBlockCell",
    "kwargs": {
        "num_units": hidden_size,
        "forget_bias": 0.
    },
    "dropout": {"output_keep_prob": 1. - enc_dropout_out},
    "num_layers": 1
}

dec_cell_hparams = {
    "type": "LSTMBlockCell",
    "kwargs": {
        "num_units": hidden_size,
        "forget_bias": 0.
    },
    "dropout": {"output_keep_prob": 1. - dec_dropout_out},
    "num_layers": 1
}

enc_emb_hparams = {
    'name': 'lookup_table',
    "dim": embed_dim,
    "dropout_rate": enc_dropout_in,
    'initializer' : {
        'type': 'random_normal_initializer',
        'kwargs': {
            'mean': 0.0,
            'stddev': embed_dim**-0.5,
        },
    }
}

dec_emb_hparams = {
    'name': 'lookup_table',
    "dim": embed_dim,
    "dropout_rate": dec_dropout_in,
    'initializer' : {
        'type': 'random_normal_initializer',
        'kwargs': {
            'mean': 0.0,
            'stddev': embed_dim**-0.5,
        },
    }
}


# KL annealing
# kl_weight = 1.0 / (1 + np.exp(-k*(step-x0)))
kl_anneal_hparams={
    "warm_up": 10,
    "start": 0.1
}

train_data_hparams = {
    "num_epochs": 1,
    "batch_size": batch_size,
    "seed": 123,
    "dataset": {
        "files": './data/{}/{}.train.txt'.format(dataset, dataset),
        "vocab_file": './data/{}/vocab.txt'.format(dataset)
    }
}

val_data_hparams = {
    "num_epochs": 1,
    "batch_size": batch_size,
    "seed": 123,
    "dataset": {
        "files": './data/{}/{}.val.txt'.format(dataset, dataset),
        "vocab_file": './data/{}/vocab.txt'.format(dataset)
    }
}

test_data_hparams = {
    "num_epochs": 1,
    "batch_size": batch_size,
    "dataset": {
        "files": './data/{}/{}.test.txt'.format(dataset, dataset),
        "vocab_file": './data/{}/vocab.txt'.format(dataset)
    }
}

opt_hparams = {
    "optimizer": {
        "type": "AdamOptimizer",
        "kwargs": {
            "learning_rate": 0.001
        }
    },
    "gradient_clip": {
        "type": "clip_by_global_norm",
        "kwargs": {"clip_norm": 5.}
    }
}
