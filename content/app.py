import streamlit as st

import torch


from transformers import T5Tokenizer, T5ForConditionalGeneration

# Page config

st.set_page_config(

    page_title="Automatic Lecture Summarizer",

    page_icon="📚",

    layout="centered"
)

# Title
st.title("📚 Automatic Lecture Summarizer")

st.subheader("Education-focused NLP Project using T5")

st.write(
    "Paste a lecture transcript below and generate a concise summary using a Transformer-based model."
)

# Load model (cached)
@st.cache_resource

def load_model():
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    return tokenizer, model

tokenizer, model = load_model()

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Text input
lecture_text = st.text_area(
    "📄 Lecture Text",
    height=250,
    placeholder="Paste your lecture transcript here..."
)

# Summarize button
if st.button("📝 Generate Summary"):
    if lecture_text.strip() == "":
        st.warning("Please enter some lecture text.")
    else:
        with st.spinner("Generating summary..."):
            input_text = "summarize: " + lecture_text

            inputs = tokenizer(
                input_text,
                return_tensors="pt",
                max_length=512,
                truncation=True
            ).to(device)

            summary_ids = model.generate(
                inputs["input_ids"],
                max_length=120,
                min_length=40,
                num_beams=6,
                no_repeat_ngram_size=3,
                repetition_penalty=2.5,
                length_penalty=1.8,
                early_stopping=True
            )

            summary = tokenizer.decode(
                summary_ids[0],
                skip_special_tokens=True
            )

        st.success("Summary Generated!")
        st.markdown("### ✨ Summary")
        st.write(summary)

# Footer
st.markdown("---")
st.caption("Developed as an NLP Capstone Project | HuggingFace + PyTorch")
st.caption("Developed By HA-MAW")
