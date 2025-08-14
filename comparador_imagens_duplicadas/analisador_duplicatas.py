import os
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Diretório contendo as imagens
image_dir = "imagens"

# Carregar o modelo ResNet50 pré-treinado
weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval()

# Remover a última camada para obter embeddings
feature_extractor = torch.nn.Sequential(*list(model.children())[:-1])

# Transformações para pré-processar as imagens
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    weights.transforms()
])

# Função para extrair embeddings de uma imagem
def get_embedding(image_path):
    image = Image.open(image_path).convert("RGB")
    img_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        embedding = feature_extractor(img_tensor).squeeze().numpy()
    return embedding.flatten()

# Carregar todas as imagens e calcular seus embeddings
embeddings = {}
for filename in os.listdir(image_dir):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
        path = os.path.join(image_dir, filename)
        embeddings[filename] = get_embedding(path)

# Comparar embeddings para encontrar duplicatas
threshold = 0.95  # Similaridade mínima para considerar duplicata
checked = set()
duplicates = []

for img1 in embeddings:
    for img2 in embeddings:
        if img1 != img2 and (img2, img1) not in checked:
            sim = cosine_similarity([embeddings[img1]], [embeddings[img2]])[0][0]
            if sim >= threshold:
                duplicates.append((img1, img2, sim))
            checked.add((img1, img2))

# Exibir resultados
if duplicates:
    print("Imagens duplicadas encontradas:")
    for dup in duplicates:
        print(f"{dup[0]} e {dup[1]} - Similaridade: {dup[2]:.2f}")
else:
    print("Nenhuma duplicata encontrada.")
