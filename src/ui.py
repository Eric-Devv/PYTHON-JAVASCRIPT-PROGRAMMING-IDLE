import os
import subprocess
import customtkinter as ctk
from tkinter import simpledialog, messagebox, filedialog, Menu
import requests  

class IDEApp:
    def __init__(self, master):
        self.master = master
        master.title("Python & JavaScript IDE")
        master.geometry('900x600')
        ctk.set_appearance_mode("dark")   

        # Create a menu bar
        self.menu_bar = Menu(master, bg="#2E2E2E", fg="white")
        master.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0, bg="#2E2E2E", fg="white")
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New Project", command=self.new_project)
        self.file_menu.add_command(label="Open File", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file_dialog)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.pack(fill='both', expand=True)

        # Button frame for vertical button layout
        self.button_frame = ctk.CTkFrame(self.main_frame)
        self.button_frame.pack(side='left', fill='y')

        # Buttons for various actions
        self.run_button = ctk.CTkButton(self.button_frame, text="Run", command=self.run_code)
        self.run_button.pack(side='top', padx=5, pady=5)

        self.debug_button = ctk.CTkButton(self.button_frame, text="Debug", command=self.debug_code)
        self.debug_button.pack(side='top', padx=5, pady=5)

        self.ai_button = ctk.CTkButton(self.button_frame, text="Ask AI", command=self.ask_ai_window)
        self.ai_button.pack(side='top', padx=5, pady=5)

        self.save_button = ctk.CTkButton(self.button_frame, text="Save", command=self.save_file_dialog)
        self.save_button.pack(side='top', padx=5, pady=5)

        self.format_button = ctk.CTkButton(self.button_frame, text="Format", command=self.format_code)
        self.format_button.pack(side='top', padx=5, pady=5)

        self.launch_terminal_button = ctk.CTkButton(self.button_frame, text="Launch Terminal", command=self.launch_terminal)
        self.launch_terminal_button.pack(side='top', padx=5, pady=5)

        # Frame for code input
        self.code_frame = ctk.CTkFrame(self.main_frame)
        self.code_frame.pack(side='right', fill='both', expand=True)

        # Text area for code input
        self.text_area = ctk.CTkTextbox(self.code_frame, 
                                         fg_color="black",  # Background color
                                         text_color="white",  # Text color
                                         border_color="grey",  # Border color
                                         border_width=1,  # Border width
                                         corner_radius=5)  # Corner radius for rounded corners
        self.text_area.pack(side='top', fill='both', expand=True)

    def new_project(self):
        """Clear the text area for a new project."""
        self.text_area.delete("1.0", ctk.END)  

    def open_file(self):
        """Open a file dialog to load code from a file."""
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py"), ("JavaScript files", "*.js"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
                self.text_area.delete("1.0", ctk.END)
                self.text_area.insert("1.0", code)  

    def save_file_dialog(self):
        """Open a file dialog to save the code to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py"), ("JavaScript files", "*.js"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", ctk.END))  # Save text from the text area

    def run_code(self):
        """Run the code written in the text area."""
        code = self.text_area.get("1.0", ctk.END).strip()  # Get the entire code
        output = self.execute_code(code)
        messagebox.showinfo("Run Output", output)  # Display output in a message box

    def debug_code(self):
        """Placeholder for debugging code."""
        messagebox.showinfo("Debugging", "Debugging feature not implemented yet.")

    def ask_ai_window(self):
        """Ask a question to the AI."""
        question = simpledialog.askstring("Ask AI", "What do you want to ask?")
        if question:
            response = self.get_ai_response(question)
            self.display_ai_response(response)

    def get_ai_response(self, question):
        """Get a response from the AI based on the question."""
        api_key = "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."  
        api_url = "https://api.openai.com/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": question}]
        }
        
        try:
            response = requests.post(api_url, headers=headers, json=data)
            response.raise_for_status()  
            return response.json()['choices'][0]['message']['content']
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to get AI response: {e}")
            return "Error retrieving response"

    def display_ai_response(self, response):
        """Display the AI response in a new window."""
        response_window = ctk.CTkToplevel(self.master)
        response_window.title("AI Response")
        response_label = ctk.CTkLabel(response_window, text=response)
        response_label.pack(padx=10, pady=10)

    def format_code(self):
        """Placeholder for formatting code."""
        messagebox.showinfo("Format Code", "Code formatting feature not implemented yet.")

    def launch_terminal(self):
        """Launch a terminal window."""
        self.terminal_window = ctk.CTkToplevel(self.master)  # Create a new window
        self.terminal_window.title("Terminal")
        self.terminal_window.geometry("600x400")  

        self.terminal_text = ctk.CTkTextbox(self.terminal_window, fg_color="black")
        self.terminal_text.pack(fill='both', expand=True)

        # Command entry
        self.command_entry = ctk.CTkEntry(self.terminal_window)
        self.command_entry.pack(fill='x', padx=10, pady=5)
        self.command_entry.bind('<Return>', self.execute_command)

        self.terminal_text.insert("end", "Welcome to the terminal!\n")

    def execute_command(self, event):
        """Execute a command entered in the terminal."""
        command = self.command_entry.get()
        self.command_entry.delete(0, 'end')  # Clear the entry box
        self.terminal_text.insert("end", f"> {command}\n")  # Display command

        # Execute the command and get the output
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.terminal_text.insert("end", output + "\n")  # Display output
        except subprocess.CalledProcessError as e:
            self.terminal_text.insert("end", f"Error: {e.output}\n")  # Display error output


if __name__ == "__main__":
    root = ctk.CTk()
    app = IDEApp(root)
    root.mainloop()
