import pandas as pd
import glob
import os


def merge_csvs_similarity(input_pattern: str, output_path: str):
    """
    Recorre todos los CSVs que coincidan con input_pattern, los concatena
    y añade dos columnas ('LLM' y 'method') extraídas del nombre de archivo,
    asumiendo que cada fichero tiene nombre "{LLM}_{method}.csv".

    :param input_pattern: Patrón glob para los CSVs (e.g. 'scenario1/1A/*/*.csv')
    :param output_path: Ruta donde se guardará el CSV unido (e.g. 'merged.csv')
    """
    csv_files = glob.glob(input_pattern)
    if not csv_files:
        raise FileNotFoundError(f"No se encontraron archivos con el patrón: {input_pattern}")

    dfs = []
    for fp in csv_files:
        df = pd.read_csv(fp)
        # extrae partes del nombre de fichero y separa LLM y método
        filename = os.path.splitext(os.path.basename(fp))[0]
        # identificar el método al final del nombre completo
        for m in ('bert_lexical', 'levenshtein', 'bert', 'bert_column_match','max_all'):
            if filename.endswith(f"_{m}"):
                method = m
                llm_str = filename[:-(len(m) + 1)]
                break
        else:
            continue
            #raise ValueError(f"Método no reconocido: '{filename}'")
        # limpiar LLM: eliminar 'hf' y '2.5'
        llm_parts = [p for p in llm_str.split('_') if p not in ('hf', '2.5')]
        llm = '_'.join(llm_parts)
        df['LLM'] = llm
        df['method'] = method
        df['column'] = df['column'].replace('XML Path', 'Data Reference')
        dfs.append(df)

    # concatena todos y reinicia índices
    merged = pd.concat(dfs, ignore_index=True)
    merged.to_csv(output_path, index=False)
    print(f"Guardado {len(merged)} filas en '{output_path}'")



def merge_csvs_with_prf(input_pattern: str, output_path: str):
    """
    Recorre todos los CSVs que coincidan con input_pattern, los concatena
    y añade una columna 'method' con el nombre del fichero (sin extensión).

    :param input_pattern: Patrón glob para los CSVs (p. ej. 'results/*.csv')
    :param output_path:    Ruta donde se guardará el CSV unido (p. ej. 'merged.csv')
    """
    csv_files = glob.glob(input_pattern)
    if not csv_files:
        raise FileNotFoundError(f"No se encontraron archivos con el patrón: {input_pattern}")

    dfs = []
    for fp in csv_files:
        df = pd.read_csv(fp)
        method = os.path.splitext(os.path.basename(fp))[0]
        df['method'] = method
        dfs.append(df)

    merged = pd.concat(dfs, ignore_index=True)
    merged.to_csv(output_path, index=False)
    print(f"Guardado {len(merged)} filas en '{output_path}'")


def merge_prf_to_f(root_dir: str, output_path: str):
    """
    Busca recursivamente archivos 'complete_results_*.csv' bajo root_dir,
    concatena todos los resultados, normaliza 'method' hasta el primer '_',
    calcula la media de F1 por (method, column) y genera un pivot table
    donde cada fila es un método y cada columna es un valor de 'column'.

    :param root_dir:    Directorio raíz donde buscar los CSVs
    :param output_path: Ruta de salida para el CSV pivotado
    """
    # 1) localizar y leer todos los CSVs
    values = [80]
    for t in values:
        pattern = os.path.join(root_dir, "**", f"complete_results_prf_*.csv")
        files = glob.glob(pattern, recursive=True)
        if not files:
            raise FileNotFoundError(f"No se encontraron archivos en '{root_dir}'")

        dfs = []
        for fp in files:
            df = pd.read_csv(fp)
            # recortar 'method' hasta el primer '_'
            df['method'] = df['method'].astype(str).str.partition('_')[0]
            dfs.append(df[['column', 'f1', 'method']])

        # 2) concatenar y agrupar para calcular medias
        all_df = pd.concat(dfs, ignore_index=True)
        agg = (
            all_df
            .groupby(['method', 'column'], as_index=False)['f1']
            .mean()
            .rename(columns={'f1': 'mean_f1'})
        )


        pivot = agg.pivot(index='method', columns='column', values='mean_f1')

        desired_cols = [
            "CSV Column","Ontology Property", "Entity Class", "Related Entity Class",
            "Subject Generation", "Join Condition", "Datatype", "Function Name", "Function Output"
        ]
        pivot = pivot.reindex(columns=desired_cols)


        pivot.to_csv(output_path.replace("_f",f"_f_{t}"), float_format="%.9f")
        print(f"Guardado pivot table con {pivot.shape[0]} métodos y {pivot.shape[1]} columnas en '{output_path}'")


