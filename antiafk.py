import sys
import pyautogui
import keyboard
import time
import threading


class antiAFK:
    def __init__(self):
        self.supported_games = ['minecraft'] # Lista con los juegos soportados.
        self.selected_game = sys.argv[1].lower() # Argumento que es pasado por consola.
        self.hide_mode = False
        self.reports = bool(sys.argv[2])
        self.sleep_time = float(sys.argv[3]) # El blucle será ejecutado cada 5 minutos (300 segundos).

        # Variables "estado".
        self.game_supported = False # Usaremos esta variable para determinar si el juego seleccionado es soportado.
        self.activate = False
        self.actual_thread = None



        # Diccionario con los macros a ejecutar para cada juego.
        self.macros = {'minecraft': ['w', 's', 'a', 'd', 'fire', 'rotation', 'jump', 'log']}


        # Registramos los macros de eventos.
        keyboard.on_press(self.on_press)


        if self.selected_game in self.supported_games:
            self.game_supported = True
            print(f'You select {self.selected_game} as game to use AntiAFK! Is supported.')

            self.App()

        else:
            self.game_supported = False
            print(f'The game selected no is supported. View the documentation to learn more.')




    def App(self):

        print('\n\nAntiAFK is running! Press "0" key to start and stop.')

        while True: # Bucle escencial de la app.

            keyboard.wait('0')

            time.sleep(1) #TODO: Bajar levemente el tiempo?
            if self.activate:
                new_thread = threading.Thread(target=self.run_macro)
                self.actual_thread = new_thread

                self.actual_thread.start()

                print("\n\n\nTo stop AntiAFK press 0 again.")

            else:
                print("\n\n\nTo run AntiAFK press 0.")



    def run_macro(self):
        while self.activate:
            
            for to_made in self.macros[self.selected_game]:
                if to_made == 'fire':
                    pyautogui.leftClick()
                    time.sleep(.5)

                elif to_made == 'aim':
                    pyautogui.rightClick()
                    time.sleep(.5)


                elif to_made == 'jump':
                    pyautogui.press('space')
                    time.sleep(.5)

                elif to_made == 'rotation': # Moveremos el mouse horizontalmente.
                    pyautogui.dragRel(200, 0, 5)
                    time.sleep(.5)

                elif to_made == 'log': # Con esto manderemos un mensaje al chat y tomaremos una captura.

                    if self.hide_mode == False:
                        pyautogui.press('t')
                        pyautogui.write("[AntiAFK] I'm a Anti-AFK Bot! Give me luck.", .5)
                        pyautogui.press('enter')

                    if self.reports:
                        pyautogui.screenshot('LastReport.jpg')
                    # pyautogui.screenshot()

                    time.sleep(.5)


                else:
                    pyautogui.press(to_made)

            time.sleep(self.sleep_time)


    # Función que maneja la activación y desactivación de los macros.
    def on_press(self, event):
        if event.name == '0':
            if self.activate:

                print("\n\n ----------- The anti-AFK is offline. ----------- ")
                # pyautogui.
                self.activate = False
            
            else:
                print("\n\n ----------- The anti-AFK is online. ----------- ")
                self.activate = True



antiAFK() # Ejecución de la app.