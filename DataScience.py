import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic
import os

sns.set(style="whitegrid")

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Datos cargados correctamente.")
        return data
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encontró.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: El archivo está vacío.")
        return None
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def create_plots(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='tipo_incidente') 
    plt.title('Número de Incidentes por Tipo')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grafico_barras_tipo_incidente.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, y='tipo_incidente')  
    plt.title('Número de Incidentes por Tipo (Horizontal)')
    plt.tight_layout()
    plt.savefig('grafico_barras_horizontal_tipo_incidente.png')
    plt.show()

    incident_counts = data.groupby(['tipo_incidente', 'sexo']).size().unstack()
    incident_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Incidentes por Tipo y Sexo')
    plt.xlabel('Tipo de Incidente')
    plt.ylabel('Número de Incidentes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grafico_barras_apiladas.png')
    plt.show()

    heatmap_data = data.pivot_table(index='tipo_incidente', columns='sexo', values='id', aggfunc='count') 
    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Mapa de Calor de Incidentes por Tipo y Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Tipo de Incidente')
    plt.tight_layout()
    plt.savefig('mapa_calor_incidentes.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    mosaic(data, ['tipo_incidente', 'sexo']) 
    plt.title('Diagrama de Mosaico de Incidentes por Tipo y Sexo')
    plt.show()

def main():
    file_path = 'cibercriminalidad_2015.csv'  
    data = load_data(file_path)
    
    if data is not None:
        print("Primeras filas de los datos:")
        print(data.head()) 
        create_plots(data)

if __name__ == "__main__":
    main()
