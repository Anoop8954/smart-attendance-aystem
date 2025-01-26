import tkinter as tk
from tkinter import messagebox


class LibrarySeatingGUI:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.seats = [["Available" for _ in range(columns)] for _ in range(rows)]
        self.buttons = []

        self.root.title("Library Seating Management System")
        self.create_seating_grid()

    def create_seating_grid(self):
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.columns):
                button = tk.Button(
                    self.root,
                    text=f"Seat {i+1},{j+1}",
                    bg="green",
                    width=10,
                    height=2,
                    command=lambda row=i, col=j: self.toggle_seat(row, col),
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def toggle_seat(self, row, col):
        if self.seats[row][col] == "Available":
            self.seats[row][col] = "Reserved"
            self.buttons[row][col].config(bg="red")
            messagebox.showinfo("Reservation", f"Seat ({row+1}, {col+1}) reserved!")
        elif self.seats[row][col] == "Reserved":
            self.seats[row][col] = "Available"
            self.buttons[row][col].config(bg="green")
            messagebox.showinfo("Cancellation", f"Reservation for Seat ({row+1}, {col+1}) canceled!")

    def run(self):
        self.root.mainloop()


# Initialize the system
def main():
    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))
    root = tk.Tk()
    app = LibrarySeatingGUI(root, rows, columns)
    app.run()


if __name__ == "__main__":
    main()
