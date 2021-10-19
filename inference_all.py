import numpy as np
import os
import tensorflow as tf
import pathlib
import argparse

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

class_names = ['audio', 'chat', 'email', 'files', 'video']
img_height = 32
img_width = 32
num_classes = 5

def load_model(checkpoint_filepath):
    
    model = Sequential([
        layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 1)),
    
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
    
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
    
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
    
        layers.Dropout(0.5),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)
    ])

    model.compile(optimizer='adam',loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy'])
    model.load_weights(checkpoint_filepath)

    return model

def inference(img_path, model):
    img = keras.preprocessing.image.load_img(img_path, target_size=(img_height, img_width), color_mode="grayscale")

    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    #print(
    #    "This packet most likely belongs to {} with a {:.2f} percent confidence."
    #    .format(class_names[np.argmax(score)], 100 * np.max(score))
    #)

    iden = class_names[np.argmax(score)]
    return iden

def inf_all(folder_path, img_num, model, img_label):
    correct = 0

    for i in range(img_num):
        img_path = folder_path+str(i)+'.png'
        
        iden = inference(img_path, model)

        if iden == img_label:
            correct = correct+1

    print(
        "Prediction is " + str((correct/img_num)*100) + " percent accurate."
        )

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--m', type=str, required=True)
    parser.add_argument('--n', type=int, required=True)
    parser.add_argument('--r', type=str, required=True)
    parser.add_argument('--l', type=str, required=True)
    args = parser.parse_args()

    checkpoint_filepath = args.m
    folder_path = args.r
    img_num = args.n
    img_label = args.l

    model = load_model(checkpoint_filepath)
    inf_all(folder_path, img_num, model, img_label)

if __name__ == '__main__':
    main()
