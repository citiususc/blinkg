
import argparse
import os
from utils import *
import glob
from evaluate import calculate_metrics
from merge_results import merge_csvs_similarity, merge_csvs_with_prf, merge_prf_to_f, aggregate_results, merge_prf_to_multi_pivot
from figures import create_figure,figures_f1


def define_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--scenario", required=True, help="Input path to the scenario")
    return parser


def eval_scenario(scenario_folder):
    root_dir = scenario_folder
    for experiment in os.listdir(root_dir):
        experiment_folder = os.path.join(root_dir, experiment)
        print(f"Evaluating {experiment_folder}")
        if os.path.isdir(experiment_folder) and (experiment != "results" and experiment!="data"):
            with open(os.path.join(experiment_folder, 'expected_table.md'), 'r', encoding='utf-8') as f:
                ground_truth = f.read()
            ground_truth = parse_md_table(ground_truth)
            for folder in os.listdir(experiment_folder):
                folder_path = os.path.join(experiment_folder, folder)
                pattern2 = os.path.join(folder_path, "*.csv")
                existing2 = glob.glob(pattern2)
                if (folder != "results" or folder != "data") and not existing2:
                    print("Evaluating " + folder_path)
                    if os.path.isdir(folder_path):
                        calculate_metrics(folder_path,ground_truth)
                else:
                    print(f"  → Skipping, found existing results: {existing2}")
            merge_csvs_similarity(f'{experiment_folder}/*/*max*.csv', f'{experiment_folder}/complete_results_sim_{experiment}.csv')
            merge_csvs_with_prf(f'{experiment_folder}/*/*80*.csv',f'{experiment_folder}/complete_results_prf_{experiment}.csv')
            #create_figure(f'{experiment_folder}/complete_results_sim_{experiment}.csv', f'{experiment_folder}/{experiment}.png')

    merge_prf_to_f(root_dir, f'{scenario_folder}/mean_column_f.csv')
    merge_prf_to_multi_pivot(root_dir, f'{scenario_folder}/mean_column_prf.csv')
    aggregate_results(root_dir, f'{scenario_folder}/mean_column_sim.csv')
    #create_figure(f'{scenario_folder}/mean_column_sim.csv', f'{scenario_folder}/mean_column_sim.png')
    #figures_f1(f'{scenario_folder}/mean_column_f_80.csv',f'{scenario_folder}/mean_column_f.png')


if __name__ == "__main__":
    args = define_args().parse_args()
    scenario_path = args.scenario
    eval_scenario(scenario_path)



