📚 Automatic Lecture Summarizer using T5 (NLP Project)

##Project Overview

Hi Everyone ,This project is not just about the seeing the final result ,it's beyond that actually it's a base line!
It's more about to understand the fundamental work flow and pipeline structure of almost every modern day Complex NLP-Model!

Also this project is an education-focused NLP application that automatically generates concise summaries from long lecture transcripts.

The goal of this project was to understand how modern NLP models (Transformers) work in practice, especially:

Tokenization

Sequence-to-sequence learning

Fine-tuning pretrained models using Hugging Face

This is a learning-oriented project, built step by step to gain hands-on experience with NLP pipelines.


🙌Our Problem Statement

Students often struggle to revise long lecture transcripts.

Solution:
Build a system that takes a long lecture text as input and outputs a short, meaningful summary automatically.

🧠 Model Used

T5-Small (t5-small)

Transformer-based Encoder–Decoder (Seq2Seq) model

Pretrained on text-to-text tasks

Fine-tuned for lecture summarization

🗂️ Dataset

This project uses a small, manually created (dummy) dataset for learning purposes,as we are supposed to view the work flow only , so this dataset is good enough😊!

Each data sample consists of:

Input (xᵢ): Lecture text

Label (yᵢ): Corresponding summary

The data is converted into a Hugging Face Dataset format.

🔄 Project Workflow

Collect lecture transcripts (.txt files)

Clean and preprocess text

Create lecture–summary pairs

Convert data to Hugging Face Dataset

Tokenize inputs and labels

Fine-tune T5-Small using PyTorch

Evaluate using ROUGE metrics

Build a simple UI using Streamlit

🧹 Text Preprocessing

Remove timestamps and filler words

Normalize whitespace

Optional lowercasing

Prepare clean text for tokenization

🔤 Tokenization

Tokenizer: T5Tokenizer

Input format:

"summarize: <lecture text>"


Input and labels are tokenized separately

Max lengths are applied to avoid overflow

⚙️ Training Details

Framework: PyTorch

Library: Hugging Face Transformers

GPU used (if available)

Model fine-tuned for multiple epochs { this phase is important in case of learning}

Loss optimized using teacher forcing

📊 Evaluation

Evaluation is done using ROUGE metrics:

ROUGE-1

ROUGE-2

ROUGE-L

These scores compare generated summaries with reference summaries to measure overlap and quality.

🖥️ Web Interface (Demo) 😁At the end we have to check it as well...

A simple Streamlit UI is built to demonstrate the model:

Paste lecture text

Click “Summarize”

Get an auto-generated summary, We get summary ..it may seem like it is only slecting the words randomly ,,but my friends actually it genrates new sentemces based on the learning
which is know as ABRTRACTIVE SUMMARIZATION..

🚀 How to Run the Project.😊.
1️⃣ Install Dependencies
pip install torch .transformers .datasets .rouge-score .streamlit

2️⃣ Run the Streamlit App
streamlit run app.py


Then open:

http://localhost:8501

📌 Project Status🤗.. 

✅ Completed (Learning-focused implementation)
🔄 Can be improved with:

Larger dataset

Better summaries

More training epochs

Advanced evaluation

🧠 Key Learnings, Actually we supposed to get these things....

How transformer models process text🤷‍♀️

Importance of input–label pairs in Seq2Seq learning😎

Tokenization and attention masks🤨

Model fine-tuning vs inference✍️

Practical NLP workflow from data to UI🙌

🙌 Acknowledgements

Hugging Face 🤗 Transformers

PyTorch

Streamlit

📬 Author

Syed Haa-Meem 😊
Data Analytics & NLP Learner
Building projects to learn modern AI systems step by step.
