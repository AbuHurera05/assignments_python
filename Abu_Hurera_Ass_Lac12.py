class Vehicle:
   def __init__(self,brand,model):
      self.brand = brand
      self.model = model
   def show_detail(self):
      return f"Brand: {self.brand} Model: {self.model}"