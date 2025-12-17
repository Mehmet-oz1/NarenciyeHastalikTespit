import numpy as np
import json
import tensorflow as tf
from PIL import Image
import os
import io

IMAGE_SIZE = (224, 224) 
MODEL_PATH = 'narenciye_hastalik_model.h5'

try:
    with open('solutions.json', 'r', encoding='utf-8') as f:
        SOLUTIONS_DB = json.load(f)
    
    CLASS_NAMES = ['Hastalik', 'Saglikli'] 

except FileNotFoundError:
    print("HATA: solutions.json dosyası bulunamadı! Varsayılan sınıflar kullanılıyor.")
    SOLUTIONS_DB = {}
    CLASS_NAMES = ['Hastalik', 'Saglikli'] 

MODEL = None 
try:
    MODEL = tf.keras.models.load_model(MODEL_PATH)
    print(f"Model başarıyla yüklendi: {MODEL_PATH}")
except Exception as e:
    print(f"HATA: Model yüklenemedi. Eğitim yapılmadı mı? ({MODEL_PATH})")
    print(f"Hata Detayı: {e}")

def predict_disease(uploaded_file):
    """
    Görüntüyü alır, işler ve eğitilmiş TensorFlow modeli ile tahmin yapar.
    """
    if MODEL is None:
        import random
        predicted_class = random.choice(CLASS_NAMES)
        confidence = random.uniform(50.00, 70.00)
        
        result = {
            'disease': predicted_class + " (MOCK)",
            'confidence': confidence,
            'solution': SOLUTIONS_DB.get(predicted_class, {'aciklama': 'Hata: Mock çözüm bulunamadı.'})
        }
        return result
        
    try:
        image = Image.open(uploaded_file).convert('RGB')
        
        image = image.resize(IMAGE_SIZE) 
        
        img_array = np.array(image) / 255.0 
        
        img_array = np.expand_dims(img_array, axis=0) 

        predictions = MODEL.predict(img_array)[0] 
        threshold = 0.5 
        
        
        if predictions[0] > threshold:
            predicted_class = CLASS_NAMES[1]
            confidence = predictions[0] * 100 
        else:
            predicted_class = CLASS_NAMES[0]
            confidence = (1 - predictions[0]) * 100 

        solution_data = SOLUTIONS_DB.get(predicted_class, {'aciklama': 'Bilinmeyen durum için çözüm bulunamadı.'})
        
        result = {
            'disease': predicted_class,
            'confidence': confidence,
            'solution': solution_data
        }
        
        return result
        
    except Exception as e:
        print(f"Tahmin sırasında kritik bir hata oluştu: {e}")
        return {
            'disease': "HATA",
            'confidence': 0.0,
            'solution': {'aciklama': f'Görüntü işlenirken kritik bir hata oluştu. Detay: {e}'}
        }

if __name__ == '__main__':
    print("Tahminci modülü yüklendi.")