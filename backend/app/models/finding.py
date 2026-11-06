from pydantic import BaseModel
class Finding(BaseModel):
    indicator:str
    confidence:float
    evidence:list[str]
