# ---------------signup----------------
# importing modules

import socket
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
import time


import sys
sys.setrecursionlimit(10000)

Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pop
    size_hint: .4, .4
    auto_dismiss: False
    title: 'Error'
    Button:
        text: 'Error Try again later!'
        on_press: pop.dismiss()
''')

#building popups
class SimplePopup(Popup):
    pass

class SampleApp(App):
    def build(self):
        return SimplePopup()

# --------------------
Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pops
    size_hint: .4, .4
    auto_dismiss: False
    title: 'Error'
    Button:
        text: 'Error Try again later!'
        on_press: pop.dismiss()
''')


class SimplePopupS(Popup):
    pass

class SampleAppS(App):
    def build(self):
        return SimplePopupS()

# --------------------
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        App.title = 'Signup'
#geting userinput for signup
        self.inside = GridLayout()
        self.inside.cols = 2
        a="11"
        self.inside.add_widget(Label(text="Username: "))
        self.name = TextInput(multiline=False, text=a)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Password: "))
        self.Passw = TextInput(multiline=False, password=True)
        self.inside.add_widget(self.Passw)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press = self.client_program)
        self.add_widget(self.submit)
    #connecting to server to send user data
    def client_program(self, name):
        email=self.email.text
        password=self.Passw.text
        Username=self.name.text
        host = "2.126.50.208"  #connects to server host
        port = 5000  # socket server port number

        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server    
        message = email
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        i=0
        while i<=2:
            if i == 2:
                message = Username
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response    
            # message = input(" -> ")  # again take input
            message = password
            # message1 = "password"
            i=i+1
        # checking what server returns 
        if data == "Close":
            print("Close")
            layout = GridLayout(cols = 1, padding = 10) 
            popupLabel = Label(text = "Sucsess")
            closeButton = Button(text = "Close") 
            layout.add_widget(popupLabel) 
            layout.add_widget(closeButton)        
            popup = Popup(title ='Sucsess', 
                        content = layout, 
                        size_hint =(None, None), size =(200, 200))   
            popup.open()    
            closeButton.bind(on_press = popup.dismiss)
            time.sleep(5)
            App.get_running_app().stop()
            PopupExample().run() 
                
        elif data == "email incorrect":
            layout = GridLayout(cols = 1, padding = 10) 
            popupLabel = Label(text = "There was an issue")
            popupLabel1 = Label(text = "Please check your email") 
            closeButton = Button(text = "Close") 
            layout.add_widget(popupLabel) #adding popup to window
            layout.add_widget(popupLabel1)
            layout.add_widget(closeButton) #adding close button       
    
            popup = Popup(title ='email incorrect', 
                        content = layout, 
                        size_hint =(None, None), size =(200, 200))   
            popup.open() 
            closeButton.bind(on_press = popup.dismiss)
            i=0
            print("email incorrect")
        elif data=="Error":
            print("there was an issue please try again later")
            layout = GridLayout(cols = 1, padding = 10) 
            popupLabel = Label(text = "There was an issue")
            popupLabel1 = Label(text = "Please try again later") 
            closeButton = Button(text = "Close") 
            layout.add_widget(popupLabel) 
            layout.add_widget(popupLabel1)
            layout.add_widget(closeButton)        
    
            # Instantiate the modal popup and display 
            popup = Popup(title ='Error', 
                        content = layout, 
                        size_hint =(None, None), size =(200, 200))   
            popup.open()    
    
            # Attach close button press with popup.dismiss action 
            closeButton.bind(on_press = popup.dismiss)
            i=0
        elif data == "User exist":
            print("there was an issue please try again")
            layout = GridLayout(cols = 1, padding = 10) 
            popupLabel = Label(text = "There was an issue")
            popupLabel1 = Label(text = "User already exists") 
            closeButton = Button(text = "Close") 
            layout.add_widget(popupLabel) 
            layout.add_widget(popupLabel1)
            layout.add_widget(closeButton)        
    
            # Instantiate the modal popup and display 
            popup = Popup(title ='Error', 
                        content = layout, 
                        size_hint =(None, None), size =(200, 200))   
            popup.open()    
    
            # Attach close button press with popup.dismiss action 
            closeButton.bind(on_press = popup.dismiss)
            i=0

        else:
            print("done")



class MyApp(App):
    def build(self):
        return MyGrid()

