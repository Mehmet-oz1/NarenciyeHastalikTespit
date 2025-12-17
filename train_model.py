import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.applications import MobileNetV2
from prepare_data import load_and_prepare_data 

EPOCHS = 10 
IMAGE_SIZE = (224, 224) 
MODEL_SAVE_PATH = 'narenciye_hastalik_model.h5'

def build_model(num_classes):
    """
    MobileNetV2 temel alınarak ikili sınıflandırma modelini oluşturur.
    """
    base_model = MobileNetV2(
        input_shape=IMAGE_SIZE + (3,), 
        include_top=False, 
        weights='imagenet'
    )
    base_model.trainable = False 

    model = Sequential([
        base_model,
        GlobalAveragePooling2D(), 
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid') 
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy', 
        metrics=['accuracy']
    )
    
    model.summary()
    return model

def train_and_save_model():
    try:
        train_ds, val_ds, test_ds, class_names, num_classes = load_and_prepare_data()
    except Exception as e:
        print("Veri kümesi yüklenemedi. Eğitim atlanıyor.")
        print(f"Hata detayı: {e}")
        num_classes = 2 
        train_ds, val_ds = None, None 
        
    model = build_model(num_classes)
    
    if train_ds is not None and val_ds is not None:
        print("\nModel Eğitimi Başlatılıyor...")
        model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=EPOCHS
        )
        
        model.save(MODEL_SAVE_PATH)
        print(f"\nModel başarıyla kaydedildi: {MODEL_SAVE_PATH}")
    else:
        print("\nModel Eğitimi ATLANDI. Lütfen görselleri ekledikten sonra tekrar çalıştırın.")

if __name__ == '__main__':
    train_and_save_model()