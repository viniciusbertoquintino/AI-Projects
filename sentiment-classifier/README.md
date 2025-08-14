# Sentiment Classifier with Hugging Face 🤖

Este projeto utiliza modelos pré-treinados da Hugging Face para classificar sentimentos em textos (positivo, negativo ou neutro).

## 📦 Tecnologias
- Python
- Hugging Face Transformers
- Dataset IMDb (via Hugging Face Datasets)
- Scikit-learn
- Streamlit

## 🚀 Como rodar o projeto

    1. Clone o repositório:

        git clone https://github.com/viniciusbertoquintino/AI-Projects.git
        
        cd AI-Projects/sentiment-classifier


    2. Instale as dependências:

        pip install -r requirements.txt

    3. Execute o script de treinamento:

        python src/train_model.py

    4. Faça previsões com:

        python src/predict.py "Esse filme foi incrível!"

## 📊 Demo interativa (opcional)
 
 streamlit run app/app.py