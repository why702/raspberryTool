# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""API for Face Detection."""

from collections import namedtuple

from aiy.vision.inference import ModelDescriptor
from aiy.vision.models import utils


_COMPUTE_GRAPH_NAME = 'facenet.binaryproto'

Facenet = namedtuple('Face', ('embeddings'))

def model():
    return ModelDescriptor(
        name='FaceRecognition',
        input_shape=(1, 160, 160, 3),
        input_normalizer=(127.5, 128),
        compute_graph=utils.load_compute_graph(_COMPUTE_GRAPH_NAME))


def get_faces(result):
    assert len(result.tensors) == 1
    tensor = result.tensors['embeddings']
    print(utils.shape_tuple(tensor.shape))
    # assert utils.shape_tuple(tensor.shape) == (1, 1, 1, 2024)
    return tuple(tensor.data)