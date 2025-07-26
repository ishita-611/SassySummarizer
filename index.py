from transformers import pipeline
import gradio as gr

#step-1: summarizer: distilBART
summarizer=pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")
#step-2: sarcasm
sarcasm_generator=pipeline("text-generation","gpt2")

def sassify_text(text):
    summary=summarizer(text,max_length=150,min_length=30,do_sample=False)[0]['summary_text']

    #prepare sarcastic prompt
    prompt=f"Rewrite this in a sarcastic and funny tone \n{summary}"

    #generate sarcastic output
    sarcastic_output=sarcasm_generator(prompt,max_length=100,do_sample=True,top_k=50,temperature=1.0)[0]['generated-text']

    #remove prompt from output
    sarcastic_rewrite=sarcastic_output.replace(prompt,"").strip()

    return sarcastic_rewrite

#Gradio Interface
iface=gr.Interface(
    fn=sassify_text,
    inputs=gr.Textbox(lines=20,placeholder="place your boring text here..."),
    outputs="text",
    title="SassySummarizer🙄",
    description="Can't make yourself read through boring stuff? Just paste that shi here"
)

iface.launch()