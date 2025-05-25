# netflix-recommender
🎬 Netflix Film ve Dizi Öneri Sistemi
Bu proje, Netflix Movies and TV Shows Dataset kullanılarak film ve dizi önerileri sunan bir içerik tabanlı öneri sistemidir. Streamlit arayüzü ile etkileşimli bir şekilde öneriler sunulur. Proje, Docker ile container haline getirilmiş olup, istenirse Kubernetes ile ölçeklendirilebilir.

📌 Amaç
Netflix içerikleri arasında benzer tür, yönetmen, oyuncu ve açıklamalara göre önerilerde bulunan kullanıcı dostu bir öneri sistemi geliştirmek.

🔧 Kullanılan Teknolojiler
Python 🐍

Pandas, NumPy, Scikit-learn

Streamlit (Web arayüzü için)

Docker (Containerizasyon)

Kubernetes (Opsiyonel - Dağıtım/Orkestrasyon)

Git/GitHub (Versiyon kontrol)

📁 Proje Yapısı
bash
Kopyala
Düzenle
netflix-recommender/
├── data/                    # Veri seti (netflix_titles.csv)
├── notebooks/               # EDA ve analiz notebookları
├── app/                     # Streamlit uygulaması
├── models/                  # Eğitilmiş modeller
├── Dockerfile               # Docker yapılandırması
├── requirements.txt         # Gerekli Python kütüphaneleri
├── README.md                # Proje tanımı
└── .gitignore
⚙️ Kurulum
bash
Kopyala
Düzenle
git clone https://github.com/kullanici-adin/netflix-recommender.git
cd netflix-recommender
pip install -r requirements.txt
streamlit run app/streamlit_app.py
Docker ile çalıştırmak için:

bash
Kopyala
Düzenle
docker build -t netflix-recommender .
docker run -p 8501:8501 netflix-recommender
📊 Proje Özellikleri
İçerik tabanlı filtreleme (Content-Based Filtering)

Tür, yönetmen, oyuncu ve açıklamalara göre benzer içerik önerisi

Kullanıcı girişiyle öneri oluşturma

Temiz ve kullanıcı dostu Streamlit arayüzü

📌 Hedefler
EDA (veri keşfi)

Benzerlik metrikleri (TF-IDF, cosine similarity) ile öneri sistemi

Model optimizasyonu

Kullanıcı arayüzü geliştirme (Streamlit)

Dağıtım ve ölçeklenebilirlik (Docker, Kubernetes)

🧠 Katkı ve Geliştirme
Geliştirmeye açıksın! Fork'la, pull request gönder veya issue açabilirsin ✨
