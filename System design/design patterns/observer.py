# Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.
# Use the Observer pattern when changes to the state of one object may require changing other objects, and the actual set of objects is unknown beforehand or changes dynamically
# Use the pattern when some objects in your app must observe others, but only for a limited time or in specific cases.

from __future__ import annotations
from abc import ABC, abstractmethod

class publisher(ABC):
    @abstractmethod
    def add_subscriber(self,observer):
        pass

    @abstractmethod
    def remove_subscriber(self,observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class YouTubeChannel(publisher):
    def __init__(self,name):
        self.name = name
        self.subscriber = []
        self.subscriber_count = 0
    
    def add_subscriber(self, observer):
        self.subscriber.append(observer)
        self.subscriber_count +=1
    
    def remove_subscriber(self, observer):
        self.subscriber.remove(observer)
        self.subscriber_count -=1
    
    def __str__(self):
        print(f"Name of channel: {self.name}, Number of Customer: {self.subscriber_count}")
    
    def publish_video(self,name):
        print("Publishing a video")
        self.notify(name)

    def notify(self,name_of_video):
        text = f"New Video {name_of_video} added by {self.name}"
        for subscriber in self.subscriber:
            subscriber.add_notification(text)
    
class userObserver(ABC):
    @abstractmethod
    def add_notification(self,text):
        pass

class User(userObserver):
    def __init__(self,name):
        self.name = name

    def add_notification(self, text):
        print(f"hello {self.name},\n {text}")


if __name__=="__main__":
    MyYoutube = YouTubeChannel("Learn Python With Fun!!")

    user_1 = User("James")
    user_2 = User("Alex")

    MyYoutube.add_subscriber(user_1)
    MyYoutube.add_subscriber(user_2)

    MyYoutube.publish_video("Observer Design Pattern using python")
    
    MyYoutube.remove_subscriber(user_1)
    MyYoutube.publish_video("Momento Design Pattern using python")




