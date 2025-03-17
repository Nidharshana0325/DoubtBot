from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load DeepSeek model
MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float32)
model.to("cpu")  # Ensure CPU usage

# Initialize FastAPI
app = FastAPI()

# Request schema
class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    try:
        
        prompt = f"<think>\nQuestion: {query.question}\nAnswer:"

        # Tokenize input
        inputs = tokenizer(prompt, return_tensors="pt")

        # Generate response with optimal settings
        with torch.no_grad():
            output = model.generate(
                **inputs, 
                max_length=50,  # Prevents excessive generation
                do_sample=True,  
                temperature=0.6,  # Recommended by DeepSeek
                top_k=50,  
                top_p=0.9  
            )
        
        # Decode and format response
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        response = response.replace(prompt, "").strip()  # Remove prompt from response

        return {"answer": response}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
