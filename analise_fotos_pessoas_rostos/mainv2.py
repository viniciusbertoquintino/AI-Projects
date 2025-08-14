import os
import shutil
import face_recognition
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Caminhos das pastas
input_folder = "fotos"  # Pasta com suas imagens
output_folder = "agrupadas_por_pessoa"
visualization_folder = "visualizacoes"

# Cria as pastas de saída se não existirem
os.makedirs(output_folder, exist_ok=True)
os.makedirs(visualization_folder, exist_ok=True)

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

# Dicionário para armazenar rostos por grupo
group_faces = {}

# Agrupa imagens por pessoa e extrai rostos para visualização
for label, image_path in zip(labels, image_paths):
    person_folder = os.path.join(output_folder, f"Pessoa_{label}")
    os.makedirs(person_folder, exist_ok=True)
    shutil.copy(image_path, person_folder)

    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    for top, right, bottom, left in face_locations:
        face_image = image[top:bottom, left:right]
        if label not in group_faces:
            group_faces[label] = []
        group_faces[label].append(face_image)

# Gera visualizações em grade para cada grupo
for label, faces in group_faces.items():
    fig, axes = plt.subplots(1, len(faces), figsize=(3 * len(faces), 3))
    if len(faces) == 1:
        axes = [axes]
    for ax, face in zip(axes, faces):
        ax.imshow(face)
        ax.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(visualization_folder, f"Pessoa_{label}.png"))
    plt.close()

print(f"✅ Imagens agrupadas em '{output_folder}' por pessoa.")
print(f"🖼️ Visualizações salvas em '{visualization_folder}'.")
