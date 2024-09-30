import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import customtkinter as ctk
from src.ui import IDEApp

if __name__ == "__main__":
    root = ctk.CTk()
    app = IDEApp(root)
    root.mainloop()
