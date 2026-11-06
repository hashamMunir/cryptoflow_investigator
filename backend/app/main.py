from fastapi import FastAPI
app=FastAPI(title="CryptoFlow Investigator")

@app.get("/health")
def health():
    return {"status":"ok"}
