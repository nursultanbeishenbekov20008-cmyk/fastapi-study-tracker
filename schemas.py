from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# User Schemas
class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Subject Schemas
class SubjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    color: str = "#3498db"

class SubjectCreate(SubjectBase):
    pass

class SubjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None

class Subject(SubjectBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Study Session Schemas
class StudySessionBase(BaseModel):
    subject_id: int
    title: str
    description: Optional[str] = None
    duration_minutes: int
    notes: Optional[str] = None

class StudySessionCreate(StudySessionBase):
    pass

class StudySessionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    duration_minutes: Optional[int] = None
    notes: Optional[str] = None

class StudySession(StudySessionBase):
    id: int
    user_id: int
    date: datetime
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Goal Schemas
class GoalBase(BaseModel):
    subject_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    target_hours: float
    deadline: Optional[datetime] = None

class GoalCreate(GoalBase):
    pass

class GoalUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    target_hours: Optional[float] = None
    completed_hours: Optional[float] = None
    is_completed: Optional[bool] = None
    deadline: Optional[datetime] = None

class Goal(GoalBase):
    id: int
    user_id: int
    completed_hours: float
    is_completed: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True