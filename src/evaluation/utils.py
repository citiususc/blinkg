import pandas as pd
import re
from sentence_transformers import SentenceTransformer
import torch
from rdflib import Graph, URIRef, RDFS
import logging

# Solo mostrar errores (ERROR+) de rdflib, no warnings ni info
logging.getLogger("rdflib").setLevel(logging.ERROR)

empty_values = ['', '-', ' ', 'N/A', 'None','—', '–', '–', '–']

model = SentenceTransformer('all-mpnet-base-v2')
model.eval()

prefix_map = {
    "ex": "http://example.org/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "owl": "http://www.w3.org/2002/07/owl#"
}


def get_property_lexicalization(property_uri: str, g: Graph, lang: str = None) -> str:
    """
    Carga la ontología desde ontology_path y busca la propiedad property_uri.
    Devuelve la concatenación de rdfs:label y rdfs:comment (filtrados por idioma si se especifica).

    :param property_uri: URI completo de la propiedad a buscar.
    :param lang: Código de idioma (e.g. 'es', 'en'); si None, toma todos los literales.
    :return: String resultante de label + " - " + comment, o mensaje si no existe.
    """
    if not (property_uri.startswith("http://") or property_uri.startswith("https://")) \
            or "{" in property_uri or "}" in property_uri:
        return property_uri
    try:
        prop = URIRef(property_uri)
        if (prop, None, None) not in g:
            return property_uri
    except:
        return property_uri

    # Recopilar labels y comments
    labels = []
    comments = []
    for _, _, lbl in g.triples((prop, RDFS.label, None)):
        if lang is None or lbl.language == lang:
            labels.append(str(lbl))
    for _, _, cmt in g.triples((prop, RDFS.comment, None)):
        if lang is None or cmt.language == lang:
            comments.append(str(cmt))

    # Construir la lexicalización
    parts = []
    if labels:
        parts.append(" / ".join(labels))
    if comments:
        parts.append(" / ".join(comments))

    if not parts:
        return f"No se encontró ni rdfs:label ni rdfs:comment para {property_uri}."

    # Por ejemplo: "Etiqueta1 / Etiqueta2 – Comentario1 / Comentario2"
    return " – ".join(parts)



def parse_md_table(md_text: str) -> pd.DataFrame:
    # Split into non-empty lines
    lines = [line.strip() for line in md_text.strip().split('\n') if line.strip()]
    # First line is header, rest are data or delimiter
    header = lines[0]
    data_lines = lines[2:]
    # Split each line by '|' into cells
    rows = [line.strip('|').split('|') for line in [header] + data_lines]
    # Create DataFrame from data rows
    df = pd.DataFrame(rows[1:], columns=rows[0])
    # Trim whitespace in column names
    df.columns = df.columns.str.strip()
    # Drop delimiter rows composed only of hyphens
    df = df[~df.apply(lambda row: all(re.fullmatch(r'-+', cell.strip()) for cell in row), axis=1)]
    # Strip whitespace from each cell
    # Strip whitespace and remove backticks from each cell
    return df.map(lambda x: str(x).replace('`', '').strip())


def strip_shared_prefixes(v1: str, v2: str) -> tuple[str, str]:
    """
    Remove only those prefixes or base URIs that appear in both v1 and v2.
    """
    if not isinstance(v1, str) or not isinstance(v2, str):
        return v1, v2
    for prefix, base_uri in prefix_map.items():
        # strip prefix:LocalName if both share the prefix
        if v1.startswith(f"{prefix}:") and v2.startswith(f"{prefix}:"):
            v1 = v1.split(":", 1)[1]
            v2 = v2.split(":", 1)[1]
        # strip base URI if both share it
        if base_uri and v1.startswith(base_uri) and v2.startswith(base_uri):
            v1 = v1[len(base_uri):]
            v2 = v2[len(base_uri):]
    return v1, v2

def expand_to_full_uri(text: str) -> str:
    """
    Expande prefix:LocalName a base_uriLocalName usando prefix_map.
    """
    if not isinstance(text, str):
        return text
    for prefix, base_uri in prefix_map.items():
        if text.startswith(f"{prefix}:"):
            return base_uri + text.split(":", 1)[1]
    return text


def clean_values(v1,v2):
    raw1, raw2 = expand_to_full_uri(v1), expand_to_full_uri(v2)
    v1, v2 = strip_shared_prefixes(raw1, raw2)
    return v1, v2