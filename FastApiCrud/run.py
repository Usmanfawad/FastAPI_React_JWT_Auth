import uvicorn


if __name__ == "__main__":
    #The backend fastAPI will serve on port 8000
    
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)