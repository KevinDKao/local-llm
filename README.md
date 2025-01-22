# local-llm
Building my own local large language model. 


# Status

Please don't review this repo. It's very messy and I've spent most of my time setting other things up

# Current Status [Personal Note]

Currently completed installing Ollama, Went to hugging face and found my llm I wanted to run, quantized it, and installed it

Bartowski Quantized model/

ollama run hf.co/bartowski/DeepSeek-R1-Distill-Qwen-14B-GGUF:Q5_K_M

I chose this model for the strong MuSR performance and mid-range computational requirements 

Multistep Soft Reasoning (MuSR):

    Scope: Reasoning and understanding on/of long texts

        Language understanding

        Reasoning capabilities

        Long context reasoning

    Scoring: Accuracy: Was the correct choice selected among the options.

# Run this command
ollama run hf.co/bartowski/DeepSeek-R1-Distill-Qwen-14B-GGUF:Q5_K_M
