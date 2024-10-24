#!/usr/bin/env python
# coding: utf-8

# Copyright 2021, IBM Corporation. 
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

"""
Python helper function to save HF model locally.
"""

__author__ = "Vagner Santana, Melina Alberio, Cassia Sanctos and Tiago Machado"
__copyright__ = "IBM Corporation 2024"
__credits__ = ["Vagner Santana, Melina Alberio, Cassia Sanctos, Tiago Machado"]
__license__ = "Apache 2.0"
__version__ = "0.0.1"

import os
from sentence_transformers import SentenceTransformer

def save_model():
    """
    Function that saves an HF model locally.

    Args:
        None.

    Returns:
        The model id and local path.

    Raises:
        Nothing.
    """
    # sentence transformer model
    model_id = "sentence-transformers/all-MiniLM-L6-v2"
    
    # download pretrained model
    model = SentenceTransformer(model_id)
    model_path = "./models/all-MiniLM-L6-v2/"

    # save to local directory
    model.save(model_path)
    saved_message = f"model {model_id} saved to {model_path}"
    print(saved_message)

    return model_id, model_path
  