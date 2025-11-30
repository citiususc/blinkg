import os
import re

def extract_tables(md_text: str) -> list[str]:
    """
    Extrae todos los bloques de tabla Markdown de un texto.
    Una tabla empieza con una línea que contiene '|' y cuya
    siguiente línea es la de delimitador (guiones y pipes).
    """
    lines = md_text.splitlines()
    tables = []
    in_table = False
    buf = []

    for idx, line in enumerate(lines):
        if not in_table:
            # buscar inicio de tabla: línea con '|' y lookahead a delimitador
            if '|' in line and idx+1 < len(lines) and re.match(r'^\s*\|?[-:\s|]+\|?\s*$', lines[idx+1]):
                in_table = True
                buf = [line]
        else:
            # mientras siga habiendo '|' recogemos filas
            if '|' in line:
                buf.append(line)
            else:
                # fin de bloque de tabla
                tables.append('\n'.join(buf))
                in_table = False
        # último bloque al final del archivo
    if in_table and buf:
        tables.append('\n'.join(buf))

    return tables

def clean_md_file(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    tables = extract_tables(text)

    new_header = (
        "| CSV Column           | Ontology Property | Entity Class | "
        "Rel. Entity Class | Subject Generation    | Join Condition | "
        "Datatype | Function Name | Function Output |"
    )
    new_delimiter = "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"

    new_tables = []
    for table in tables:
        lines = table.splitlines()
        if len(lines) >= 2:
            # Replace header and delimiter
            lines[0] = new_header
            lines[1] = new_delimiter

            # Count how many columns we should have
            header_cells = [cell for cell in lines[0].split('|') if cell.strip()]
            header_count = len(header_cells)
            empty_values = ['', '-', ' ', 'N/A', 'None', '—', '–']

            processed_rows = lines[:2]
            # Process each data row
            for row in lines[2:]:
                # Extract the cell texts (drop leading/trailing '|')
                cells = [c.strip() for c in row.split('|')[1:-1]]

                # If there are more cells than headers, merge extras into the last valid cell
                if len(cells) > header_count:
                    valid = cells[:header_count]       # keep exactly as many as headers
                    extras = cells[header_count:]      # everything beyond
                    # drop any “empty placeholder” in the extras
                    extras_clean = [e for e in extras if e not in empty_values]
                    # append non-empty extras onto the last valid cell
                    if extras_clean:
                        valid[-1] = valid[-1] + ' ' + ' '.join(extras_clean)
                    cells = valid

                # Rebuild the Markdown row with the correct number of columns
                processed_rows.append("| " + " | ".join(cells) + " |")

            lines = processed_rows

        new_tables.append("\n".join(lines))

    new_text = ("\n\n".join(new_tables) + "\n") if new_tables else ""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)

def process_folder(root_dir: str) -> None:
    """
    Recorre recursivamente root_dir y limpia cada .md encontrado.
    """
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.lower().endswith('.md'):
                full_path = os.path.join(dirpath, fname)
                clean_md_file(full_path)
                print(f'→ Limpió tablas en {full_path}')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Extrae y normaliza tablas Markdown en un directorio"
    )
    parser.add_argument(
        "root_dir",
        help="Directorio raíz donde buscar archivos .md"
    )
    args = parser.parse_args()
    process_folder(args.root_dir)