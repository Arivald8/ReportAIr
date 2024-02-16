import customtkinter
import tkinter

customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    WIDTH = 1100
    HEIGHT = 600
    LEFT_SIDE_WIDTH = 150
    RIGHT_SIDE_WIDTH = 100
    MID_WIDTH = 200
    PADX = 10
    PADY = 10

    def __init__(self):
        super().__init__()

        # Window conf
        self.title("ReportAIr")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Layout conf
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=4)
        
        self.grid_rowconfigure(0, weight=0)
        
        # Left sidebar frame
        self.l_frame = customtkinter.CTkFrame(self, width=self.LEFT_SIDE_WIDTH, height=self.HEIGHT, border_color="Gray", border_width=2)
        self.l_frame.grid(row=0, column=0, sticky="nsew")

        # Left sidebar buttons
        self.l_frame_btn1 = customtkinter.CTkOptionMenu(self.l_frame, values=["Select Student"])
        self.l_frame_btn1.grid(row=0, column=0, padx=self.PADX, pady=(30, 10))

        self.l_frame_btn2 = customtkinter.CTkButton(self.l_frame, text="Add Student")
        self.l_frame_btn2.grid(row=1, column=0, padx=self.PADX, pady=self.PADY)

        self.l_frame_btn3 = customtkinter.CTkButton(self.l_frame, text="Remove Student")
        self.l_frame_btn3.grid(row=2, column=0, padx=self.PADX, pady=self.PADY)

        self.l_frame_btn4 = customtkinter.CTkButton(self.l_frame, text="Generate Report")
        self.l_frame_btn4.grid(row=3, column=0, padx=self.PADX, pady=(30, 10))

        self.l_frame_btn5 = customtkinter.CTkButton(self.l_frame, text="Save Report")
        self.l_frame_btn5.grid(row=4, column=0, padx=self.PADX, pady=self.PADY)

        self.l_frame_btn6 = customtkinter.CTkButton(self.l_frame, text="Export Report")
        self.l_frame_btn6.grid(row=5, column=0, padx=self.PADX, pady=self.PADY)

        self.l_frame_btn7 = customtkinter.CTkButton(self.l_frame, text="Report Settings")
        self.l_frame_btn7.grid(row=6, column=0, padx=self.PADX, pady=self.PADY)

        self.l_frame_btn8 = customtkinter.CTkButton(self.l_frame, text="Generate Target")
        self.l_frame_btn8.grid(row=7, column=0, padx=self.PADX, pady=(30, 10))

        self.l_frame_btn9 = customtkinter.CTkButton(self.l_frame, text="Save Target")
        self.l_frame_btn9.grid(row=8, column=0, padx=self.PADX, pady=self.PADY)

        self.l_frame_btn10 = customtkinter.CTkButton(self.l_frame, text="Export Target")
        self.l_frame_btn10.grid(row=9, column=0, padx=self.PADX, pady=self.PADY)

        self.l_frame_btn11 = customtkinter.CTkButton(self.l_frame, text="Target Settings")
        self.l_frame_btn11.grid(row=10, column=0, padx=self.PADX, pady=self.PADY)


        # Right sidebar frame
        self.r_frame = customtkinter.CTkFrame(self, width=self.RIGHT_SIDE_WIDTH, height=self.HEIGHT, border_color="Gray", border_width=2)
        self.r_frame.grid(row=0, column=2, sticky="nsew")

        # Right sidebar info
        self.r_frame_label = customtkinter.CTkLabel(self.r_frame, text="Report Card")
        self.r_frame_label.grid(row=0, column=2)
        self.r_frame_label.place(relx=0.5, rely=0.02, anchor=tkinter.N)


        # Mid Frame
        self.m_frame = customtkinter.CTkFrame(self, width=self.MID_WIDTH, height=self.HEIGHT)
        self.m_frame.grid(row=0, column=1, sticky="nsew")
        
        self.mid_btn1_label = customtkinter.CTkLabel(self.m_frame, text="1.", padx=self.PADX)
        self.mid_btn1_label.grid(row=0, column=1, pady=(30, 0))
        self.mid_btn1 = customtkinter.CTkOptionMenu(self.m_frame, values=[""])
        self.mid_btn1.grid(row=0, column=2, padx=self.PADX, pady=(30, 0))
        self.mid_btn1_custom = customtkinter.CTkEntry(self.m_frame, placeholder_text="Custom Notes", width=340)
        self.mid_btn1_custom.grid(row=0, column=3, padx=self.PADX, pady=(30, 0))

        self.mid_btn2_label = customtkinter.CTkLabel(self.m_frame, text="2.")
        self.mid_btn2_label.grid(row=1, column=1, pady=(30, 0))
        self.mid_btn2 = customtkinter.CTkOptionMenu(self.m_frame, values=[""])
        self.mid_btn2.grid(row=1, column=2, padx=self.PADX, pady=(30, 0))
        self.mid_btn2_custom = customtkinter.CTkEntry(self.m_frame, placeholder_text="Custom Notes", width=340)
        self.mid_btn2_custom.grid(row=1, column=3, padx=self.PADX, pady=(30, 0))

        self.mid_btn3_label = customtkinter.CTkLabel(self.m_frame, text="3.")
        self.mid_btn3_label.grid(row=2, column=1, pady=(30, 0))
        self.mid_btn3 = customtkinter.CTkOptionMenu(self.m_frame, values=[""])
        self.mid_btn3.grid(row=2, column=2, padx=self.PADX, pady=(30, 0))
        self.mid_btn3_custom = customtkinter.CTkEntry(self.m_frame, placeholder_text="Custom Notes", width=340)
        self.mid_btn3_custom.grid(row=2, column=3, padx=self.PADX, pady=(30, 0))

        self.mid_btn4_label = customtkinter.CTkLabel(self.m_frame, text="4.")
        self.mid_btn4_label.grid(row=3, column=1, pady=(30, 0))
        self.mid_btn4 = customtkinter.CTkOptionMenu(self.m_frame, values=[""])
        self.mid_btn4.grid(row=3, column=2, padx=self.PADX, pady=(30, 0))
        self.mid_btn4_custom = customtkinter.CTkEntry(self.m_frame, placeholder_text="Custom Notes", width=340)
        self.mid_btn4_custom.grid(row=3, column=3, padx=self.PADX, pady=(30, 0))

        self.mid_btn5_label = customtkinter.CTkLabel(self.m_frame, text="5.")
        self.mid_btn5_label.grid(row=4, column=1, pady=(30, 0))
        self.mid_btn5 = customtkinter.CTkOptionMenu(self.m_frame, values=[""])
        self.mid_btn5.grid(row=4, column=2, padx=self.PADX, pady=(30, 0))
        self.mid_btn5_custom = customtkinter.CTkEntry(self.m_frame, placeholder_text="Custom Notes", width=340)
        self.mid_btn5_custom.grid(row=4, column=3, padx=self.PADX, pady=(30, 0))

        self.mid_btn6_label = customtkinter.CTkLabel(self.m_frame, text="6.")
        self.mid_btn6_label.grid(row=5, column=1, pady=(30, 0))
        self.mid_btn6 = customtkinter.CTkOptionMenu(self.m_frame, values=[""])
        self.mid_btn6.grid(row=5, column=2, padx=self.PADX, pady=(30, 0))
        self.mid_btn6_custom = customtkinter.CTkEntry(self.m_frame, placeholder_text="Custom Notes", width=340)
        self.mid_btn6_custom.grid(row=5, column=3, padx=self.PADX, pady=(30, 0))

        self.mid_btn7_label = customtkinter.CTkLabel(self.m_frame, text="7.")
        self.mid_btn7_label.grid(row=6, column=1, pady=(30, 0))
        self.mid_btn7 = customtkinter.CTkOptionMenu(self.m_frame, values=[""])
        self.mid_btn7.grid(row=6, column=2, padx=self.PADX, pady=(30, 0))
        self.mid_btn7_custom = customtkinter.CTkEntry(self.m_frame, placeholder_text="Custom Notes", width=340)
        self.mid_btn7_custom.grid(row=6, column=3, padx=self.PADX, pady=(30, 0))

        self.mid_btn8_label = customtkinter.CTkLabel(self.m_frame, text="8.")
        self.mid_btn8_label.grid(row=7, column=1, pady=(30, 0))
        self.mid_btn8 = customtkinter.CTkOptionMenu(self.m_frame, values=[""])
        self.mid_btn8.grid(row=7, column=2, padx=self.PADX, pady=(30, 0))
        self.mid_btn8_custom = customtkinter.CTkEntry(self.m_frame, placeholder_text="Custom Notes", width=340)
        self.mid_btn8_custom.grid(row=7, column=3, padx=self.PADX, pady=(30, 0))

        self.mid_btn_set = customtkinter.CTkButton(self.m_frame, text="Set", command=self.mid_btn_set_callback)
        self.mid_btn_set.grid(row=8, column=2, padx=self.PADX, pady=(30, 0))


    def mid_btn_set_callback(self):
        window = SetBtnWindow()
        window.attributes("-topmost", True)



class SetBtnWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()

        # Window conf
        self.title("ReportAIr")
        self.geometry(f"{500}x{500}")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)

        self.grid_rowconfigure(0, weight=0)

        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.grid(row=0, column=0)

        self.btn1_label = customtkinter.CTkLabel(self.main_frame, text="1.")
        self.btn1_label.grid(row=0, column=0, padx=10, pady=10)

        self.set_btn1_label = customtkinter.CTkEntry(self.main_frame, placeholder_text="Set Label Name")
        self.set_btn1_label.grid(row=0, column=1)
        







if __name__ == "__main__":
    app = App()
    app.mainloop()