from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# CORS setup to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orders = []
order_id_counter = 1
totals = {"burgers": 0, "fries": 0, "drinks": 0}

class UserInput(BaseModel):
    message: str

@app.post("/process")
def process_input(user_input: UserInput):
    global order_id_counter
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input.message}],
        functions=[
            {
                "name": "place_order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "burgers": {"type": "integer"},
                        "fries": {"type": "integer"},
                        "drinks": {"type": "integer"}
                    },
                    "required": []
                }
            },
            {
                "name": "cancel_order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_number": {"type": "integer"}
                    },
                    "required": ["order_number"]
                }
            }
        ]
    )

    action = response.choices[0].message.get("function_call", {})
    if action["name"] == "place_order":
        params = eval(action["arguments"])
        order = {
            "id": order_id_counter,
            "burgers": params.get("burgers", 0),
            "fries": params.get("fries", 0),
            "drinks": params.get("drinks", 0)
        }
        orders.append(order)
        totals["burgers"] += order["burgers"]
        totals["fries"] += order["fries"]
        totals["drinks"] += order["drinks"]
        order_id_counter += 1
        return {"status": "order_placed", "order": order, "totals": totals, "orders": orders}
    
    elif action["name"] == "cancel_order":
        order_number = eval(action["arguments"])["order_number"]
        for order in orders:
            if order["id"] == order_number:
                totals["burgers"] -= order["burgers"]
                totals["fries"] -= order["fries"]
                totals["drinks"] -= order["drinks"]
                orders.remove(order)
                return {"status": "order_cancelled", "order_number": order_number, "totals": totals, "orders": orders}
        raise HTTPException(status_code=404, detail="Order not found")
    
    raise HTTPException(status_code=400, detail="Invalid action")
