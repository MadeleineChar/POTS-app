import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
from data_manager import DataManager

BG_COLOR = "#F5EFFF"
BTN_COLOR = "#CDC1FF"
BTN_TEXT_COLOR = "#000000"
HEADER_COLOR = "#A594F9"

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("POTS Management App")
        self.root.configure(bg=BG_COLOR)
        self.dataManager = DataManager()
        self.mainMenu()

    def clearFrame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mainMenu(self):
        self.clearFrame()
        tk.Label(self.root, text="💜 POTS Management", bg=BG_COLOR, fg=HEADER_COLOR, font=("Poppins", 18, "bold")).pack(pady=20)
        tk.Label(self.root, text="What would you like to do today?", bg=BG_COLOR, font=("Poppins", 12)).pack(pady=5)

        tk.Button(self.root, text="📝 Track Symptoms\nLog how you're feeling today", command=self.inputSymptom,
                  bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Poppins", 12), width=30, height=3).pack(pady=10)

        tk.Button(self.root, text="💓 Track Heart Rate\nRecord your heart rate reading", command=self.inputHR,
                  bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Poppins", 12), width=30, height=3).pack(pady=10)

        tk.Button(self.root, text="📊 View Graphs\nVisualize your data", command=self.showGraphMenu,
                  bg="#BTN_COLOR", fg="#BTN_TEXT_COLOR", font=("Poppins", 12), width=30, height=3).pack(pady=10)

        tk.Button(self.root, text="🚪 Exit\nClose the app", command=self.root.quit,
                  bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Poppins", 12), width=30, height=3).pack(pady=10)

        tk.Label(self.root, text="Remember: You're doing great by taking care of yourself 💜",
                 bg=BG_COLOR, fg="#555555", font=("Poppins", 10)).pack(pady=20)

    def inputSymptom(self):
        self.clearFrame()
        tk.Label(self.root, text="📝 Track Symptoms", bg=BG_COLOR, fg=HEADER_COLOR, font=("Poppins", 18, "bold")).pack(pady=20)
        tk.Label(self.root, text="Share how you're feeling today", bg=BG_COLOR, font=("Poppins", 12)).pack(pady=5)

        symptom_entry = tk.Text(self.root, height=5, width=40, font=("Poppins", 10))
        symptom_entry.pack(pady=5)

        def saveSymptom():
            symptom = symptom_entry.get("1.0", tk.END).strip()
            if symptom:
                self.dataManager.addSymptom(symptom)
                messagebox.showinfo("Success", "Symptom saved successfully.")
                self.mainMenu()
            else:
                messagebox.showerror("Error", "Symptom cannot be empty.")

        tk.Button(self.root, text="💾 Save Symptom", command=saveSymptom,
                  bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Poppins", 12), width=20, height=2).pack(pady=10)

        tk.Button(self.root, text="🔙 Back", command=self.mainMenu,
                  bg="#E0E0E0", fg="#000000", font=("Poppins", 10), width=10).pack(pady=5)

    def inputHR(self):
        self.clearFrame()
        tk.Label(self.root, text="💓 Track Heart Rate", bg=BG_COLOR, fg=HEADER_COLOR, font=("Poppins", 18, "bold")).pack(pady=20)
        tk.Label(self.root, text="Enter your heart rate (bpm)", bg=BG_COLOR, font=("Poppins", 12)).pack(pady=5)

        hr_entry = tk.Entry(self.root, font=("Poppins", 12))
        hr_entry.pack(pady=5)

        def saveHR():
            hr = hr_entry.get().strip()
            if hr.isdigit():
                self.dataManager.addHR(int(hr))
                messagebox.showinfo("Success", "Heart rate saved successfully.")
                self.mainMenu()
            else:
                messagebox.showerror("Error", "Please enter a numeric value.")

        tk.Button(self.root, text="💾 Save Heart Rate", command=saveHR,
                  bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Poppins", 12), width=20, height=2).pack(pady=10)

        tk.Button(self.root, text="🔙 Back", command=self.mainMenu,
                  bg="#E0E0E0", fg="#000000", font=("Poppins", 10), width=10).pack(pady=5)

    def showGraphMenu(self):
        self.clearFrame()
        tk.Label(self.root, text="📊 View Graphs", bg=BG_COLOR, fg=HEADER_COLOR, font("Poppins",18, "bold")).pack(pady=20)
            tk.Button(self.root, text="💓 Heart Rate Trends", command=self.plotHRGraph, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Poppins", 12), width=25, height=2).pack(pady=10)
            tk.Button(self.root, text="📝 Symptom Frequency", command=self.plotSymptomGraph, bg=BTN_COLOR, fg=BTN_TEXT_COLOR, font=("Poppins", 12), width=25, height=2).pack(pady=10)
            tk.Button(self.root, text="🔙 Back", command=self.mainMenu, bg="#E0E0E0", fg="#000000", font=("Poppins", 10), width=10).pack(pady=20)

    def plotHRGraph(self_:
        dates,hr_values = self.dataManagger.getHRData()
        fig,ax = plt.subplots(figsize=(8, 4))
        ax.plot(dates, hr_values, marker='o', color='A594F9', linewidth=2)
        ax.set_title ("Heart Rate Trends", fontweight='bold')
        ax.set_xlabel("Date")
        ax.set_ylabel("BPM")
        ax.grid(True, linestyle='--', alpha=0.6)

        self.clearFrame()
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)


        

                    
