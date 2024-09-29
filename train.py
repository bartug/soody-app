import os
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from keras.applications import MobileNet
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.utils import plot_model
import pandas as pd

# Eğitim ve Test Veri Seti Boyutları:
nb_train_samples = 28709
nb_validation_samples = 7178

# Yüz ifadesi örnekleri:
expressions_list = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Modeli oluşturma
img_rows, img_cols = 224, 224
num_labels = len(expressions_list)

base_model = MobileNet(weights='imagenet', include_top=False, input_shape=(img_rows, img_cols, 3))
for layer in base_model.layers:
    layer.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
x = Dense(1024, activation='relu')(x)
x = Dense(512, activation='relu')(x)
predictions = Dense(num_labels, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

train_data_dir = './train'
validation_data_dir = './test'
# Eğitim ve Test Veri Seti Boyutları:
print("Eğitim veri seti boyutu:", nb_train_samples)
print("Test veri seti boyutu:", nb_validation_samples)

# Yüz ifadesi örnekleri:
expressions_list = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Yüz ifadelerinin gösterilmesi
print("Yüz ifadesi örnekleri:")
for i, expression in enumerate(expressions_list):
    print(f"{i}. {expression}")

# Veri artırma
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    width_shift_range=0.3,
    height_shift_range=0.3,
    horizontal_flip=True,
    fill_mode='nearest')

validation_datagen = ImageDataGenerator(rescale=1./255)

# Batch boyutu
batch_size = 32

# Eğitim verilerini oluşturma
train_generator = train_datagen.flow_from_directory(
    directory=train_data_dir,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode="categorical")

# Doğrulama verilerini oluşturma
validation_generator = validation_datagen.flow_from_directory(
    directory=validation_data_dir,
    target_size=(img_rows, img_cols),
    batch_size=batch_size,
    class_mode="categorical")

# Modeli kaydetme
checkpoint = ModelCheckpoint('model.h5',
                             monitor='val_loss',
                             mode='min',
                             save_best_only=True,
                             verbose=1)

# Eğitimi durdurma
earlystop = EarlyStopping(
                          monitor='val_loss',
                          min_delta=0.001,
                          patience=10,
                          verbose=1,
                          restore_best_weights=True)

# Öğrenme hızını azaltma
learning_rate_reduction = ReduceLROnPlateau(monitor='val_accuracy',
                                            patience=5,
                                            verbose=1,
                                            factor=0.2,
                                            min_lr=0.0001)

# Callback fonksiyonları listesi
callbacks = [earlystop, checkpoint, learning_rate_reduction]


# Modeli derleme
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr=0.001),
              metrics=['accuracy'])

# Eğitim sürecinin gerçekleştirilmesi
epochs = 30
history = model.fit(
    train_generator,
    steps_per_epoch=nb_train_samples//batch_size,
    epochs=epochs,
    callbacks=callbacks,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples//batch_size)

# Eğitim sürecinin görselleştirilmesi
title_font = {"family": "arial", "color": "k", "weight": "bold", "size": 14}
axes_font = {"family": "arial", "color": "#023553", "weight": "bold", "size": 12}

fig = plt.figure(figsize=(25, 8))

plt.plot(history.history["accuracy"], color="#3BB47E", label="Eğitim başarısı")
plt.plot(history.history["val_accuracy"], color="#FF605C", label="Doğrulama başarısı")

plt.xticks(range(len(history.history["accuracy"])))

plt.legend(loc="upper left")

plt.title("Doğruluk (Accuracy) - Epok (Epochs)", fontdict=title_font)
plt.xlabel("Epok Numarası (Epoch Number)", fontdict=axes_font)
plt.ylabel("Doğruluk (Accuracy)", fontdict=axes_font)

plt.grid(True, axis="x", alpha=0.5, linestyle="--")

max_val_acc_row_index = history.history['val_accuracy'].index(max(history.history['val_accuracy']))
plt.scatter(max_val_acc_row_index, history.history['val_accuracy'][max_val_acc_row_index])

plt.show()

# Modeli kaydetme
model.save("new_model.h5")

# Test verilerini tahmin etme
Y_pred = model.predict(validation_generator)
y_pred = np.argmax(Y_pred, axis=1)
y_true = validation_generator.classes

# Confusion Matrix oluşturma
cm = confusion_matrix(y_true, y_pred)

# Confusion Matrix'i görselleştirme
plt.figure(figsize=(8, 8))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(num_labels)
plt.xticks(tick_marks, range(num_labels))
plt.yticks(tick_marks, range(num_labels))
plt.xlabel('Tahmin Edilen Etiketler')
plt.ylabel('Gerçek Etiketler')
plt.show()


# Eğitim geçmişini DataFrame olarak gösterme
history_df = pd.DataFrame(history.history)
print(history_df)
2