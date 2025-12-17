import tensorflow as tf
import os

IMAGE_SIZE = (224, 224) 
BATCH_SIZE = 32
DATA_DIR = 'Dataset' 

def load_and_prepare_data(data_dir=DATA_DIR):
    print("Veri Kümeleri Yükleniyor...")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        os.path.join(data_dir, 'train'),
        labels='inferred',
        label_mode='binary', 
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=True
    )
    
    val_ds = tf.keras.utils.image_dataset_from_directory(
        os.path.join(data_dir, 'validation'),
        labels='inferred',
        label_mode='binary',
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=False
    )
    
    test_ds = tf.keras.utils.image_dataset_from_directory(
        os.path.join(data_dir, 'test'),
        labels='inferred',
        label_mode='binary',
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=False
    )
    
    class_names = train_ds.class_names 
    num_classes = len(class_names) 

    print(f"\nToplam {num_classes} Sınıf Bulundu: {class_names}")

    normalization_layer = tf.keras.layers.Rescaling(1./255)

    def prepare(ds):
        ds = ds.map(lambda x, y: (normalization_layer(x), y))
        return ds.cache().prefetch(buffer_size=tf.data.AUTOTUNE)

    train_ds = prepare(train_ds)
    val_ds = prepare(val_ds)
    test_ds = prepare(test_ds)

    print("Veri Kümesi Hazırlığı Tamamlandı.")

    return train_ds, val_ds, test_ds, class_names, num_classes

if __name__ == '__main__':
    try:
        train_ds, val_ds, test_ds, class_names, num_classes = load_and_prepare_data()
        print(f"\nBeklenen Sınıf Adları (Alfabetik Sıra): {class_names}")
    except Exception as e:
        print(f"\n HATA: Veri kümesi yüklenemedi. Detay: {e}")