def merge_prf_to_multi_pivot(root_dir: str, output_path: str):
    """
    Busca recursivamente archivos 'complete_results_prf_*.csv' bajo root_dir,
    concatena todos los resultados, normaliza 'method' (hasta el primer '_'),
    calcula la media de precision, recall y f1 por (method, column) y genera
    un pivot table donde las columnas son un MultiIndex (metric, column).
    """
    # 1) localizar y leer todos los CSVs
    pattern = os.path.join(root_dir, "**", "complete_results_prf_*.csv")
    files = glob.glob(pattern, recursive=True)
    if not files:
        raise FileNotFoundError(f"No se encontraron archivos en '{root_dir}'")

    dfs = []
    for fp in files:
        df = pd.read_csv(fp)
        # recortar 'method' hasta el primer '_'
        df['method'] = df['method'].astype(str).str.partition('_')[0]
        # quedarnos con las métricas + column + method
        dfs.append(df[['column', 'precision', 'recall', 'f1', 'method']])

    # 2) concatenar y agrupar para calcular medias
    all_df = pd.concat(dfs, ignore_index=True)
    agg = (
        all_df
        .groupby(['method', 'column'], as_index=False)
        .agg({
            'precision': 'mean',
            'recall':    'mean',
            'f1':        'mean'
        })
    )

    # 3) pivot con MultiIndex en columnas: (metric, column)
    pivot = agg.pivot_table(
        index='method',
        columns='column',
        values=['precision','recall','f1']
    )

    # 4) reordenar las columnas (añadiendo CSV Column si no existiera)
    desired_cols = [
        "CSV Column", "Datatype", "Entity Class", "Rel. Entity Class",
        "Subject Generation", "Join Condition", "Ontology Property",
        "Function Name", "Function Output"
    ]
    # asegurar que todas estén en el pivot (añadiendo columnas vacías si falta)
    for col in desired_cols:
        if col not in pivot.columns.get_level_values(1):
            for metric in ['precision','recall','f1']:
                pivot[(metric, col)] = pd.NA

    # ahora reindexar
    metrics = ['precision', 'recall', 'f1']
    cols = desired_cols

    full_index = pd.MultiIndex.from_product(
        [metrics, cols],
        names=['metric', 'column']
    )

    pivot = pivot.reindex(
        index=pivot.index,
        columns=full_index,
        fill_value=pd.NA
    )

    # 5) (Opcional) aplanar el MultiIndex en columnas simples
    pivot.columns = [
        f"{metric}_{column}" for metric, column in pivot.columns
    ]

    # 6) guardar
    pivot.to_csv(output_path, float_format="%.9f")
    print(f"Guardado pivot table con {pivot.shape[0]} métodos y {pivot.shape[1]} columnas en '{output_path}'")
    transpose_prf_with_modes(output_path, output_path.replace("_prf","_transpose_prf"))


def transpose_prf_with_modes(input_csv: str, output_csv: str):
    """
    Load PRF results (methods only, no suffix), then build a transposed table:
    - Rows: Task x Metric in specified order
    - Columns: MultiIndex(Method, Mode) for modes Manual, Automatic-Raw, Automatic-Clean
    - Fill only Automatic-Raw values; Manual and Automatic-Clean remain empty
    """
    # Load data
    df = pd.read_csv(input_csv)

    # Define tasks and metrics
    tasks = [
        "CSV Column", "Datatype", "Entity Class", "Rel. Entity Class",
        "Subject Generation", "Join Condition", "Ontology Property",
        "Function Name", "Function Output"
    ]
    metrics = ['precision', 'recall', 'f1']

    # Prepare full index and columns
    full_index = pd.MultiIndex.from_product([tasks, metrics], names=['Task', 'Metric'])
    methods = sorted(df['method'].unique())
    modes = ['Manual', 'Automatic-Raw', 'Automatic-Clean']
    full_cols = pd.MultiIndex.from_product([methods, modes], names=['Method', 'Mode'])

    # Initialize empty DataFrame
    full_df = pd.DataFrame(index=full_index, columns=full_cols, dtype=float)

    # Fill Automatic-Raw values from df
    for _, row in df.iterrows():
        method = row['method']
        for task in tasks:
            for metric in metrics:
                col_name = f"{metric}_{task}"
                if col_name in row:
                    full_df.at[(task, metric), (method, 'Automatic-Clean')] = row[col_name]

    # Save to CSV
    full_df.to_csv(
        output_csv,
        sep=';',
        decimal=',',
        float_format="%.9f",
        na_rep=''
    )
    print(f"Transposed PRF with modes saved to '{output_csv}'")


def aggregate_results(root_dir: str,  output_over_methods: str = "mean_by_column_LLM.csv"):
    """
    Busca recursivamente todos los archivos 'complete_results.csv' bajo root_dir,
    concatena sus datos y genera dos CSVs:

    1) output_method: media de mean_similarity agrupada por (column, LLM, method)
    2) output_over_methods: media de mean_similarity agrupada por (column, LLM),
       es decir, todos los métodos juntos.
    """
    pattern = os.path.join(root_dir, "**", "complete_results_sim*.csv")
    files = glob.glob(pattern, recursive=True)
    if not files:
        raise FileNotFoundError(f"No se encontraron archivos en '{root_dir}'")

    # Leer y concatenar
    dfs = []
    for fp in files:
        df = pd.read_csv(fp)
        dfs.append(df)
    all_df = pd.concat(dfs, ignore_index=True)

    # 2) Media por column, LLM (todos los métodos juntos)
    agg_over_methods = (
        all_df
        .groupby(['column', 'LLM'], as_index=False)
        ['mean_similarity']
        .mean()
    )
    agg_over_methods.to_csv(output_over_methods, index=False)
    print(f"Guardado: {output_over_methods}")
