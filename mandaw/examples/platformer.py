from mandaw import *

# Window
mandaw = Mandaw("Platformer", bg_color = "cyan")

# Ground
ground = GameObject(mandaw, "rect", 1000, 100, mandaw.width / 2 - 500, 500, "gray")

objects = []

# Player
class PlatformerController(GameObject):
    def __init__(self):
        super().__init__(
            mandaw,
            "rect",
            30,
            70,
            mandaw.width / 2 - 15,
            mandaw.height / 2 - 35,
            "orange",
        )
        
        # Player Speed
        self.speed = 3
        # Set the position as a variable
        self.pos = mandaw.width / 2 - self.width

    def movement(self):
        # Player movement
        if mandaw.controls.is_key_pressed(mandaw.keys["A"]):
            self.pos -= 1 * self.speed
        if mandaw.controls.is_key_pressed(mandaw.keys["D"]):
            self.pos += 1 * self.speed

        # Gravity
        if not self.collidelistall(objects):
            self.y += 3

        # Set the x position as the x variable
        self.x = self.pos

    def jump(self):
        # Jumping
        if self.collidelistall(objects):
            self.y -= 100

class Platform(GameObject):
    def __init__(self, x, y):
        super().__init__(
            mandaw,
            "rect",
            100,
            20,
            x,
            y,
            "green"
        )

# Call the player
player = PlatformerController()

platform = Platform(mandaw.width / 2 - 200, mandaw.height / 2 + 150)
platform1 = Platform(mandaw.width / 2 - 300, mandaw.height / 2 + 80)
platform2 = Platform(mandaw.width / 2 - 400, mandaw.height / 2 + 10)
platform3 = Platform(mandaw.width / 2 - 300, mandaw.height / 2 - 60)
platform4 = Platform(mandaw.width / 2 - 200, mandaw.height / 2 - 130)
platform5 = Platform(mandaw.width / 2 - 100, mandaw.height / 2 - 200)
platform6 = Platform(mandaw.width / 2 + 100, mandaw.height / 2 - 200)
platform7 = Platform(mandaw.width / 2 + 300, mandaw.height / 2 - 200)

objects.append(ground)
objects.append(platform)
objects.append(platform1)
objects.append(platform2)
objects.append(platform3)
objects.append(platform4)
objects.append(platform5)
objects.append(platform6)
objects.append(platform7)


# Main Game Loop
while True:
    # Call the player functions
    player.movement()

    if mandaw.controls.is_key_pressed(mandaw.keys["SPACE"]):
        player.jump()

    # Draw the ground and player
    ground.draw()
    player.draw()
    platform.draw()
    platform1.draw()
    platform2.draw()
    platform3.draw()
    platform4.draw()
    platform5.draw()
    platform6.draw()
    platform7.draw()

    # Run the program
    mandaw.run()
