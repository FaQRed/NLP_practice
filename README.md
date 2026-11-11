# NLP Practice

Exercises for the Natural Language Processing (NLP) course at PJATK.

Author: Kiryl Sankouski ([@FaQRed](https://github.com/FaQRed))

## Contents

- `lesson_01/01_Tokenizacja.ipynb` - tokenization, vocabulary and OOV, pre-processing, model tokenizers (BERT, DistilBERT, RoBERTa), POS tagging and Matcher in spaCy
- `lesson_02/2-Wektory-slow-PJN.ipynb` - word vectors: one-hot vs embeddings, cosine similarity, Polish pre-trained vectors (gensim KeyedVectors), Word Mover's Distance, contextual embeddings (Flair), Q&A bot based on sentence similarity
- `lesson_03/3 - LSTM - PJN.ipynb` - LSTM: cell state and gates, next-word prediction with a trainable embedding layer, sequence-to-sequence next-sentence prediction (encoder-decoder LSTM on Flair sentence embeddings, nearest sentence by cosine similarity)
- `lesson_04/4 - Transformers, część 1_ attention - PJN.ipynb` - Transformers, part 1: attention mechanism (queries, keys, values), scaled dot-product attention step by step on vectors and matrices (NumPy), self-attention heatmap, multi-head attention (PyTorch, output projection W_O), exercises: attention by hand and a two-head attention implementation with weight visualization
- `lesson_05/5 - Transformers, część 2_ architektura - PJN.ipynb` - Transformers, part 2: full architecture, positional encoding (sin/cos), encoder layer (multi-head self-attention, Add & Norm, feed forward), decoder layer (masked self-attention, encoder-decoder cross-attention), linear + softmax output, exercises: causal mask for self-attention and a mini-Transformer (nn.Transformer) trained on a copy task with teacher forcing and token-by-token generation
- `lesson_06/6 - Tuning, LoRA - PJN.ipynb` - fine-tuning and LoRA: pre-training vs fine-tuning, full fine-tuning of DistilBERT for IMDb sentiment classification (Trainer, TrainingArguments, inference on MPS), low-rank adaptation (matrices A and B, rank r, alpha), exercise: LoRA fine-tuning of distilgpt2 on Abirate/english_quotes with peft (LoraConfig, get_peft_model, data collator for causal LM) and text generation
