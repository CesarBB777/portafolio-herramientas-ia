\# \[ClipQuest]



&#x20;



> \\\[Buscador de escenas en grabaciones de videojuegos]



&#x20;



\*\*Proyecto integrador · Herramientas de IA\*\*



&#x20;



\*\*Grupo:\*\* \[1B ] · \*\*Equipo:\*\* \[ 1 ]



&#x20;



\## 👥 Integrantes



&#x20;



| Integrantes                | Matricula |

| -------------------------- | --------- |

| Diego Isaac Rico Hernández | 198492-8  |

| César Iván Macías Anguiano | 198553-7  |

| Ernesto Tehuintle Ramírez  | 198626-6  |

| Sebastián Guerrero Ambriz  | 197113-2  |



&#x20;



\## 1. Caso de uso



&#x20;



\[Localizar escenas de videos o partidas sin tener que revisar todo el video, muy útil para creadores de contenido o gamers.]



&#x20;



\- \*\*Entrada:\*\* \[Videos y fotos]



\- \*\*Salida:\*\* \[Clip especifico en relación a lo que buscaron]



&#x20;



\## 2. Modelo abierto elegido



&#x20;



| Dato                         | Respuesta                                                                           |

| ---------------------------- | ----------------------------------------------------------------------------------- |

| Identificador                | \[openai/clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32) |

| Tarea (pipeline tag)         | `\\\[zero-shot-image-classification]`                                                  |

| Número de parámetros         | Aproximadamente 151.28 millones                                                     |

| Licencia                     | MIT, según el repositorio oficial                                                   |

| Limitación o sesgo declarado | Dificultades para distinguir categorías muy específicas y contar<br>objetos         |





\## 3. Viabilidad de hardware



&#x20;



$$



\\text{Memoria mínima} = 151,280,000 \\times 2\\ \\text{bytes} \\approx \\ 0.303\\ \\text{GB}



$$



&#x20;



\- \*\*VRAM disponible en Colab:\*\* \[ 0.30315,360 ] MIB (\[con Tesla T4])



\- \*\*Dónde se ejecuta:\*\* \[Colab con GPU]



\- \*\*Por qué:\*\* \[Procesaremos fotogramas en lotes



pequeños para controlar la memoria. ]



&#x20;



\## 4. Riesgo ético



&#x20;



\- \*\*Riesgo:\*\* \[Privacidad: las grabaciones pueden mostrar conversaciones o datos personales. ]



\- \*\*Mitigación:\*\* \[Usaremos videos



propios o autorizados, eliminaremos los archivos temporales al terminar y no publicaremos las



grabaciones en el repositorio. ]






&#x20;



\## 5. Evidencia

<img width="658" height="404" alt="Captura de pantalla 2026-10-29 083137" src="https://github.com/user-attachments/assets/f70ecbd0-84be-4e37-bd0e-b35e4ec49ebe" />
<img width="654" height="379" alt="Captura de pantalla 2026-10-29 083009" src="https://github.com/user-attachments/assets/780ca020-0a24-4709-96d3-bbd94729165d" />

