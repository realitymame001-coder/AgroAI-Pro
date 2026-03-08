# AgroAI Pro 🌾

AI-powered crop disease detection platform with:
- AI model training (PyTorch)
- FastAPI backend
- React frontend
- Android app (Camera + optional on-device model)
- Agricultural knowledge base (crops, diseases, treatments)

## Quick Start

### Backend
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload

### AI Model
cd ai-model
pip install -r requirements.txt
python train.py

### Frontend
cd frontend
npm install
npm run dev

### Docker
docker build -t agroai ./deployment
docker run -p 8000:8000 agroai
