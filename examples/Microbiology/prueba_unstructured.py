from pathlib import Path
import time
# Requerido: pip install "unstructured[pdf]"
from unstructured.partition.pdf import partition_pdf

def element_to_markdown(element):
    """
    Convierte un elemento de Unstructured a sintaxis Markdown 
    según su categoría.
    """
    tipo = element.category.lower()
    texto = element.text.strip()

    if tipo == "title":
        # Podrías ajustar el nivel del # según metadatos si fuera necesario
        return f"# {texto}\n"
    elif tipo == "listitem":
        return f"* {texto}"
    elif tipo == "table":
        # Si Unstructured detecta una tabla y tiene activada la 
        # extracción de tablas, suele venir en metadata como HTML
        if hasattr(element.metadata, "text_as_html") and element.metadata.text_as_html:
            return f"\n{element.metadata.text_as_html}\n"
        return f"\n| {texto} |\n" # Fallback simple
    elif tipo == "pagenumber":
        return f"\n--- Página {texto} ---\n"
    else:
        # Texto narrativo, Header, Footer, etc.
        return f"{texto}\n"

def formatear_tiempo(segundos):
    horas, rem = divmod(int(segundos), 3600)
    minutos, segundos_res = divmod(rem, 60)
    partes = []
    if horas > 0: partes.append(f"{horas} h")
    if minutos > 0: partes.append(f"{minutos} m")
    partes.append(f"{segundos_res} s")
    return " ".join(partes)

# Rutas
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "pdf_para_prueba"
OUTPUT_DIR = BASE_DIR / "data_prueba_unstructured" # Mantenemos el nombre de tu carpeta

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

files = list(DATA_DIR.glob("**/*.pdf"))

for f in files:
    inicio = time.time()
    print(f"Procesando con fidelidad: {f.name}...")
    
    try:
    
        elements = partition_pdf(
            filename=str(f),
            strategy="hi_res",
            infer_table_structure=True, 
            languages=["spa"] # Ajusta según el idioma de tus PDFs
        )
        
        # Convertimos cada elemento detectado a Markdown
        lineas_markdown = [element_to_markdown(el) for el in elements]
        contenido_final = "\n".join(lineas_markdown)

        fin = time.time()
        tiempo_str = formatear_tiempo(fin - inicio)

        # Manejo de rutas
        ruta_relativa = f.relative_to(DATA_DIR)
        output_path = (OUTPUT_DIR / ruta_relativa).with_suffix(".md")
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as out:
            out.write(f"\n\n")
            out.write(contenido_final)
            
        print(f"Finalizado: {output_path.name} en {tiempo_str}")

    except Exception as e:
        print(f"Error en {f.name}: {e}")

print("\nProceso de alta fidelidad completado.")