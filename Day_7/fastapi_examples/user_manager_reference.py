from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, Field
from typing import Optional
import secrets

from userdb_mariadb import *  
from userdb_generic import UserDB

# Initialize FastAPI app
app = FastAPI(
    title="User Management API",
    description="API for managing users with authentication",
    version="1.0.0"
)

# Security
security = HTTPBasic()

# Pydantic models for request/response validation
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username must be 3-50 characters")
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")
    fullname: str = Field(..., min_length=1, max_length=100, description="Full name")

class UserUpdate(BaseModel):
    password: Optional[str] = Field(None, min_length=6, description="New password")
    fullname: Optional[str] = Field(None, min_length=1, max_length=100, description="New full name")

class UserResponse(BaseModel):
    username: str
    fullname: str
    message: str

class UserAuthenticated(BaseModel):
    username: str
    fullname: str
    authenticated: bool

# Dependency to get database connection
def get_db():
    """Dependency to get database connection"""
    db = UserDB()
    try:
        db.connect()
        yield db
    finally:
        db.close()

# Authentication dependency
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security), db: UserDB = Depends(get_db)):
    """Authenticate user using HTTP Basic Auth"""
    is_authenticated = db.authenticate(credentials.username, credentials.password)
    if not is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Optional: Create table on startup
@app.on_event("startup")
async def startup_event():
    """Create user table if it doesn't exist"""
    with UserDB() as db:
        db.create_table()
        print("Database table initialized")

# API Endpoints

@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: UserDB = Depends(get_db)):
    """
    Create a new user
    
    - **username**: Unique username (3-50 characters)
    - **password**: Password (minimum 6 characters)
    - **fullname**: User's full name
    """
    try:
        db.add(user.username, user.password, user.fullname)
        return UserResponse(
            username=user.username,
            fullname=user.fullname,
            message="User created successfully"
        )
    except Exception as e:
        # Handle duplicate username or other database errors
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating user: {str(e)}"
        )

@app.get("/users/me", response_model=UserAuthenticated)
async def get_current_user(
    username: str = Depends(authenticate_user),
    db: UserDB = Depends(get_db)
):
    """
    Get information about the currently authenticated user
    """
    # You might want to fetch full user details here
    # For now, we'll return basic info
    return UserAuthenticated(
        username=username,
        fullname="",  # You would fetch this from database
        authenticated=True
    )

@app.put("/users/{username}", response_model=UserResponse)
async def update_user(
    username: str,
    user_update: UserUpdate,
    current_user: str = Depends(authenticate_user),
    db: UserDB = Depends(get_db)
):
    """
    Update user information
    
    - Users can only update their own information
    - Provide at least one field to update (password or fullname)
    """
    # Check if user is updating their own information
    if current_user != username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own information"
        )
    
    try:
        db.modify(
            username,
            password=user_update.password,
            fullname=user_update.fullname
        )
        return UserResponse(
            username=username,
            fullname=user_update.fullname or "Updated",
            message="User updated successfully"
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error updating user: {str(e)}"
        )

@app.delete("/users/{username}", response_model=UserResponse)
async def delete_user(
    username: str,
    current_user: str = Depends(authenticate_user),
    db: UserDB = Depends(get_db)
):
    """
    Delete a user
    
    - Users can only delete their own account
    """
    # Check if user is deleting their own information
    if current_user != username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own account"
        )
    
    try:
        db.delete(username)
        return UserResponse(
            username=username,
            fullname="",
            message="User deleted successfully"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error deleting user: {str(e)}"
        )

@app.post("/auth/login")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Authenticate user and return success message
    This endpoint uses the same authentication as other protected endpoints
    """
    # The authenticate_user dependency handles the actual authentication
    # If we get here, authentication was successful
    return {
        "message": "Authentication successful",
        "username": credentials.username
    }

@app.get("/users/check-username/{username}")
async def check_username_availability(
    username: str,
    db: UserDB = Depends(get_db)
):
    """
    Check if a username is available
    This endpoint doesn't require authentication
    """
    try:
        # You would need to add this method to your UserDB class
        # For now, we'll assume we can query the database
        db.cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
        count = db.cursor.fetchone()[0]
        return {
            "username": username,
            "available": count == 0
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error checking username: {str(e)}"
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """Check if the API is running"""
    return {"status": "healthy", "message": "User Management API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)