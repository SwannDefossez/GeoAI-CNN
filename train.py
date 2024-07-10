import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, Callback
import os
import time

tf.config.list_physical_devices('GPU')


classes = ['AE', 'AL', 'AR', 'AT', 'AU', 'BD', 'BE', 'BG', 'BO', 'BR', 'BW', 'CA', 'CH', 'CL', 'CO', 'CR', 'CZ', 'DE', 'DK', 'DO', 'EC', 'EE', 'ES', 'FI', 'FR', 'GB', 'GH', 'GR', 'GT', 'HR', 'HU', 'ID', 'IE', 'IL', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KR', 'LK', 'LS', 'LT', 'LU', 'LV', 'MA', 'MD', 'ME', 'MK', 'MN', 'MT', 'MX', 'MY', 'NG', 'NL', 'NO', 'NZ', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'RO', 'RS', 'RU', 'SA', 'SE', 'SG', 'SI', 'SK', 'SN', 'TH', 'TR', 'TW', 'TZ', 'UG', 'US', 'UY', 'ZA']

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('trainset',
                                                 target_size=(224, 224),
                                                 batch_size=32,
                                                 class_mode='categorical')

test_set = test_datagen.flow_from_directory('testset',
                                            target_size=(224, 224),
                                            batch_size=32,
                                            class_mode='categorical')


model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    BatchNormalization(),
    MaxPool2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    BatchNormalization(),
    MaxPool2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(82, activation='softmax')
])


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

filepath = 'checkpoint.keras'

model_checkpoint = ModelCheckpoint(
    filepath=filepath,
    save_best_only=True,
    monitor='val_loss',
    mode='min',
    verbose=1
)

early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=10,
    verbose=1,
    mode='min',
    restore_best_weights=True
)


model.fit(
    training_set,
    epochs=50,
    validation_data=test_set,
    callbacks=[model_checkpoint, early_stopping, time_limit_callback]
)


model.save('model.keras')
