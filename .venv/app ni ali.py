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


# =====================================================
# MAIN MENU SCREEN
# =====================================================

<MainMenuScreen>:
    name: "main"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(25)
        spacing: dp(20)
        md_bg_color: 0.03, 0.07, 0.18, 1

        # ---------------- HEADER ----------------

        MDLabel:
            text: "Savings Tracker"
            font_style: "H3"
            bold: True
            halign: "left"
            valign: "top"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_y: None
            height: dp(80)

        MDLabel:
            text: "Manage your goals and finances"
            font_style: "Subtitle1"
            halign: "left"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.7
            size_hint_y: None
            height: dp(30)

        Widget:

        # ---------------- BUTTONS ----------------

        MDRaisedButton:
            text: "Savings"
            pos_hint: {"center_x": 0.5}
            size_hint: None, None
            size: dp(260), dp(50)
            on_release: app.change_screen("savings")

        MDRaisedButton:
            text: "Add Goal"
            pos_hint: {"center_x": 0.5}
            size_hint: None, None
            size: dp(260), dp(50)
            on_release: app.change_screen("add_goal")

        MDRaisedButton:
            text: "Add Transaction"
            pos_hint: {"center_x": 0.5}
            size_hint: None, None
            size: dp(260), dp(50)
            on_release: app.change_screen("add_transaction")

        MDRaisedButton:
            text: "Transactions"
            pos_hint: {"center_x": 0.5}
            size_hint: None, None
            size: dp(260), dp(50)
            on_release: app.change_screen("transactions")

        MDRaisedButton:
            text: "Summary"
            pos_hint: {"center_x": 0.5}
            size_hint: None, None
            size: dp(260), dp(50)
            on_release: app.change_screen("summary")

        Widget:

        MDLabel:
            text: "Track your savings goals and progress"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.5
            size_hint_y: None
            height: dp(30)


# =====================================================
# SAVINGS SCREEN
# =====================================================

<SavingsScreen>:
    name: "savings"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            pos_hint: {"x": 0}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Savings Goals"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1

        Widget:


# =====================================================
# ADD GOAL SCREEN
# =====================================================

<AddGoalScreen>:
    name: "add_goal"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            pos_hint: {"x": 0}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Add Goal"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1

        Widget:


# =====================================================
# ADD TRANSACTION SCREEN
# =====================================================

<AddTransactionScreen>:
    name: "add_transaction"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            pos_hint: {"x": 0}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Add Transaction"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1

        Widget:


# =====================================================
# TRANSACTIONS SCREEN
# =====================================================

<TransactionsScreen>:
    name: "transactions"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            pos_hint: {"x": 0}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Transactions"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1

        Widget:


# =====================================================
# SUMMARY SCREEN
# =====================================================

<SummaryScreen>:
    name: "summary"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDIconButton:
            icon: "arrow-left"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            pos_hint: {"x": 0}
            on_release: app.change_screen("main")

        MDLabel:
            text: "Summary"
            font_style: "H4"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1

        Widget:
'''


# =====================================================
# SCREEN CLASSES
# =====================================================

class MainMenuScreen(MDScreen):
    pass


class SavingsScreen(MDScreen):
    pass


class AddGoalScreen(MDScreen):
    pass


class AddTransactionScreen(MDScreen):
    pass


class TransactionsScreen(MDScreen):
    pass


class SummaryScreen(MDScreen):
    pass


# =====================================================
# MAIN APP
# =====================================================

class SavingsTrackerApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.current = screen_name


# =====================================================
# RUN APP
# =====================================================

if __name__ == "__main__":
    SavingsTrackerApp().run()