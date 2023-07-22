import tkinter as tk

class JoystickApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Control")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Create a rectangle representing the robot
        self.robot = self.canvas.create_rectangle(180, 180, 220, 220, fill="blue")

        # Create buttons for joystick control
        self.up_button = tk.Button(root, text="Up", repeatdelay=500, repeatinterval=100, command=lambda: self.start_move("up"))
        self.up_button.pack(side=tk.TOP)
        self.down_button = tk.Button(root, text="Down", repeatdelay=500, repeatinterval=100, command=lambda: self.start_move("down"))
        self.down_button.pack(side=tk.BOTTOM)
        self.left_button = tk.Button(root, text="Left", repeatdelay=500, repeatinterval=100, command=lambda: self.start_move("left"))
        self.left_button.pack(side=tk.LEFT)
        self.right_button = tk.Button(root, text="Right", repeatdelay=500, repeatinterval=100, command=lambda: self.start_move("right"))
        self.right_button.pack(side=tk.RIGHT)

        # Bind button press and release events to start and stop movement
        self.up_button.bind("<ButtonPress-1>", lambda event: self.move_robot("up"))
        self.down_button.bind("<ButtonPress-1>", lambda event: self.move_robot("down"))
        self.left_button.bind("<ButtonPress-1>", lambda event: self.move_robot("left"))
        self.right_button.bind("<ButtonPress-1>", lambda event: self.move_robot("right"))
        self.root.bind("<ButtonRelease-1>", self.stop_move)

        self.current_direction = None

    def start_move(self, direction):
        self.current_direction = direction
        self.move_robot()

    def stop_move(self, event):
        self.current_direction = None

    def move_robot(self):
        if self.current_direction == "up":
            self.canvas.move(self.robot, 0, -10)
        elif self.current_direction == "down":
            self.canvas.move(self.robot, 0, 10)
        elif self.current_direction == "left":
            self.canvas.move(self.robot, -10, 0)
        elif self.current_direction == "right":
            self.canvas.move(self.robot, 10, 0)

        if self.current_direction is not None:
            self.root.after(100, self.move_robot)

if __name__ == "__main__":
    root = tk.Tk()
    app = JoystickApp(root)
    root.mainloop()