# -----------------Login----------------

Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pop
    size_hint: .4, .4
    auto_dismiss: False
    title: 'Error'
    Button:
        text: 'Error Try again later!'
        on_press: pop.dismiss()
''')



# --------------------
# bulids popup to call later
Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pops
    size_hint: .4, .4
    auto_dismiss: False
    title: 'Error'
    Button:
        text: 'Error Try again later!'
        on_press: pop.dismiss()
''')
# --------------------
# creating class for login window and bulding gridlayout
class MyGrida(GridLayout):
    
    Username = ""
    def __init__(self, **kwargs):
        super(MyGrida, self).__init__(**kwargs)
        self.cols = 1
        App.title = 'Login'
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Username: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)


        self.inside.add_widget(Label(text="Password: "))
        self.Passw = TextInput(multiline=False, password=True)
        self.inside.add_widget(self.Passw)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)
        self.inside.add_widget(Label(text=""))
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press = self.client_program)
        self.inside.add_widget(self.submit)
        # connecting to server to send user data
    def client_program(self, name):
        self.inside.clear_widgets()

        # self.submit.clear_widgets()
        global Username
        email=self.email.text
        password=self.Passw.text
        Username=self.name.text
        
        host = "2.126.50.208"
        port = 1232

        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server    
            # Attach close button press with popup.dismiss action 
        message = email
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        i=0
        while i<=2:
            if i == 2:
                message = Username
            client_socket.send(message.encode())  # send message
            print(message)
            data = client_socket.recv(1024).decode()  # receive response    

            print('Received from server: ' + data)  # show in terminal
            message = password
            i=i+1
        # checking server response
        if data == "Close":
            print("Close")
            layout = GridLayout(cols = 1, padding = 10) 
            popupLabel = Label(text = "Sucsess")
            closeButton = Button(text = "Close") 
            layout.add_widget(popupLabel) 
            layout.add_widget(closeButton)        
            popup = Popup(title ='Sucsess', 
                        content = layout, 
                        size_hint =(None, None), size =(200, 200))   
            popup.open()    
            closeButton.bind(on_press = popup.dismiss)
            time.sleep(5)
            App.get_running_app().stop()
            PopupExample().run() 
                
        elif data == "email incorrect":
            layout = GridLayout(cols = 1, padding = 10) 
            popupLabel = Label(text = "There was an issue")
            popupLabel1 = Label(text = "Please check your email") 
            closeButton = Button(text = "Close") 
            layout.add_widget(popupLabel) 
            layout.add_widget(popupLabel1)
            layout.add_widget(closeButton)        
    
            popup = Popup(title ='email incorrect', 
                        content = layout, 
                        size_hint =(None, None), size =(200, 200))   
            popup.open() 
            closeButton.bind(on_press = popup.dismiss)
            i=0
            print("email incorrect")
        elif data == "login":
            layout = GridLayout(cols = 1, padding = 10) 
            popupLabel = Label(text = "Succsess")
            popupLabel1 = Label(text = "Please wait") 
            closeButton = Button(text = "Close") 
            layout.add_widget(popupLabel) 
            layout.add_widget(popupLabel1)
            layout.add_widget(closeButton)        
            self.remove_widget(self.name)
            self.remove_widget(self.Passw)
            self.remove_widget(self.email)

            popup = Popup(title ='Succsess', 
                        content = layout, 
                        size_hint =(None, None), size =(200, 200))   
            popup.open() 
            closeButton.bind(on_press = popup.dismiss, on_release = chat)
        elif data=="Error":
                print("there was an issue please try again later")
                layout = GridLayout(cols = 1, padding = 10) 
                popupLabel = Label(text = "There was an issue")
                popupLabel1 = Label(text = "Please try again later") 
                closeButton = Button(text = "Close") 
                layout.add_widget(popupLabel) 
                layout.add_widget(popupLabel1)
                layout.add_widget(closeButton)         
                popup = Popup(title ='Error', 
                            content = layout, 
                            size_hint =(None, None), size =(200, 200))   
                popup.open()    
        
                closeButton.bind(on_press = popup.dismiss)
                i=0
        else:
            print("done")




class Login(App):
    def build(self):
        return MyGrida()

# ---------------chat app-------------
# importing modules

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import socket_client
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import sys
import os


kivy.require("1.10.1")


