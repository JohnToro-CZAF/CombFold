#@title Run Prediction

import sys
import argparse

from colabfold.batch import get_queries, run
from colabfold.download import default_data_dir
from colabfold.utils import setup_logging
from pathlib import Path

# input_dir = '/content/01192' #@param {type:"string"}
# result_dir = '/content/01192_pdbs' #@param {type:"string"}
# msa_mode = "MMseqs2 (UniRef+Environmental)" #@param ["MMseqs2 (UniRef+Environmental)", "MMseqs2 (UniRef only)","single_sequence","custom"]
# num_models = 1 #@param [1,2,3,4,5] {type:"raw"}
# num_recycles = 3 #@param [1,3,6,12,24,48] {type:"raw"}
# stop_at_score = 100 #@param {type:"string"}
# use_custom_msa = False
# num_relax = 0
# use_amber = num_relax > 0
# relax_max_iterations = 200
# use_templates = False
# do_not_overwrite_results = True
# zip_results = False


parser = argparse.ArgumentParser()
parser.add_argument("--result_dir", type=str, required=True)
parser.add_argument("--input_dir", type=str, required=True)
parser.add_argument("--use_templates", type=bool, default=False)
parser.add_argument("--num_relax", type=int, default=0)
parser.add_argument("--relax_max_iterations", type=int, default=200)
parser.add_argument("--msa_mode", type=str, default="MMseqs2 (UniRef+Environmental)")
parser.add_argument("--num_models", type=int, default=1)
parser.add_argument("--num_recycles", type=int, default=3)
parser.add_argument("--do_not_overwrite_results", type=bool, default=True)
parser.add_argument("--rank_by", type=str, default="auto")
parser.add_argument("--stop_at_score", type=float, default=100)
parser.add_argument("--zip_results", type=bool, default=False)

args = parser.parse_args()
setup_logging(Path(args.result_dir).joinpath("log.txt"))

queries, is_complex = get_queries(args.input_dir)
run(
    queries=queries,
    result_dir=args.result_dir,
    use_templates=args.use_templates,
    num_relax=args.num_relax,
    relax_max_iterations=args.relax_max_iterations,
    msa_mode=args.msa_mode,
    model_type="auto",
    num_models=args.num_models,
    num_recycles=args.num_recycles,
    model_order=[1, 2, 3, 4, 5],
    is_complex=is_complex,
    data_dir=default_data_dir,
    keep_existing_results=args.do_not_overwrite_results,
    rank_by=args.rank_by,
    pair_mode="unpaired+paired",
    stop_at_score=args.stop_at_score,
    zip_results=args.zip_results,
    user_agent="colabfold/google-colab-batch",
)