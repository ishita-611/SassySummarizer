This is a **work-in-progress**. The sarcasm model is still in therapy.

# SassySummarizer
Ever read something so boring it made you question your will to live? **SassySummarizer** is here to fix that.


This AI-powered chatbot takes your dull, academic, or way-too-formal text and transforms it into a short, **funny**, and **sarcastic** rewrite. Built with Hugging Face Transformers and a splash of chaotic humor, this is your new favorite tool for study recaps, sarcastic emails (maybe don't), or just spicing things up.

## Features

-  **Summarizes** long-form text using `distilBART`  
-  **Sarcastifies** it using `GPT-2` and some clever prompting  
-  **Interactive UI** built with Gradio

## Tech Stack

- [HuggingFace Transformers](https://huggingface.co/transformers/) – for BART & GPT-2 models  
- [Gradio](https://gradio.app) – to serve a slick browser UI  
- Python 3.8+

##  How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/sassy-summarizer.git
   cd sassy-summarizer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python index.py
   ```
4. Your browser will open. Paste some boring text. Watch the magic happen.

> ⚠️ **Heads up, mortal:**  
> This snarky summarizer runs on transformers, and those divas need a **GPU** to slay.  
> Run it on CPU if you *love waiting forever* (or watching your machine cry).  
> Use a GPU for the real magic
