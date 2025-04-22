lm_eval --model hf \
--model_args pretrained="meta-llama/Llama-2-7b-chat-hf" \
--tasks k_halu \
--device cuda:0 \
--batch_size 4 \
--use_cache ./cache/llama2_samples_em \
--log_samples \
--output_path ./results/llama2_samples &

lm_eval --model hf \
--model_args pretrained="meta-llama/Meta-Llama-3-8B-Instruct" \
--tasks k_halu \
--device cuda:1 \
--batch_size 4 \
--use_cache ./cache/llama3_samples \
--log_samples \
--output_path ./results/llama3_samples &

#
#lm_eval --model hf \
#--model_args pretrained="nlpai-lab/KULLM3" \
#--tasks k_halu \
#--device cuda:0 \
#--batch_size 4 \
#--use_cache ./cache/kullm3 \
#--log_samples \
#--output_path ./results/kullm3_samples &
#
#lm_eval --model hf \
#--model_args pretrained="mistralai/Mistral-Nemo-Instruct-2407" \
#--tasks k_halu \
#--device cuda:1 \
#--batch_size 4 \
#--use_cache ./cache/mistral \
#--log_samples \
#--output_path ./results/mistral_samples &
####
#
#lm_eval --model hf \
#--model_args pretrained="LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct" \
#--tasks k_halu \
#--device cuda:0 \
#--batch_size 4 \
#--use_cache ./cache/exaone \
#--log_samples \
#--output_path ./results/exaone_samples &

## 생성
#lm_eval --model hf \
#--model_args pretrained="meta-llama/Llama-2-7b-chat-hf" \
#--tasks k_halu_em \
#--device cuda:0 \
#--batch_size 4 \
#--num_fewshot 0 \
#--use_cache ./cache/llama2 \
#--log_samples \
#--output_path ./results/llama2_samples_em &
#
#lm_eval --model hf \
#--model_args pretrained="meta-llama/Meta-Llama-3-8B-Instruct" \
#--tasks k_halu_em \
#--device cuda:1 \
#--batch_size 4 \
#--num_fewshot 0 \
#--use_cache ./cache/llama3 \
#--log_samples \
#--output_path ./results/llama3_samples_em &
##
#lm_eval --model hf \
#--model_args pretrained="nlpai-lab/KULLM3" \
#--tasks k_halu_em \
#--device cuda:1 \
#--batch_size 4 \
#--num_fewshot 0 \
#--use_cache ./cache/kullm3 \
#--log_samples \
#--output_path ./results/kullm3_samples_em &
#
#lm_eval --model hf \
#--model_args pretrained="mistralai/Mistral-Nemo-Instruct-2407" \
#--tasks k_halu_em \
#--device cuda:0 \
#--batch_size 4 \
#--num_fewshot 0 \
#--use_cache ./cache/mistral \
#--log_samples \
#--output_path ./results/mistral_samples_em &
##
#lm_eval --model hf \
#--model_args pretrained="LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct" \
#--tasks k_halu_em \
#--device cuda:1 \
#--batch_size 4 \
#--num_fewshot 0 \
#--use_cache ./cache/exaone \
#--log_samples \
#--output_path ./results/exaone_samples_em &
