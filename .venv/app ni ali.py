from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


KV = '''
ScreenManager:

    MainMenuScreen:
    SavingsScreen:
    AddGoalScreen:
    AddTransactionScreen:
    TransactionsScreen:
    SummaryScreen:


# ---------------- MAIN MENU ----------------
<MainMenuScreen>:
    name: "main"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDLabel:
            text: "Savings Tracker"
            font_style: "H4"
            halign: "left"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            size_hint_y: None
            height: dp(60)

        MDRaisedButton:
            text: "Savings"
            size_hint_x: None
            width: dp(250)
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("savings")

        MDRaisedButton:
            text: "Add Goal"
            size_hint_x: None
            width: dp(250)
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("add_goal")

        MDRaisedButton:
            text: "Add Transaction"
            size_hint_x: None
            width: dp(250)
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("add_transaction")

        MDRaisedButton:
            text: "Transactions"
            size_hint_x: None
            width: dp(250)
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("transactions")

        MDRaisedButton:
            text: "Summary"
            size_hint_x: None
            width: dp(250)
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("summary")


# ---------------- SAVINGS ----------------
<SavingsScreen>:
    name: "savings"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.1}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Savings Goals"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1


# ---------------- ADD GOAL ----------------
<AddGoalScreen>:
    name: "add_goal"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.1}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Add Goal"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1


# ---------------- ADD TRANSACTION ----------------
<AddTransactionScreen>:
    name: "add_transaction"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.1}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Add Transaction"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1


# ---------------- TRANSACTIONS ----------------
<TransactionsScreen>:
    name: "transactions"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.1}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Transactions"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1


# ---------------- SUMMARY ----------------
<SummaryScreen>:
    name: "summary"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": 0.1}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Summary"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
'''

# ---------------- SCREENS ----------------
class MainMenuScreen(MDScreen): pass
class SavingsScreen(MDScreen): pass
class AddGoalScreen(MDScreen): pass
class AddTransactionScreen(MDScreen): pass
class TransactionsScreen(MDScreen): pass
class SummaryScreen(MDScreen): pass


# ---------------- APP ----------------
class SavingsTrackerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.current = screen_name


# ---------------- RUN ----------------
if __name__ == "__main__":
    SavingsTrackerApp().run()