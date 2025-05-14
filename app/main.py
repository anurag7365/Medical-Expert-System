from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.model import predict_disease  # Import your model's predict function

# Create FastAPI instance
app = FastAPI()

# Jinja2 templates directory
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Render the home page
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    fever: int = Form(...),
    cough: int = Form(...),
    headache: int = Form(...),
):
    # Get disease prediction result
    result = predict_disease({"fever": fever, "cough": cough, "headache": headache})
    
    # Render predict.html with the prediction result
    return templates.TemplateResponse("predict.html", {"request": request, "disease_prediction": result})
