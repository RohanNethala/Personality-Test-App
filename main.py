# Personality Test App by Rohan Nethala
# This app will allow users to determine what their personality type is (introvert vs extrovert).

# Importing Modules into the program
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Building the  app itself
class PersonalityTestApp(App):
    def build(self):
        # Layout for the Personality Test app, where all of the buttons, images, text, etc will be on
        global user_points
        user_points = 0
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (.8, .8)
        self.window.pos_hint = {"center_x": .5, "center_y": .5}

        # Putting the image on the app
        self.logo = Image(source='images/mind image.jpeg')
        self.window.add_widget(self.logo)

        # Putting the label under the image, which is the title of this app
        self.label = Label(
            text="Rohan's Personality Test App",
            bold=True,
            font_size=18,
            color='#87CEEB'
        )
        self.window.add_widget(self.label)

        # Putting the 'enter' button under the  text input box; this will obtain the user's name he/she/they typed in the text input box
        self.start_button = Button(
            text="START",
            size_hint=(1, .5),
            bold=True,
            color='red',
            background_color='yellow',
            background_normal=''
        )
        # Functionality for the start button
        self.window.add_widget(self.start_button)
        self.start_button.bind(on_press=self.start_game)
        return self.window

    # Command for the start button to begin the personality test
    def start_game(self, instance):
        self.window.clear_widgets()

        # question 1 stuff

        # question 1 text/title
        self.question_1 = Label(
            text="Do you like to go to parties?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )

        self.window.add_widget(self.question_1)

        # question 1 buttons
        # Please note that these buttons are almost identical for each question. I chose not to comment the other question's buttons and their respective add/don't add to score commands because it would be tedious to do so.

        # yes button in question 1
        self.yes_button_1 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )

        self.window.add_widget(self.yes_button_1)
        self.yes_button_1.bind(on_press=self.add_to_score_1)

        # no button in question 1
        self.no_button_1 = Button(
            text='NO',
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_1)
        self.no_button_1.bind(on_press=self.dont_add_to_score_1)

        return self.window

    # function(s) for adding to the score. if the user has a final score of 5 or above, he/she/they is an extrovert.
    def add_to_score_1(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()
        self.question_2 = Label(
            text="Do you like to be alone?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_2)

        self.yes_button_2 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_2)
        self.yes_button_2.bind(on_press=self.add_to_score_2)

        self.no_button_2 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_2)
        self.no_button_2.bind(on_press=self.dont_add_to_score_2)

    # function for not adding to the score. if the user has a final score of 4 or lower, he/she/they is an introvert.
    def dont_add_to_score_1(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()
        self.question_2 = Label(
            text="Do you like to be alone?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_2)

        self.yes_button_2 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_2)
        self.yes_button_2.bind(on_press=self.add_to_score_2)

        self.no_button_2 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_2)
        self.no_button_2.bind(on_press=self.dont_add_to_score_2)

    def add_to_score_2(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()
        self.question_3 = Label(
            text="Do you like to be around people?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_3)

        self.yes_button_3 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_3)
        self.yes_button_3.bind(on_press=self.add_to_score_3)

        self.no_button_3 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_3)
        self.no_button_3.bind(on_press=self.dont_add_to_score_3)

    def dont_add_to_score_2(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()
        self.question_3 = Label(
            text="Do you like to be around people?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_3)

        self.yes_button_3 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_3)
        self.yes_button_3.bind(on_press=self.add_to_score_3)

        self.no_button_3 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_3)
        self.no_button_3.bind(on_press=self.dont_add_to_score_3)

    def add_to_score_3(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()
        self.question_4 = Label(
            text="Do people describe you as outgoing, talkative, and friendly?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_4)

        self.yes_button_4 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_4)
        self.yes_button_4.bind(on_press=self.add_to_score_4)

        self.no_button_4 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_4)
        self.no_button_4.bind(on_press=self.dont_add_to_score_4)

    def dont_add_to_score_3(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()
        self.question_4 = Label(
            text="Do people describe you as outgoing, talkative, and friendly?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_4)

        self.yes_button_4 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_4)
        self.yes_button_4.bind(on_press=self.add_to_score_4)

        self.no_button_4 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_4)
        self.no_button_4.bind(on_press=self.dont_add_to_score_4)

    def add_to_score_4(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()
        self.question_5 = Label(
            text="Do you like public speaking?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_5)

        self.yes_button_5 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_5)
        self.yes_button_5.bind(on_press=self.add_to_score_5)

        self.no_button_5 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_5)
        self.no_button_5.bind(on_press=self.dont_add_to_score_5)

    def dont_add_to_score_4(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()
        self.question_5 = Label(
            text="Do you like public speaking?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_5)

        self.yes_button_5 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_5)
        self.yes_button_5.bind(on_press=self.add_to_score_5)

        self.no_button_5 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_5)
        self.no_button_5.bind(on_press=self.dont_add_to_score_5)

    def add_to_score_5(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()
        self.question_6 = Label(
            text="Do you like meeting new people?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_6)

        self.yes_button_6 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_6)
        self.yes_button_6.bind(on_press=self.add_to_score_6)

        self.no_button_6 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_6)
        self.no_button_6.bind(on_press=self.dont_add_to_score_6)

    def dont_add_to_score_5(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()
        self.question_6 = Label(
            text="Do you like meeting new people?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_6)

        self.yes_button_6 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_6)
        self.yes_button_6.bind(on_press=self.add_to_score_6)

        self.no_button_6 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_6)
        self.no_button_6.bind(on_press=self.dont_add_to_score_6)

    def add_to_score_6(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()
        self.question_7 = Label(
            text="Do you often share your problems with others?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_7)

        self.yes_button_7 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_7)
        self.yes_button_7.bind(on_press=self.add_to_score_7)

        self.no_button_7 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_7)
        self.no_button_7.bind(on_press=self.dont_add_to_score_7)

    def dont_add_to_score_6(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()
        self.question_7 = Label(
            text="Do you often share your problems with others?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_7)

        self.yes_button_7 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_7)
        self.yes_button_7.bind(on_press=self.add_to_score_7)

        self.no_button_7 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_7)
        self.no_button_7.bind(on_press=self.dont_add_to_score_7)

    def add_to_score_7(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()
        self.question_8 = Label(
            text="Do you like to be the center of attention?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_8)

        self.yes_button_8 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_8)
        self.yes_button_8.bind(on_press=self.add_to_score_8)

        self.no_button_8 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_8)
        self.no_button_8.bind(on_press=self.dont_add_to_score_8)

    def dont_add_to_score_7(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()
        self.question_8 = Label(
            text="Do you like to be the center of attention?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_8)

        self.yes_button_8 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_8)
        self.yes_button_8.bind(on_press=self.add_to_score_8)

        self.no_button_8 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_8)
        self.no_button_8.bind(on_press=self.dont_add_to_score_8)

    def add_to_score_8(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()
        self.question_9 = Label(
            text="Are you a team player?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_9)

        self.yes_button_9 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_9)
        self.yes_button_9.bind(on_press=self.add_to_score_9)

        self.no_button_9 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_9)
        self.no_button_9.bind(on_press=self.dont_add_to_score_9)

    def dont_add_to_score_8(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()
        self.question_9 = Label(
            text="Are you a team player?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_9)

        self.yes_button_9 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_9)
        self.yes_button_9.bind(on_press=self.add_to_score_9)

        self.no_button_9 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_9)
        self.no_button_9.bind(on_press=self.dont_add_to_score_9)

    def add_to_score_9(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()
        self.question_10 = Label(
            text="Do you like being around large groups of people?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_10)

        self.yes_button_10 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_10)
        self.yes_button_10.bind(on_press=self.add_to_score_10)

        self.no_button_10 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_10)
        self.no_button_10.bind(on_press=self.dont_add_to_score_10)

    def dont_add_to_score_9(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()
        self.question_10 = Label(
            text="Do you like being around large groups of people?",
            pos_hint={"center_x": .5, "top": 1},
            color="lime",
            bold=True,
            font_size=20
        )
        self.window.add_widget(self.question_10)

        self.yes_button_10 = Button(
            text="YES",
            bold=True,
            background_color='red',
            background_normal=''
        )
        self.window.add_widget(self.yes_button_10)
        self.yes_button_10.bind(on_press=self.add_to_score_10)

        self.no_button_10 = Button(
            text="NO",
            bold=True,
            background_color='blue',
            background_normal=''
        )
        self.window.add_widget(self.no_button_10)
        self.no_button_10.bind(on_press=self.dont_add_to_score_10)

    def add_to_score_10(self, instance):
        global user_points
        user_points += 1
        print(user_points)
        self.window.clear_widgets()

        if user_points >= 5:
            self.final_result = Label(
                text="You are an Extrovert!",
                font_size=40,
                color='yellow'
            )
        else:
            self.final_result = Label(
                text="You are an Introvert!",
                font_size=40,
                color='white'
            )
        self.window.add_widget(self.final_result)

    def dont_add_to_score_10(self, instance):
        global user_points
        print(user_points)
        self.window.clear_widgets()

        if user_points >= 5:
            self.final_result = Label(
                text="You are an Extrovert!",
                font_size=40,
                color='yellow'
            )
        else:
            self.final_result = Label(
                text="You are an Introvert!",
                font_size=40,
                color='white'
            )
        self.window.add_widget(self.final_result)


# Running the app
if __name__ == "__main__":
    PersonalityTestApp().run()
    print(f"Hello {user_points}!")
    print("Hello world")
    print("Hello Rohan")