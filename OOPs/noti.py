class Notification:
    def send_notification(self):
        pass

class EmailNotifinaction(Notification):
    def send_notification(self):
        email_service.send_email(customer)

class Push_Notification(Notification):
    def send_notification(self):
        firebase.send_push_notification(customer)

class SMS_Notification(Notification):
    def send_notification(self):
        

