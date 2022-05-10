class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print("Restaurant Name: ", self.restaurant_name)
        print("Cuisine Type: ", self.cuisine_type)
    
    def open_restaurant(self):
        print("The restaurant is open!")
    
    def total_number_served(self):
        print("Number Served: ", self.number_served)
        
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served+=number