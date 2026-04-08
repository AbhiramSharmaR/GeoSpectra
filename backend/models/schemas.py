from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class AnalysisRequest(BaseModel):
    region: str

class MLResult(BaseModel):
    change_ratio: float
    classification: str
    output_image_path: str

class AnalysisResultResponse(BaseModel):
    id: str
    user_id: str
    region: str
    change_ratio: float
    classification: str
    report: str
    output_image_path: str
    timestamp: datetime
