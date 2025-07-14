# K-HALU
K-HALU: Multiple Answer Korean Hallucination Benchmark for Large Language Models [[Paper](https://openreview.net/forum?id=VnLhUogHYE)]

*Jaehyung Seo and Heuiseok Lim* 

🏫 [NLP & AI Lab](https://nlp.korea.ac.kr/), Korea University

### 📊 Dataset Download

The **K-HALU** dataset is available on **AI-HUB**.  
🔗 [Dataset Link](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=120&topMenu=100&aihubDataSe=extrldata&dataSetSn=71872)

- The K-HALU dataset is available for download and use through the provided link upon **agreeing to the usage policy and submitting a usage application**.
- K-HALU has been developed and released in compliance with the **National Information Society Agency of Korea (NIA)**’s data usage policies and registration procedures.

---

### 🔥 News (BugFIX)

- **February 21, 2025**: The official GitHub repository for K-HALU is now open.  
- **February 24 - March 2025**: The K-HALU dataset will be available (via the link above).  
- **June 2025**: Official evaluation scripts for K-HALU will be released.
- **July 14, 2025**: Bug Fixes
  
  1. *Bug where `task_list` was not recognized*: fixed registry conflict by renaming k_halu.yaml to *`k_halu_logit.yaml`* and task name from k_halu to *`k_halu_log`*.
  
  2. Applied distinction between `normalized and non-normalized` scores in the results.
  
### 🛠️ Installation

This repository partially adopts the evaluation methods from version **0.4.1** of [EleutherAI/lm-eval-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/v0.3.0) for evaluating K-HALU.

```bash
$ git clone https://github.com/J-Seo/K-HALU.git
```

```bash
# Requires Python >= 3.10.0, torch >= 2.1.0
## If you want to use the latest models, update your `transformers` library to the latest version.
$ cd K-HALU
$ pip install -r requirements.txt
$ cd lm-evaluation-harness
$ pip install -e .
```

### 🚀 Usage

This repository includes the evaluation script for the sample version of the K-HALU benchmark, available at [`J-Seo/k_halu_samples`](https://huggingface.co/datasets/J-Seo/k_halu_samples) on Hugging Face.

⚠️ Please note that the full version is currently pending upload to AI-HUB and may take some time.

The `test.sh` script evaluates model performance using either logit-based scoring or exact match metrics.

You can modify the .yaml and .py files under lm_eval/tasks/k_halu to match your own experimental environment or preferred evaluation method.

To evaluate a model using the sample version of K-HALU:
```bash
lm_eval --model hf \
--model_args pretrained="meta-llama/Llama-2-7b-chat-hf"  \
--tasks k_halu_log \             # Use 'k_halu_em' for exact match evaluation
--device cuda:0 \
--batch_size 4 \
--use_cache ./cache/llama2_samples \ # Enable caching for faster evaluation
--log_samples \
--output_path ./results/llama2_samples & # Save logs and results
```

Run the Evaluation
```bash
$ cd lm-evaluation-harness
$ sh test.sh
```

Below are sample outputs from running the benchmark with `LLaMA-2-7B-Chat`


```bash
hf (pretrained=meta-llama/Llama-2-7b-chat-hf), gen_kwargs: (), limit: None, num_fewshot: None, batch_size: 4
|Tasks |Version|Filter|n-shot| Metric  |Value |   |Stderr|
|------|-------|------|-----:|---------|-----:|---|-----:|
|k_halu|Yaml   |none  |     0|f1       |0.4273|±  |0.0840|
|      |       |none  |     0|precision|0.4672|±  |0.0852|
|      |       |none  |     0|recall   |0.4300|±  |0.0943|
|      |       |none  |     0|acc_norm |0.2857|±  |0.1010|


hf (pretrained=meta-llama/Llama-2-7b-chat-hf), gen_kwargs: (), limit: None, num_fewshot: None, batch_size: 4
|  Tasks  |Version|Filter|n-shot|Metric|Value |   |Stderr|
|---------|-------|------|-----:|------|-----:|---|-----:|
|k_halu_em|Yaml   |none  |     0|acc   |0.0476|±  |0.0476|
```

### How to Use the AI-HUB Dataset

Modify the `dataset_path` in `./K-HALU/lm-evaluation-harness/lm_eval/tasks/k_halu/k_halu_logit.yaml` 
to point to the downloaded file `k_halu_test_v1_1.jsonl`.

```bash
task: k_halu_log
**dataset_path: !CustomPath/k_halu_test_v1_1.jsonl**
dataset_name: null
output_type: multiple_choice
#training_split: train
test_split: test
process_docs: !function utils.process_docs_zero
doc_to_text: "{{query}}"
doc_to_target: "{{label}}"
doc_to_choice: "{{choices}}"
metric_list:
  - metric: f1
    aggregation: f1
    higher_is_better: true
  - metric: precision
    aggregation: precision
    higher_is_better: true
  - metric: recall
    aggregation: recall
    higher_is_better: true
  - metric: acc_norm
    aggregation: mean
    higher_is_better: true
metadata:
  - version: 0.0

```

### 📖 Citation

```bash
@inproceedings{
seo2025khalu,
title={K-{HALU}: Multiple Answer Korean Hallucination Benchmark for Large Language Models},
author={Jaehyung Seo and Heuiseok Lim},
booktitle={The Thirteenth International Conference on Learning Representations},
year={2025},
url={https://openreview.net/forum?id=VnLhUogHYE}
}
```

### 🙏 Acknowledgement
K-HALU used datasets from The Open AI Dataset Project (AI-Hub, S. Korea). All dataset-related information can be accessed through AI-Hub (www.aihub.or.kr).

