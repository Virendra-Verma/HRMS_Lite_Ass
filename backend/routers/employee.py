from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Optional, List
import time
from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from database import get_db
from models import Employee 

router = APIRouter(prefix="/employees", tags=["Employees"])

# --- Schema ---
class EmployeeCreate(BaseModel):
    fullName: str = Field(..., alias="name")
    employeeId: Optional[str] = None 
    email: EmailStr
    department: str
    
    @model_validator(mode='before')
    @classmethod
    def handle_mapping(cls, data):
        if isinstance(data, dict):
            if 'name' in data and 'fullName' not in data:
                data['fullName'] = data.get('name')
            if not data.get('employeeId'):
                data['employeeId'] = f"EMP-{int(time.time() * 1000)}"
        return data
    
    class Config:
        populate_by_name = True

# --- POST Route ---
@router.post("", status_code=status.HTTP_201_CREATED)
@router.post("/", include_in_schema=False)
def create_employee(emp_in: EmployeeCreate, db: Session = Depends(get_db)):
    existing = db.query(Employee).filter(
        or_(Employee.email == emp_in.email, Employee.employee_id == emp_in.employeeId)
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Employee ID or Email already exists")

    new_emp = Employee(
        employee_id=emp_in.employeeId,
        full_name=emp_in.fullName,
        email=emp_in.email,
        department=emp_in.department
    )
    
    try:
        db.add(new_emp)
        db.commit()
        db.refresh(new_emp)
        return {"success": True, "data": new_emp}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# --- GET All Employees (MAPPING FIXED HERE) ---
@router.get("")
@router.get("/", include_in_schema=False)
def get_all_employees(db: Session = Depends(get_db), page: int = 1, limit: int = 10):
    query = db.query(Employee).filter(Employee.deleted_at == None)
    total = query.count()
    employees = query.order_by(Employee.created_at.desc()).offset((page-1)*limit).limit(limit).all()
    
    # FRONTEND FIX: Backend 'full_name' bhej raha tha, frontend 'name' dhoond raha tha.
    # Hum yahan frontend ki language (name, joining_date) mein data bhejenge.
    formatted_data = []
    for emp in employees:
        formatted_data.append({
            "id": emp.id,
            "employee_id": emp.employee_id,
            "name": emp.full_name,        # <--- frontend ko yahi chahiye
            "email": emp.email,
            "department": emp.department,
            "joining_date": emp.created_at, # <--- "Invalid Date" solve ho jayega
            "status": "Active"
        })

    return {
        "success": True, 
        "total": total, 
        "data": formatted_data
    }

# --- Stats Route ---
@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(Employee).count()
    return {"success": True, "data": {"totalEmployees": total}}