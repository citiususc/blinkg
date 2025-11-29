import pandas as pd
import re


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
