from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from bson import ObjectId
from backend.models.schemas import AnalysisRequest, AnalysisResultResponse
from backend.auth.jwt import get_current_user
from backend.db.database import get_db
from backend.services.analysis_service import AnalysisService

router = APIRouter(prefix="/api/analysis", tags=["analysis"])

@router.get("/regions", response_model=List[str])
async def get_regions(current_user=Depends(get_current_user)):
    return AnalysisService.get_available_regions()

@router.post("/analyze", response_model=AnalysisResultResponse)
async def analyze_region(request: AnalysisRequest, current_user=Depends(get_current_user), db=Depends(get_db)):
    try:
        result_data = AnalysisService.perform_analysis(request.region)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    result_data["user_id"] = current_user["id"]
    
    db_result = await db["results"].insert_one(result_data)
    
    result_data["id"] = str(db_result.inserted_id)
    return AnalysisResultResponse(**result_data)

@router.get("/results", response_model=List[AnalysisResultResponse])
async def get_results(current_user=Depends(get_current_user), db=Depends(get_db)):
    cursor = db["results"].find({"user_id": current_user["id"]})
    results = []
    async for document in cursor:
        document["id"] = str(document["_id"])
        results.append(AnalysisResultResponse(**document))
    return results

@router.get("/results/{result_id}", response_model=AnalysisResultResponse)
async def get_result_by_id(result_id: str, current_user=Depends(get_current_user), db=Depends(get_db)):
    if not ObjectId.is_valid(result_id):
        raise HTTPException(status_code=400, detail="Invalid Result ID format")
        
    result = await db["results"].find_one({"_id": ObjectId(result_id), "user_id": current_user["id"]})
    if not result:
        raise HTTPException(status_code=404, detail="Result not found or unaccessible")
        
    result["id"] = str(result["_id"])
    return AnalysisResultResponse(**result)
