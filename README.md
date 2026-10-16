# carbon_intelligence_platform
An advanced, AI-powered platform for tracking, predicting, and optimizing carbon emissions across organizations and supply chains. Built to empower businesses to make data-driven sustainability decisions.
🌟 Features
Comprehensive Emissions Tracking: Aggregate and visualize Scope 1, 2, and 3 emissions through an intuitive dashboard.
AI-Powered Recommendations: Receive automated, machine-learning-driven suggestions to reduce carbon footprints.
Simulation Engine: Test the impact of sustainability initiatives (like switching to renewable energy) before implementing them.
Supply Chain Digital Twin: An interactive 3D visualization of your supply chain network to identify emission hotspots.
Automated Reporting & Compliance: Generate in-depth EDA and prediction reports (CSV/PDF) instantly.
💻 Tech Stack
Frontend:

React 18 + Vite
Tailwind CSS
Three.js & React Three Fiber (for Digital Twin 3D visualizations)
Recharts (for analytics dashboards)
Backend:

FastAPI (Python)
MongoDB (Database)
Pandas, Scikit-Learn, XGBoost (Machine Learning models for predictions and simulations)
🚀 Getting Started
You can run the entire platform easily using Docker.

Prerequisites
Docker & Docker Compose
MongoDB (or you can use a cloud Atlas URI in your .env)
1. Clone the repository
git clone https://github.com/vipulofficial206/carbon-intelligence-platform.git
cd carbon-intelligence-platform
2. Environment Variables
Create a .env file in the backend/ directory:

MONGO_URI=mongodb://mongo:27017/carbon_db
SECRET_KEY=your_secret_key_here
3. Run with Docker Compose
docker-compose up --build
The application will be available at:

Frontend: http://localhost:3000
Backend API: http://localhost:8000
API Docs (Swagger): http://localhost:8000/docs
🛠️ Manual Development Setup
If you prefer to run the servers manually without Docker:

Backend:

cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Frontend:

cd frontend_new
npm install
npm run dev
📄 License
This project is licensed under the MIT License.
