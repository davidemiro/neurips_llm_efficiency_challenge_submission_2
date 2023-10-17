from datasets import load_dataset,concatenate_datasets
import sys
sys.path.insert(0, "/content/neurips_llm_efficiency_challenge")
from .dataset_orca import load_orca
from .dataset_p3_multi_qa import load_p3_multi_qa
from .dataset_multi_news_summarize import load_multi_news_summarize

def load():
    dataset_orca = load_orca()
    dataset_p3_multi_qa = load_p3_multi_qa()
    dataset_multi_news_summarize = load_multi_news_summarize()

    return concatenate_datasets([dataset_multi_news_summarize])

