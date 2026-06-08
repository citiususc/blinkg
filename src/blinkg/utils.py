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


def _prefixes(ontology: Graph | None) -> dict:
    """Union of the built-in prefix_map and the ontology's declared namespaces."""
    out = dict(prefix_map)
    if ontology is not None:
        for prefix, ns in ontology.namespaces():
            out[prefix] = str(ns)
    return out


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



def strip_shared_prefixes(v1: str, v2: str, ontology: Graph | None = None) -> tuple[str, str]:
    """
    Remove only those prefixes or base URIs that appear in both v1 and v2.
    When the ontology is provided, its declared namespaces extend the built-in prefix_map.
    """
    if not isinstance(v1, str) or not isinstance(v2, str):
        return v1, v2
    for prefix, base_uri in _prefixes(ontology).items():
        # strip prefix:LocalName if both share the prefix
        if v1.startswith(f"{prefix}:") and v2.startswith(f"{prefix}:"):
            v1 = v1.split(":", 1)[1]
            v2 = v2.split(":", 1)[1]
        # strip base URI if both share it
        if base_uri and v1.startswith(base_uri) and v2.startswith(base_uri):
            v1 = v1[len(base_uri):]
            v2 = v2[len(base_uri):]
    return v1, v2

_CURIE_RE = re.compile(r"(?<![\w/:])(\w*):([\w.-]+)")


def expand_to_full_uri(text: str, ontology: Graph | None = None) -> str:
    """
    Expand every prefix:LocalName occurrence in ``text`` to base_uri+LocalName.
    When the ontology is provided, its declared namespaces extend the built-in prefix_map.
    """
    if not isinstance(text, str):
        return text
    prefixes = _prefixes(ontology)
    return _CURIE_RE.sub(
        lambda m: prefixes[m.group(1)] + m.group(2) if m.group(1) in prefixes else m.group(0),
        text,
    )


def clean_values(v1, v2, ontology: Graph | None = None):
    raw1, raw2 = expand_to_full_uri(v1, ontology), expand_to_full_uri(v2, ontology)
    v1, v2 = strip_shared_prefixes(raw1, raw2, ontology)
    return v1, v2
