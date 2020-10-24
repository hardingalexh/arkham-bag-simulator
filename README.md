# arkham-bag-simulator

## Local Development
### Backend
    * `cd backend`
    * Create virtual environment `python3 -m venv .venv` (only for intial setup)
    * Activate virtual environment `source .venv/bin/activate`
    * Install dependencies `pip install -r requirements.txt` (only for initial setup)
    * navigate to app `cd app`
    * Run dev server `uvicorn main:app --reload` (this makes the backend available at http://localhost:8000)

### Frontend
    * `cd frontend`
    * `yarn install` (only for first-time setup)
    * `yarn serve` (this makes the frontend available at http://localhost:8080)