class ConnectPage(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        username = Username
        App.title = 'Chatroom' # names the window
        self.inside = GridLayout()
        self.cols = 2  # used for  grid
        if os.path.isfile("prev_details.txt"):
            with open("prev_details.txt","r") as f: #if file exitst it will pull data which is previus server connection
                d = f.read().split(",")
                prev_ip = d[0]
                prev_port = d[1]
        else: #stops from crashing if no file and sets values to empty
            prev_ip = ""
            prev_port = ""

        # adding widgets to window
        self.add_widget(Label(text='IP:'))  
        self.ip = TextInput(text=prev_ip, multiline=False) 
        self.add_widget(self.ip) 
        self.add_widget(Label(text='Port:'))
        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)
        self.user =  Label(text="username: ")
        self.add_widget(self.user)
        self.username =  Label(text=username)
        self.add_widget(self.username)
        # print(self.username.text)



        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())  
        self.add_widget(self.join)

    def join_button(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = Username
        # saving server connection to speedup connection next time
        with open("prev_details.txt","w") as f:
            f.write(f"{ip},{port},{username}")

        info = f"Joining {ip}:{port} as {username}"
        chat_app.info_page.update_info(info)
        chat_app.screen_manager.current = 'Info'
        Clock.schedule_once(self.connect, 1)


    def connect(self, _):
        #gets connection info e.g. host ports and spits error if no connection
        port = int(self.port.text)
        ip = self.ip.text
        username = Username

        if not socket_client.connect(ip, port, username, show_error):
            return

        chat_app.create_chat_page()
        chat_app.screen_manager.current = 'Chat'



class ScrollableLabel(ScrollView):
#creates scrolable text to allow users to go back and read previus text
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)


        self.chat_history = Label(size_hint_y=None, markup=True)
        self.scroll_to_point = Label()


        self.layout.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll_to_point)


    def update_chat_history(self, message):
        #updates chat when a message is recived
        self.chat_history.text += '\n' + message


        self.layout.height = self.chat_history.texture_size[1] + 15
        self.chat_history.height = self.chat_history.texture_size[1]
        self.chat_history.text_size = (self.chat_history.width * 0.98, None)

        self.scroll_to(self.scroll_to_point)
    
    def update_chat_history_layout(self, _=None):
        self.layout.height = self.chat_history.texture_size[1]+15
        self.chat_history.hight = self.chat_history.texture_size[1]
        self.chat_history.text_size = (self.chat_history.width * 0.98, None)



class ChatPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.rows = 2

        self.history = ScrollableLabel(height=Window.size[1]*0.9, size_hint_y=None)
        self.add_widget(self.history)

        self.new_message = TextInput(width=Window.size[0]*0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        self.send.bind(on_press=self.send_message)# binds send function to button


        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)

        Window.bind(on_key_down=self.on_key_down)

        Clock.schedule_once(self.focus_text_input, 1)
        socket_client.start_listening(self.incoming_message, show_error)
        self.bind(size=self.adjust_fields)

    def adjust_fields(self, *_):
        if Window.size[1] * 0.1 < 50:
            new_height = Window.size[1] -50 
        else:
             new_height = Window.size[1] *0.9
        self.history.height = new_height

        if Window.size[0] * 0.2 <160:
            new_width = Window.size[1] -160
        else:
            new_width = Window.size[0] * 0.8
        self.new_message.width = new_width

        Clock.schedule_once(self.history.update_chat_history_layout, 0.01)
    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.send_message(None)


    def send_message(self, _):
        message = self.new_message.text
        self.new_message.text = ""
        if message:
            self.history.update_chat_history(f"[color=dd2020]{chat_app.connect_page.username.text}[/color] > {message}")
            socket_client.send(message)

        Clock.schedule_once(self.focus_text_input, 0.1)

    
    def focus_text_input(self, _):
        self.new_message.focus = True

    def incoming_message(self, username, message):
        self.history.update_chat_history(f"[color=20dd20]{chat_app.connect_page.username.text}[/color] > {message}")




class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.cols = 1

        self.message = Label(halign="center", valign="middle", font_size=30)


        self.message.bind(width=self.update_text_width)


        self.add_widget(self.message)


    def update_info(self, message):
        self.message.text = message


    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)


