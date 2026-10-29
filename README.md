# NLP Practice

Exercises for the Natural Language Processing (NLP) course at PJATK.

Author: Kiryl Sankouski ([@FaQRed](https://github.com/FaQRed))

## Contents

- `lesson_01/01_Tokenizacja.ipynb` - tokenization, vocabulary and OOV, pre-processing, model tokenizers (BERT, DistilBERT, RoBERTa), POS tagging and Matcher in spaCy
- `lesson_02/2-Wektory-slow-PJN.ipynb` - word vectors: one-hot vs embeddings, cosine similarity, Polish pre-trained vectors (gensim KeyedVectors), Word Mover's Distance, contextual embeddings (Flair), Q&A bot based on sentence similarity
- `lesson_03/3 - LSTM - PJN.ipynb` - LSTM: cell state and gates, next-word prediction with a trainable embedding layer, sequence-to-sequence next-sentence prediction (encoder-decoder LSTM on Flair sentence embeddings, nearest sentence by cosine similarity)
- `lesson_04/4 - Transformers, część 1_ attention - PJN.ipynb` - Transformers, part 1: attention mechanism (queries, keys, values), scaled dot-product attention step by step on vectors and matrices (NumPy), self-attention heatmap, multi-head attention (PyTorch, output projection W_O), exercises: attention by hand and a two-head attention implementation with weight visualization
