import streamlit as st
from PIL import Image
from predictor import predict_disease 

st.set_page_config(
    page_title="Narenciye Sağlık Tespit Sistemi (Hasta mı? Sağlıklı mı?)",
    layout="wide",
    initial_sidebar_state="auto"
)

def main():
    """Ana Streamlit Uygulama Fonksiyonu"""
    
    st.title("Narenciye Sağlık Tespit Sistemi (Hastalık/Sağlıklı)")
    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Lütfen bir narenciye (meyve veya yaprak) görseli yükleyin:", 
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        
        image = Image.open(uploaded_file)
        st.image(image, caption='Yüklenen Görsel', use_container_width=True)
        st.markdown("---")
        
        if st.button('Durumu Tespit Et'):
            
            with st.spinner('Analiz yapılıyor...'):
                result = predict_disease(uploaded_file) 
            
            st.success("Analiz Tamamlandı!")
            
            disease_name = result['disease']
            confidence_level = result['confidence']
            solution_data = result['solution']
            
            st.subheader(f"Tespit Edilen Durum: {disease_name}")
            st.metric(
                label="Güven Seviyesi (Model Tahmini)", 
                value=f"%{confidence_level:.2f}"
            )

            st.markdown("### Detaylı Bilgi ve Öneriler")
            
            st.markdown(f"**Açıklama:** {solution_data['aciklama']}")
            
            st.markdown("#### Önleyici Tedbirler")
            for item in solution_data['onlemler']:
                st.markdown(f"- {item}")
                
            st.markdown("#### Tedavi Yöntemleri")
            st.markdown(solution_data['tedavi'])
            
            st.markdown("---")


if __name__ == '__main__':
    main()