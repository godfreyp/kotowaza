import customtkinter as ck
import kotowaza as kw
import cache
from random import choice

class App(ck.CTk):

    WIDTH = 900
    HEIGHT = 600
    c = cache.Cache()

    def __init__(self):
        super().__init__()
        self.title = ("Idiom/Expression Chooser")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.onClosing)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = ck.CTkFrame(master=self, width=180, corner_radius=10)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        self.frame_right = ck.CTkFrame(master=self, corner_radius=10)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============
        self.label_1 = ck.CTkLabel(master=self.frame_left,
                                              text="Interface",
                                              text_font=("Arial", -30))
        self.label_1.grid(row=1, column=0, pady=20, padx=10)

        self.button_1 = ck.CTkButton(master=self.frame_left,
                                                text="Generate",
                                                command=self.callSaying)
        self.button_1.grid(row=2, column=0, pady=20, padx=20)

        self.button_2 = ck.CTkButton(master=self.frame_left,
                                                text="Reset",
                                                command=self.resetCache)
        self.button_2.grid(row=3, column=0, pady=20, padx=20)

        self.button_3 = ck.CTkButton(master=self.frame_left,
                                                text="Quit",
                                                command=self.onClosing)
        self.button_2.grid(row=4, column=0, pady=20, padx=20)

        # ============ frame_right ============

        self.label_2 = ck.CTkLabel(master=self.frame_right,
                                              text="",
                                              text_font=("Arial", -40),
                                              wrap=600)
        self.label_2.grid(row=0, column=1, pady=20, padx=10)
        

    def callSaying(self):
        if self.c.getLength() == self.c.getCacheLength():
            self.label_2.configure(text="You're finished! Press reset to start again!")
        else:
            randnum = choice([i for i in range(1, self.c.getLength() + 1) if i not in self.c.getCache()])
            self.c.addValue(randnum)
            idiom = kw.returnSaying(randnum)
            self.label_2.configure(text=idiom)


    def resetCache(self):
        self.label_2.configure(text="Press \"Generate\" to start again")
        self.c.resetCache()

    def onClosing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

