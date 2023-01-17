from winotify import Notification, audio


class GameNotifier():

    def __init__(self, button_text):
        self.button_text = button_text

    def get_game_url(self, team_1, team_2):
        return f"https://www.vipstand.se/tag/{team_1}-vs-{team_2}-live-sports-stream"

    def send_notification(self, team_1, team_2):
        toast = Notification(app_id="windows app",
                             title="Winotify Test Toast",
                             msg="New Notification!")
        toast.set_audio(audio.Mail, loop=True)

        toast.add_actions(label="click",
                          launch=self.get_game_url(team_1, team_2))
        toast.show()

if __name__ == "__main__":
  notfier = GameNotifier("A new game")
  notfier.send_notification("rangers", "aberdeen")