class EpicApp(App):
    def build(self):

        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)


        self.info_page = InfoPage()
        screen = Screen(name='Info')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


    def create_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name='Chat')
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)


def show_error(message):
    chat_app.info_page.update_info(message)
    chat_app.screen_manager.current = 'Info'
    Clock.schedule_once(sys.exit, 10)


def chat(self):
    global chat_app
    App.get_running_app().stop()
    if __name__ == "__main__":
        chat_app = EpicApp()
        chat_app.run()





# ----------------L OR S--------------------
# importing modules

import kivy 
from kivy.app import App 
kivy.require('1.9.0')  
from kivy.uix.button import Button 
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.popup import Popup   
from kivy.uix.label import Label 
from kivy.config import Config 
  

Config.set('graphics', 'resizable', True) 

class PopupExample(App): 

  
    def build(self): 
        App.title = 'Login or Signup'
        self.layout = GridLayout(cols = 1, padding = 10) 
  
        # print(App.get_running_app())
          
        layout = GridLayout(cols = 1, padding = 10) 
  
        popupLabel = Label(text = "Login or Signup") 
        login = Button(text = "Login")
        signup = Button(text = "Signup")
        help = Button(text = "Help") 
  
        layout.add_widget(popupLabel) 
        layout.add_widget(login)      
        layout.add_widget(signup)   
        layout.add_widget(help)


        popup = Popup(title ='Login or Signup', 
                      content = layout, 
                      size_hint =(None, None), size =(200, 200))   
        popup.open()    
  
        login.bind(on_press = popup.dismiss,  on_release= self.Login)
        signup.bind(on_press = popup.dismiss, on_release= self.signup)
        help.bind(on_press = popup.dismiss, on_release= self.help)

    def signup(self, signup):
        if __name__ == "__main__":
            sound = SoundLoader.load('signup.mp3')
            sound.play()
            time.sleep(2.3)
            App.get_running_app().stop()
            MyApp().run()
    def Login(self, signup):
        if __name__ == "__main__":
            sound = SoundLoader.load('login.wav')
            sound.play()
            time.sleep(2.3)
            App.get_running_app().stop()
            Login().run()
    def help(self, *_):
        if __name__ == "__main__":
            App.get_running_app().stop()
            about_build().run()

# ---------------about/help-----------------
# importing modules


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.core.window import Window
import kivy.utils
from kivy.uix.floatlayout import FloatLayout

class about(GridLayout, FloatLayout):
    
    def __init__(self, **kwargs):
        super(about, self).__init__(**kwargs)
        self.cols = 1
        App.title = 'About'
        self.inside = GridLayout()
        self.inside.cols = 1
        
        helpe = Button(text="Back",pos_hint={'x': 0, 'center_y': .5}, size_hint=(None, None))
        helpe.bind(on_press=self.back)
        self.add_widget(helpe)


        self.inside.add_widget(Label(text="This app was designed and created by JAGS_BLAST"))
        self.inside.add_widget(Label(text="The first step is to create a login throuh the signup page and please make sure to remeber your login"))
        self.inside.add_widget(Label(text="after you have created your login now you need to login"))
        self.inside.add_widget(Label(text="once you are logged in you will need to ether find someone running the server programe or connect to our main public server"))
        self.inside.add_widget(Label(text="The Host for our public server it at the moment is: '2.126.50.208'"))
        self.inside.add_widget(Label(text="The Port for our public server is: '33000'"))
        self.add_widget(self.inside)

    def back(self, *_):
        self.remove_widget(self.inside)
        # self.remove_widget(helpe)
        App.get_running_app().stop()
        PopupExample().run()

class about_build(App):
    def build(self):
        global Build
        Build = about_build()
        return about()

# ---------------splash----------------
# importing modules
from kivy.app import App
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import time


class timer():
    def work1(self):
        print("RUNNING")
        time.sleep(0.5)
        App.get_running_app().stop()
        PopupExample().run()

class arge(App):

    def build(self):
        wing = Image(source='splash.png',pos=(800,800))
        animation = Animation(x=0, y=0, d=2, t='out_bounce')
        animation.start(wing)

        Clock.schedule_once(timer.work1, 5)
        sound = SoundLoader.load('cry.mp3')
        sound.play()
        return wing
        

if __name__ == "__main__":
    chat_app = EpicApp()
    arge().run()
chat_app = EpicApp()
