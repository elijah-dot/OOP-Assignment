#Activity 1: Design  Class

class Smartphone:

    def __init__(self, brand, model, battery_life):

        self.brand = brand

        self.model = model

        self.battery_life = battery_life  # in hours


    def display_info(self):

        """Display the smartphone's information."""
        return f"Brand: {self.brand}, Model: {self.model}, Battery Life: {self.battery_life} hours"


    def use_app(self, app_name):

        """Simulate using an app and reduce battery life."""

        if self.battery_life > 0:

            self.battery_life -= 1  # Using an app consumes 1 hour of battery

            return f"Using {app_name}. Battery life left: {self.battery_life} hours."

        else:

            return "Battery is dead! Please charge your smartphone."


# Example of creating a smartphone object

my_phone = Smartphone("Apple", "iPhone 14", 20)

print(my_phone.display_info())
print(my_phone.use_app("Facebook"))

print(my_phone.use_app("Instagram"))


# activity2 Inheritance Layer

class CameraPhone(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        """Simulate taking a photo."""
        if self.battery_life > 0:
            return f"Taking a photo with {self.camera_megapixels} MP camera."
        else:
            return "Battery is dead! Please charge your camera phone."

# Example of creating a camera phone object
my_camera_phone = CameraPhone("Samsung", "Galaxy S21", 18, 108)
print(my_camera_phone.display_info())
print(my_camera_phone.take_photo())
print(my_camera_phone.use_app("Snapchat"))
