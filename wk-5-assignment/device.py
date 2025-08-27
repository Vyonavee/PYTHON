# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"Device: {self.brand} {self.model}"

# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage  
        self.battery = battery  
    
    # Method to display smartphone details
    def phone_info(self):
        return f"{self.device_info()}, Storage: {self.storage}GB, Battery: {self.battery}mAh"
    
    # Method to simulate charging
    def charge(self, amount):
        self.battery += amount
        return f"{self.model} charged! New battery level: {self.battery}mAh"
    
    # Method to install an app
    def install_app(self, app_name, size):
        if size <= self.storage:
            self.storage -= size
            return f"Installed {app_name}. Remaining storage: {self.storage}GB"
        else:
            return f"Not enough storage to install {app_name}!"

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 4000)
phone2 = Smartphone("Apple", "iPhone 13", 256, 3500)

print(phone1.phone_info())
print(phone1.install_app("WhatsApp", 2))
print(phone1.charge(500))

print(phone2.phone_info())
print(phone2.install_app("Call Of Duty", 300))  # This one is too big
