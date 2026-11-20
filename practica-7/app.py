import gradio as gr
import torch
from transformers import pipeline

# Cargar el pipeline de clasificación de imágenes con el modelo especificado
clasificador = pipeline(
    task="image-classification",
    model="google/mobilenet_v2_1.0_224",
    device=0 if torch.cuda.is_available() else -1,
)


def clasificar(imagen):
  if imagen is None:
    return "Por favor, sube o selecciona una imagen."

  # Obtener las 3 predicciones más probables
  resultados = clasificador(imagen, top_k=3)

  # Formatear la salida con etiqueta y porcentaje
  salida = []
  for res in resultados:
    etiqueta = res["label"]
    porcentaje = res["score"] * 100
    salida.append(f"{etiqueta}: {porcentaje:.2f}%")

  return "\n".join(salida)


# Crear la interfaz de Gradio
interfaz = gr.Interface(
    fn=clasificar,
    inputs=gr.Image(type="pil", label="Sube una imagen"),
    outputs=gr.Textbox(label="Top 3 Predicciones"),
    title="Clasificador de Imágenes (MobileNetV2)",
    description=(
        "Sube una imagen para obtener las 3 etiquetas más probables usando"
        " google/mobilenet_v2_1.0_224."
    ),
)

if __name__ == "__main__":
  interfaz.launch()