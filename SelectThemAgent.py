# Import customtkinter module
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk
import random

app = ctk.CTk()
ctk.set_appearance_mode("Dark") 

app.geometry('800x600')
app.title('Valorant Agent Selector(Sigma Version)')

agentname = 'Astra', 'Brimstone', 'Breach', 'Clove', 'Chamber', 'Cypher', 'Deadlock', 'Fade', 'Gekko', 'Harbor', 'Iso', 'Jett', 'KAY/O',
'Killjoy', 'Neon', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru'


class Picture:
    astra_img = Image.open('Downloads/tkintersomething/astra.jpg').resize((300,300))
    ast_img = ImageTk.PhotoImage(astra_img)

    breach_img = Image.open('Downloads/tkintersomething/breach.jpg').resize((300,300))
    bre_img = ImageTk.PhotoImage(breach_img)

    brimstone_img = Image.open('Downloads/tkintersomething/brimstone.jpg').resize((300,300))
    bri_img = ImageTk.PhotoImage(brimstone_img)

    chamber_img = Image.open('Downloads/tkintersomething/chamber.jpg').resize((300,300))
    cha_img = ImageTk.PhotoImage(chamber_img)

    cypher_img =  Image.open('Downloads/tkintersomething/cypher.jpg').resize((300,300))
    cyp_img = ImageTk.PhotoImage(cypher_img)

    clove_img = Image.open('Downloads/tkintersomething/clove.jpg').resize((300,300))
    clo_img = ImageTk.PhotoImage(clove_img)

    deadlock_img = Image.open('Downloads/tkintersomething/deadlock.jpg').resize((300,300))
    dea_img = ImageTk.PhotoImage(deadlock_img)

    fade_img = Image.open('Downloads/tkintersomething/fade.jpg').resize((300,300))
    fad_img = ImageTk.PhotoImage(fade_img)

    gekko_img = Image.open('Downloads/tkintersomething/gekko.jpg').resize((300,300))
    gek_img = ImageTk.PhotoImage(gekko_img)

    harbor_img = Image.open('Downloads/tkintersomething/harbor.jpg').resize((300,300))
    har_img = ImageTk.PhotoImage(harbor_img)

    iso1_img = Image.open('Downloads/tkintersomething/iso.jpg').resize((300,300))
    iso_img = ImageTk.PhotoImage(iso1_img)

    jett_img = Image.open('Downloads/tkintersomething/jett.jpg').resize((300,300))
    jet_img = ImageTk.PhotoImage(jett_img)

    kayo_img = Image.open('Downloads/tkintersomething/KAYO.jpg').resize((300,300))
    kay_img = ImageTk.PhotoImage(kayo_img)

    killjoy_img = Image.open('Downloads/tkintersomething/killjoy.jpg').resize((300,300))
    kj_img = ImageTk.PhotoImage(killjoy_img)

    neon_img = Image.open('Downloads/tkintersomething/neon.jpg').resize((300,300))
    neo_img = ImageTk.PhotoImage(neon_img)

    omen_img = Image.open('Downloads/tkintersomething/omen.jpg').resize((300,300))
    ome_img = ImageTk.PhotoImage(omen_img)

    phoenix_img = Image.open('Downloads/tkintersomething/phoenix.jpg').resize((300,300))
    pho_img = ImageTk.PhotoImage(phoenix_img)

    raze_img = Image.open('Downloads/tkintersomething/raze.jpg').resize((300,300))
    raz_img = ImageTk.PhotoImage(raze_img)

    reyna_img = Image.open('Downloads/tkintersomething/reyna.jpg').resize((300,300))
    rey_img = ImageTk.PhotoImage(reyna_img)

    sage_img = Image.open('Downloads/tkintersomething/sage.jpg').resize((300,300))
    sag_img = ImageTk.PhotoImage(sage_img)

    skye_img = Image.open('Downloads/tkintersomething/skye.jpg').resize((300,300))
    sky_img = ImageTk.PhotoImage(skye_img)

    sova_img = Image.open('Downloads/tkintersomething/sova.jpg').resize((300,300))
    sov_img = ImageTk.PhotoImage(sova_img)

    viper_img = Image.open('Downloads/tkintersomething/viper.jpg').resize((300,300))
    vip_img = ImageTk.PhotoImage(viper_img)

    yoru_img = Image.open('Downloads/tkintersomething/yoru.jpg').resize((300,300))
    yor_img = ImageTk.PhotoImage(yoru_img)

