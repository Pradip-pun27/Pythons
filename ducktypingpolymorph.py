class Bird1:
    def speak(self):
        print("chirping chirping1")
class Bird2:
    def speak(self):
        print("chirping Chirping2")
b=Bird2()
class Bird:
    def sound(self,b):
        b.speak()
bird=Bird()
bird.sound(b)