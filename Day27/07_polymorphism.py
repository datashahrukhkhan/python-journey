class EmailNotification:
    def send(self):
        print("Sending email")


class SMSNotification:
    def send(self):
        print("Sending SMS")


class PushNotification:
    def send(self):
        print("Sending push notification")


def notify(notification):
    notification.send()


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notify(notification)