import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_figure(results_path, output_path):
    # 1. Load data
    df = pd.read_csv(results_path)

    # 2. Create combined LLM_method column
    #if 'method' in df.columns:
    #    df['LLM_method'] = df['LLM'] + '_' + df['method']
    #else:
    df['LLM_method'] = df['LLM']
    df['LLM_method'] = df['LLM_method'].str.replace('_clean', '', regex=False)


    # 3. Pivot the table to prepare the heatmap
    pivot = df.pivot(index='column', columns='LLM_method', values='mean_similarity')

    # 3a. Clip values to [0, 1]
    pivot = pivot.clip(0.0, 1.0)

    # 4. Draw the heatmap with fixed color range 0→1
    fig, ax = plt.subplots(figsize=(14, 8))
    im = ax.imshow(pivot.values, aspect='auto', cmap='viridis', vmin=0.0, vmax=1.0)

    # 5. Annotate each cell with its value (two decimals)
    for i in range(pivot.shape[0]):
        for j in range(pivot.shape[1]):
            val = pivot.values[i, j]
            # choose text color for contrast
            text_color = 'white' if val < 0.5 else 'black'
            ax.text(j, i, f"{val:.2f}", ha='center', va='center', color=text_color, fontsize=8)

    # 6. Configure ticks, labels, and title
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, rotation=45, ha='right')
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index)
    ax.set_xlabel('LLM')
    ax.set_ylabel('Task')
    ax.set_title('Mean Similarity Heatmap Task VS LLM')

    # 7. Add color bar with ticks from 0 to 1 in steps of 0.1
    cbar = plt.colorbar(im, ax=ax, orientation='vertical', pad=0.02)
    cbar.set_label('Mean Similarity', rotation=270, labelpad=15)
    cbar.set_ticks(np.arange(0.0, 1.01, 0.1))

    # 8. Save the figure as a PNG
    plt.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)

    print(f"Heatmap saved to '{output_path}'")


def figures_f1(results_path, output_path):
    df = pd.read_csv(results_path)
    df.iloc[:, 1:] = df.iloc[:, 1:].replace(',', '.', regex=True).astype(float)

    # Reordenar columnas
    ordered_columns = [
        'Data Reference',
        'Subject Generation',
        'Entity Class',
        'Ontology Property',
        'Related Entity Class',
        'Join Condition',
        'Datatype',
        #'Language Annotations'
        'Function Name',
        'Function Output'
    ]
    df = df[['Method'] + ordered_columns]

    # Configuración del gráfico
    fig, ax = plt.subplots(figsize=(12, 6))

    labels = ordered_columns
    x = range(len(labels))
    bar_width = 0.13

    # Colores personalizados
    colors = ['#ccccff', '#DABBF7', '#9D86B8', '#5F4B66', '#56667A', '#7D938A']

    # Patrones hatch únicos
    hatch_patterns = ['/', '\\', 'x', '-', 'o', '.']

    # Dibujar barras
    for i, row in df.iterrows():
        ax.bar(
            [p + bar_width*i for p in x],
            row[1:],
            width=bar_width,
            label=row['Method'],
            color=colors[i % len(colors)],
            edgecolor='black',
            hatch=hatch_patterns[i % len(hatch_patterns)],
            linewidth=0.8
        )

    # Ejes y etiquetas
    ax.set_title("F1 Weighted Average", fontsize=16)
    ax.set_xticks([p + bar_width*2.5 for p in x])
    ax.set_xticklabels(labels, rotation=20, fontsize=10)
    ax.set_ylim([0, 1.0])
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Leyenda debajo del gráfico
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, fontsize=9)

    plt.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)

#figures_f1("../evaluation/scenario1_manual/measure_f.csv", "../evaluation/scenario1_manual/measure_f.png")
#figures_f1("../evaluation/scenario2_manual/measure_f.csv", "../evaluation/scenario2_manual/measure_f.png")
#figures_f1("../evaluation/scenario3_manual/measure_f.csv", "../evaluation/scenario3_manual/measure_f.png")


#figures_f1("../evaluation/scenario3_clean/mean_column_f_80.csv", "../evaluation/scenario3_clean/f1_3_clean.png")
#figures_f1("../evaluation/scenario3_no_clean/mean_column_f_80_no_clean.csv", "../evaluation/scenario3_no_clean/f1_3_noclean.png")

#figures_f1("../evaluation/scenario1_clean/mean_column_f_80.csv", "../evaluation/scenario1_clean/f1_1_clean.png")
#figures_f1("../evaluation/scenario1_no_clean/mean_column_f_80.csv", "../evaluation/scenario1_no_clean/f1_1_noclean.png")

figures_f1("../evaluation/scenario2_clean/mean_column_f_80.csv", "../evaluation/scenario2_clean/f1_2_clean.png")
figures_f1("../evaluation/scenario2_no_clean/mean_column_f_80.csv", "../evaluation/scenario2_no_clean/f1_2_noclean.png")