from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()


products=[
              {"id":1,"name": "shoes", "description": "black", "price": 300, "image": "shoe_image"},
              {"id":2, "name": "T shirt", "description": "pink", "price": 350, "image": "T shirt_image"},
              {"id":3, "name": "jewelry", "description": "gold", "price": 1500, "image": "jewelry_image"},
              {"id":4, "name": "hair bonnet", "description": "white", "price": 50, "image": "hair bonnet_image"}
              ]

class Products(BaseModel):
   name:str
   description:str
   price:float
   image:str
  
   

class User(BaseModel):
    userid: int
    username: str
    email: str
    password: str

users = []

class Log_in_data(BaseModel):
    email: str
    password: str

class CartItem(BaseModel):
   user_id:int
   cart_id: int
   product_id: int
   quantity: int



# 1
@app.get("/")
def get_home():
  return{"Message": "Akwaaba! Welcome to our E-commerce Api"}

#2  list of sample products
@app.get("/products")
def get_products():
    return{"products":products}

#GET a single product by using id to search 
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
     if product["id"] == product_id:
       return{"product": product}
    raise HTTPException(status_code=404, detail="Product not found")


@app.patch("/products/{product_id}")
def update_product(product_id: int, products:Products):
  update = get_product_by_id(product_id)
  update_dict = update["product"]
  update_dict.update(products.model_dump())
  return {"message": "product updated", "product": products}



#3 Users (Basic Auth Simulation)
# create a list to store users (id, username, email, password)

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
@app.post("/login")
def login(data: Log_in_data):
    for user in users:
        if user["email"] == data.email and user["password"] == data.password:
            return {"message": "Login successful", 
                    "username": user["username"]}
    raise HTTPException(status_code=401, detail="Invalid credentials")   


# 4 Cart 
#Use a dictionary to simulate cart

@app.post("/cart")
def add_to_cart(cart: CartItem):
   cart = []
   get_product_by_id(cart.item.product_id)
   cart.append(cart.model_dump())
   return{"message": "Product added successfully", "cart": cart}
   
   

   
