import os
import shutil
import face_recognition
import numpy as np
from sklearn.cluster import DBSCAN

# Caminho da pasta com as imagens
input_folder = "fotos"
output_folder = "agrupadas_por_pessoa"

# Cria a pasta de saída se não existir
os.makedirs(output_folder, exist_ok=True)

# Lista de embeddings faciais e caminhos das imagens
face_encodings = []
image_paths = []

# Percorre todas as imagens da pasta
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)

        # Se houver rostos detectados, salva o primeiro encoding
        if encodings:
            face_encodings.append(encodings[0])
            image_paths.append(image_path)

# Converte para array numpy
encodings_array = np.array(face_encodings)

# Aplica DBSCAN para agrupar rostos semelhantes
clustering = DBSCAN(metric='euclidean', eps=0.6, min_samples=1)
labels = clustering.fit_predict(encodings_array)

# Agrupa imagens por pessoa
for label, image_path in zip(labels, image_paths):
    person_folder = os.path.join(output_folder, f"Pessoa_{label}")
    os.makedirs(person_folder, exist_ok=True)
    shutil.copy(image_path, person_folder)

print(f"Processo concluído! As imagens foram agrupadas em '{output_folder}' por pessoa.")
