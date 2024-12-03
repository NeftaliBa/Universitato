# 1. Importaciones necesarias
import os
import pandas as pd
import re
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import HashingVectorizer, CountVectorizer, TfidfVectorizer
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.decomposition import LatentDirichletAllocation, PCA
from sklearn.metrics import accuracy_score, classification_report
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import joblib
import numpy as np

# 1.1 Generar el archivo CSV desde las carpetas de datos (si no existe)
def cargar_datos(basepath):
    data = []
    etiquetas = {'pos': 1, 'neg': 0}

    for conjunto in ['train', 'test']:
        for etiqueta, valor in etiquetas.items():
            path = os.path.join(basepath, conjunto, etiqueta)
            for archivo in os.listdir(path):
                if archivo.endswith('.txt'):
                    with open(os.path.join(path, archivo), 'r', encoding='utf-8') as f:
                        data.append((f.read(), valor))

    df = pd.DataFrame(data, columns=['review', 'sentiment'])
    return df

# Verifica si el archivo CSV ya existe
csv_path = 'movie_data.csv'
basepath = r'C:\Users\nefta\Desktop\Universitato\7D\Codigo\introduccion a data science\movies\aclImdb'

if not os.path.exists(csv_path):
    print("Generando el archivo CSV...")
    df = cargar_datos(basepath)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df.to_csv(csv_path, index=False, encoding='utf-8')
    print("Archivo CSV generado con éxito: movie_data.csv")
else:
    print("El archivo CSV ya existe.")

# 2. Cargar el archivo CSV
data = pd.read_csv(csv_path)
print(data.head())

# 3. Preprocesamiento de texto
stop_words = set(stopwords.words('english'))
# Ya estoy harto de que me salgan las muy desgraciadas
irrelevantes = {'movie', 'film', 'br', 'one', 'see', 'story', 'films', 'movies', 'make', 'plot', 'think', 'life'}

def limpiar_texto(texto):
    texto = re.sub(r'<br\s*/?>', ' ', texto)  # Eliminar etiquetas <br />
    texto = re.sub(r'[^\w\s]', '', texto)  # Quitar puntuación
    texto = re.sub(r'\d+', '', texto)  # Quitar números
    texto = texto.lower()  # Convertir a minúsculas
    texto = ' '.join([palabra for palabra in texto.split() if palabra not in stop_words and palabra not in irrelevantes])
    return texto

data['clean_text'] = data['review'].apply(limpiar_texto)
print(data.head())


# 4. División en conjunto de entrenamiento y prueba
X = data['clean_text']
y = data['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Configurar y transformar con TfidfVectorizer
tfidf = TfidfVectorizer(max_features=5000, min_df=5, stop_words='english')  # Limita a palabras comunes
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# 5. Clasificación usando SGDClassifier
clf = SGDClassifier(loss='log_loss', random_state=42)
clf.fit(X_train_tfidf, y_train)

y_pred = clf.predict(X_test_tfidf)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Palabras clave para cada clase
feature_names = tfidf.get_feature_names_out()  # Obtener los nombres de las características
weights = clf.coef_

# Palabras asociadas a sentimientos positivos
positive_words = {feature_names[i]: weights[0, i] for i in weights[0].argsort()[-10:]}

# Palabras asociadas a sentimientos negativos
negative_words = {feature_names[i]: weights[0, i] for i in weights[0].argsort()[:10]}

print("Positive words:", positive_words)
print("Negative words:", negative_words)

# Guardar modelo y vectorizador
joblib.dump(clf, 'sentiment_model.pkl')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')

# 6. Inferencia de temas con LDA
count_vectorizer = CountVectorizer(max_df=0.9, min_df=5, stop_words='english')  # Filtra palabras raras
X_train_counts = count_vectorizer.fit_transform(X_train)

lda = LatentDirichletAllocation(n_components=10, random_state=42)
lda.fit(X_train_counts)

for idx, topic in enumerate(lda.components_):
    print(f"Tema {idx}:")
    print([count_vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])

# Visualización de temas con WordCloud
for idx, topic in enumerate(lda.components_):
    words = {count_vectorizer.get_feature_names_out()[i]: topic[i] for i in topic.argsort()[-10:]}
    wordcloud = WordCloud(background_color="white").generate_from_frequencies(words)
    
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(f"Tema {idx}")
    plt.show()

# 7. PCA y gráficos de dispersión
tfidf = TfidfVectorizer(max_features=5000, min_df=5, stop_words='english')  # Limita a palabras comunes
X_train_tfidf = tfidf.fit_transform(X_train)

pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_tfidf.toarray())

plt.figure(figsize=(10, 6))
plt.scatter(X_train_pca[y_train.values == 1, 0], X_train_pca[y_train.values == 1, 1], color='blue', alpha=0.5, label='Positive')
plt.scatter(X_train_pca[y_train.values == 0, 0], X_train_pca[y_train.values == 0, 1], color='red', alpha=0.5, label='Negative')
plt.title('Sentiment Analysis PCA Visualization')
plt.legend()
plt.show()

# 8. Histogramas de frecuencia
positive_weights = X_train_tfidf[y_train.values == 1].sum(axis=0).A1
negative_weights = X_train_tfidf[y_train.values == 0].sum(axis=0).A1

positive_counter = Counter(dict(zip(tfidf.get_feature_names_out(), positive_weights))).most_common(10)
negative_counter = Counter(dict(zip(tfidf.get_feature_names_out(), negative_weights))).most_common(10)

pos_words, pos_counts = zip(*positive_counter)
neg_words, neg_counts = zip(*negative_counter)

plt.barh(pos_words, pos_counts, color='blue', label='Positive', alpha=0.7)
plt.barh(neg_words, neg_counts, color='red', label='Negative', alpha=0.7)
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.title('Top Words by Sentiment')
plt.legend()
plt.show()
