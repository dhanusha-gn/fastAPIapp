from fastapi import APIRouter, HTTPException, Depends, status
from schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse
from models import company, job
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/company", tags=["company"])

companies = []

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CompanyResponse
)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    companies.append(company)
    return company


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[CompanyResponse]
)
def get_all_company(db: Session = Depends(get_db)):
    return companies


@router.get(
    "/{company_id}",
    status_code=status.HTTP_200_OK,
    response_model=CompanyResponse
)
def get_company(company_id: int):
    if company_id >= len(companies):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )
    return companies[company_id]


@router.put(
    "/{company_id}",
    status_code=status.HTTP_200_OK,
    response_model=CompanyResponse
)
def update_company(company_id: int, company: CompanyUpdate):
    if company_id >= len(companies):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )

    companies[company_id] = company
    return companies[company_id]


@router.delete(
    "/{company_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_company(company_id: int):
    if company_id >= len(companies):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company not found"
        )

    companies.pop(company_id)
    return {"message": "Company deleted successfully"}