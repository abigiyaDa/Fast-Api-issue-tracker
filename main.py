from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.middleware("http")(timing_middleware)
# here we are adding the cors middleware to allow cross origin requests from any origin, with any method and any header. 
# This is useful for development purposes, but in production you should restrict the origins, methods and headers that are allowed to access your API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(issues_router)



















# items = [
#     {"id": 1, "name": "Item 1"},
#     {"id": 2, "name": "Item 2"},    
#     {"id": 3, "name": "Item 3"}
# ]

# @app.get("/health")
# def health_check():
#     return {"status": "ok"}

# # a route that fetches all items and displays them 
# @app.get("/items")
# def get_items():
#     return items

# # get a specific item by id
# @app.get("/items/{item_id}")   
# def get_item(item_id: int):
#     for item in items:
#         if item["id"] == item_id:
#             return item
#     return {"error": "Item not found"}

# # post request 

# @app.post("/items")
# def create_item(item: dict):
#     items.append(item)
#     return item