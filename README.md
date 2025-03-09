# 🚗 Drive-Thru Ordering System (Svelte + FastAPI + OpenAI)


https://github.com/user-attachments/assets/ea2e34d5-6897-439d-a6e3-24a9670a7138


This is a **mock drive-thru ordering system** built with:
- **Frontend:** Svelte + Vite
- **Backend:** FastAPI (Python)
- **AI Integration:** OpenAI's GPT to process order requests

## ✨ Features:
- Users can place orders with natural language (e.g., `"I would like two burgers and a drink"`).
- Users can cancel an order by specifying the order number (e.g., `"Cancel order #2"`).
- Orders update dynamically in the UI with total item counts.

---

## 🛠 Installation Instructions

### 🔹 1️⃣ Clone the repository:
```bash
git clone https://github.com/yourusername/drive-thru-ordering.git
cd drive-thru-ordering
```
🔹 2️⃣ Navigate to the backend/ folder:
cd backend

🔹 3️⃣ Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

🔹 4️⃣ Install dependencies:
pip install -r requirements.txt

🔹 5️⃣ Set up the .env file:
OPENAI_API_KEY=your_openai_api_key_here

🔹 6️⃣ Run the backend server:
uvicorn main:app --reload --port 8000

🔹 7️⃣ Navigate to the frontend/ folder:
cd ../frontend

🔹 8️⃣ Install frontend dependencies:
npm install
🔹 9️⃣ Run the frontend dev server:
npm run dev
