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
# MAIN MENU
# =====================================================

<MainMenuScreen>:
    name: "main"

    MDBoxLayout:
        orientation: "vertical"
        padding: dp(25)
        spacing: dp(15)
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDLabel:
            text: "Savings Tracker"
            font_style: "H3"
            bold: True
            halign: "left"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            size_hint_y: None
            height: dp(70)

        MDLabel:
            text: "Manage your goals and finances"
            font_style: "Subtitle1"
            halign: "left"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.6
            size_hint_y: None
            height: dp(30)

        Widget:

        # ================= BUTTONS =================

        MDRaisedButton:
            text: "Savings"
            size_hint: None, None
            size: dp(260), dp(50)
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.2, 0.5, 1, 1
            background_normal: ""
            background_down: ""
            on_release: app.change_screen("savings")

        MDRaisedButton:
            text: "Add Goal"
            size_hint: None, None
            size: dp(260), dp(50)
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.1, 0.7, 0.4, 1
            background_normal: ""
            background_down: ""
            on_release: app.change_screen("add_goal")

        MDRaisedButton:
            text: "Add Transaction"
            size_hint: None, None
            size: dp(260), dp(50)
            pos_hint: {"center_x": 0.5}
            md_bg_color: 1, 0.6, 0.2, 1
            background_normal: ""
            background_down: ""
            on_release: app.change_screen("add_transaction")

        MDRaisedButton:
            text: "Transactions"
            size_hint: None, None
            size: dp(260), dp(50)
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.8, 0.3, 0.9, 1
            background_normal: ""
            background_down: ""
            on_release: app.change_screen("transactions")

        MDRaisedButton:
            text: "Summary"
            size_hint: None, None
            size: dp(260), dp(50)
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0.9, 0.2, 0.2, 1
            background_normal: ""
            background_down: ""
            on_release: app.change_screen("summary")

        Widget:

        MDLabel:
            text: "Track your savings goals and progress"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.4
            size_hint_y: None
            height: dp(30)


# =====================================================
# SAVINGS SCREEN
# =====================================================

<SavingsScreen>:
    name: "savings"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDTopAppBar:
            title: "Savings Goals"
            left_action_items: [["arrow-left", lambda x: app.change_screen("main")]]

        MDLabel:
            text: "Your savings goals will appear here"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.6


# =====================================================
# ADD GOAL SCREEN
# =====================================================

<AddGoalScreen>:
    name: "add_goal"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDTopAppBar:
            title: "Add Goal"
            left_action_items: [["arrow-left", lambda x: app.change_screen("main")]]

        MDLabel:
            text: "Create a new savings goal"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.6


# =====================================================
# ADD TRANSACTION SCREEN
# =====================================================

<AddTransactionScreen>:
    name: "add_transaction"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDTopAppBar:
            title: "Add Transaction"
            left_action_items: [["arrow-left", lambda x: app.change_screen("main")]]

        MDLabel:
            text: "Add a new transaction"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.6


# =====================================================
# TRANSACTIONS SCREEN
# =====================================================

<TransactionsScreen>:
    name: "transactions"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDTopAppBar:
            title: "Transactions"
            left_action_items: [["arrow-left", lambda x: app.change_screen("main")]]

        MDLabel:
            text: "Your transactions will appear here"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.6


# =====================================================
# SUMMARY SCREEN
# =====================================================

<SummaryScreen>:
    name: "summary"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 0.03, 0.07, 0.18, 1

        MDTopAppBar:
            title: "Summary"
            left_action_items: [["arrow-left", lambda x: app.change_screen("main")]]

        MDLabel:
            text: "Summary of your savings"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.6
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