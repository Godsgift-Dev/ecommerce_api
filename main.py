from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 1
@app.get("/")
def get_home():
  return{"Message": "Akwaaba! Welcome to our E-commerce Api"}

#2  list of sample products
@app.get("/products")
def get_products():
    products=[
              {"id":1,"name": "shoes", "description": "black", "price": 300, "image": "shoe_image"},
              {"id":2, "name": "T shirt", "description": "pink", "price": 350, "image": "T shirt_image"},
              {"id":3, "name": "jewelry", "description": "gold", "price": 1500, "image": "jewelry_image"},
              {"id":4, "name": "hair bonnet", "description": "white", "price": 50, "image": "hair bonnet_image"}
              ]
    return{"products":products}

#GET a single product by using id to search 
@app.get("/products/{product_id}")
def get_product(product_id: int):
    products = [
         {"id": 1, "name": "shoes", "description": "black", "price": 300 ,"image": "shoe_image"}, 
         { "id": 2,"name": "T shirt", "description": "pink", "price": 350,"image": "T shirt_image"},
         {"id": 3, "name": "Jewelry", "description": "gold", "price": 1500, "image": "jewelry_image"},
         {"id": 4, "name": "hair bonnet", "description": "white", "price": 50, "image": "hair bonnet_image"}
             ]
    for product in products:
     if product["id"] == product_id:
       return{"product": product}
    raise HTTPException(status_code=404, detail="Product not found")
     

#3 Users (Basic Auth Simulation)
# create a list to store users (id, username, email, password)

class User(BaseModel):
    userid: int
    username: str
    email: str
    password: str

users = []

@app.post("/register")
def register(user: User):
# simple check if email already exists
    for u in users:
        if u["email"] == user.email:
          raise HTTPException(status_code=400, detail="You are already registered")
# If email is not found, add the user
    users.append(user.model_dump())
    return {"message": "You are registered successfully", "user": user}

# login 

class Log_in_data(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(data: Log_in_data):
    for user in users:
        if user["email"] == data.email and user["password"] == data.password:
            return {"message": "Login successful", 
                    "username": user["username"]}
    raise HTTPException(status_code=401, detail="Invalid credentials")   



# 4 Cart 

#class CartItem(BaseModel):
#  product_id: int
 # quantity: int
#Use a dictionary to simulate cart
#carts = {}

#@app.post("/cart/{user_id}")
#def add_to_cart(user_id: int, item: CartItem):
   
   

   
