# Decorator is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.
# “Wrapper” is the alternative nickname for the Decorator pattern that clearly expresses the main idea of the pattern. A wrapper is an object that can be linked with some target object. The wrapper contains the same set of methods as the target and delegates to it all requests it receives. However, the wrapper may alter the result by doing something either before or after it passes the request to the target.
# Applicability:
#  Use the Decorator pattern when you need to be able to assign extra behaviors to objects at runtime without breaking the code that uses these objects.
#  Use the pattern when it’s awkward or not possible to extend an object’s behavior using inheritance.

class notifier:
    def get_text(self):
        pass 

class email_notifier(notifier):
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

class sms_notifier(notifier):
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

class notifier_decorator(notifier):
    notifier = None
    def __init__(self, wrapped_notifier):
        self.wrapped_notifier = wrapped_notifier

    def get_text(self):
        return self.wrapped_notifier.get_text()


class email_notifier_decorator(notifier_decorator):
    def __init__(self, wrapped_notifier, subject):
        super().__init__(wrapped_notifier)
        self.subject = subject

    def get_text(self):
        return f"Subject: {self.subject}\n{self.wrapped_notifier.get_text()}"  

class sms_notifier_decorator(notifier_decorator):
    def __init__(self, wrapped_notifier, sender):
        super().__init__(wrapped_notifier)
        self.sender = sender

    def get_text(self):
        return f"Sender: {self.sender}\n{self.wrapped_notifier.get_text()}"

# Example usage

email = email_notifier("Hello Email")
email = email_notifier_decorator(email, "Greetings")
print(email.get_text())

sms = sms_notifier("Hello SMS")
sms = sms_notifier_decorator(sms, "Alice")
print(sms.get_text())