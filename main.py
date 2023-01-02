import tkinter as tk
import os

def main():
    pass
    class Window_master:
        raiz = tk.Tk()

        carpeta_principal = os.path.dirname(__file__)

        carpeta_imagenes = os.path.join(carpeta_principal, "images")

        wtotal = raiz.winfo_screenwidth()

        htotal = raiz.winfo_screenheight()

        wwindow = 750

        hvwindow = 400

        pwidth = round(wtotal/2-wwindow/2)

        pheight = round(htotal/2-hvwindow/2)

        raiz.geometry(str(wwindow)+"x"+str(hvwindow)+"+"+str(pwidth)+"+"+str(pheight))

        raiz.configure(background="#5CE1E6")

        raiz.title("Play is free")

        raiz.resizable(0,0)

        raiz.iconbitmap(os.path.join(carpeta_imagenes,"numero-par-impar.ico"))

        #//////////CONFIG////////////////////////////////////////////////

        lb_welcome = tk.Label(
            
            raiz,
            text="""
            Type a number that is in the range (1-1000)
                   To validate if it is odd or even
            """
        ).grid(column=2, row=1)

        lb_response = tk.Label(

            raiz,
            text="Response"
        ).grid(column=3, row=3)

        text_box = tk.Entry(

            raiz,
            justify= tk.CENTER

        ).grid(column=3, row=2)

        button_check = tk.Button(

            raiz,
            text="CHECK"
        ).grid(column=1, row=2)

        raiz.mainloop()

if __name__ == '__main__':
    main()