class Game:
    def __init__(self, master):
       self.master = master

       self.nameLabel = ctk.CTkLabel(master,
                            text="Random an Agent!", font=("Courier", 44))
       self.nameLabel.grid(row=0, column=0,
                    padx=190, pady=20,
                    sticky="ew")
    
       self.valoagent = ctk.CTkLabel(master,
                            text="", font=("Courier", 80))
       self.valoagent.grid(row=15, column=0,
                    padx=200, pady=20,
                    sticky="ew")
    
       self.agent = ctk.CTkLabel(master,
                            text="",
                            image="")
       self.agent.grid(row=18, column=0,
                    padx=200, pady=20,
                    sticky="ew")
       
       self.buttons = ctk.CTkButton(master,
                            text="Randomize", font=("Courier", 25), command=self.on_button_click, hover_color='green')
       self.buttons.grid(row=3, column=0,
                    padx=150, pady=20,
                    sticky="ew")
    
     
    def on_button_click(self):
        selected_agent = random.choice(agentname)
        self.valoagent.configure(text=selected_agent)
        self.name_selected(selected_agent)
        return selected_agent
    
    def name_selected(self, selected_agent):
        if selected_agent == 'Astra':
            self.agent.configure(image=Picture.ast_img)
        elif selected_agent == 'Breach':
            self.agent.configure(image=Picture.bre_img)
        elif selected_agent == 'Brimstone':
            self.agent.configure(image=Picture.bri_img)
        elif selected_agent == 'Chamber':
            self.agent.configure(image=Picture.cha_img)
        elif selected_agent == 'Cypher':
            self.agent.configure(image=Picture.cyp_img)
        elif selected_agent == 'Clove':
            self.agent.configure(image=Picture.clo_img)
        elif selected_agent == 'Deadlock':
            self.agent.configure(image=Picture.dea_img)
        elif selected_agent == 'Fade':
            self.agent.configure(image=Picture.fad_img)
        elif selected_agent == 'Gekko':
            self.agent.configure(image=Picture.gek_img)
        elif selected_agent == 'Harbor':
            self.agent.configure(image=Picture.har_img)
        elif selected_agent == 'Iso':
            self.agent.configure(image=Picture.iso_img)
        elif selected_agent == 'Jett':
            self.agent.configure(image=Picture.jet_img)
        elif selected_agent == 'KAY/O':
            self.agent.configure(image=Picture.kay_img)
        elif selected_agent == 'Killjoy':
            self.agent.configure(image=Picture.kj_img)
        elif selected_agent == 'Neon':
            self.agent.configure(image=Picture.neo_img)
        elif selected_agent == 'Omen':
            self.agent.configure(image=Picture.ome_img)
        elif selected_agent == 'Phoenix':
            self.agent.configure(image=Picture.pho_img)
        elif selected_agent == 'Raze':
            self.agent.configure(image=Picture.raz_img)
        elif selected_agent == 'Reyna':
            self.agent.configure(image=Picture.rey_img)
        elif selected_agent == 'Sage':
            self.agent.configure(image=Picture.sag_img)
        elif selected_agent == 'Skye':
            self.agent.configure(image=Picture.sky_img)
        elif selected_agent == 'Sova':
            self.agent.configure(image=Picture.sov_img)
        elif selected_agent == 'Viper':
            self.agent.configure(image=Picture.vip_img)
        elif selected_agent == 'Yoru':
            self.agent.configure(image=Picture.yor_img)

game_instance = Game(app)
app.mainloop()