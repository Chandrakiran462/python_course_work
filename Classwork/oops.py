# when ever we need to work our code differnent for different users that is called object orianted programming
# Encapsulation - to restrict few varialbles,
# Inheritance   - Promotes code reuse by allowing new classes to inherit properties and methods from existing classes. 
# Abstraction   - Hides complex implementation details and exposes only necessary features.
# Polymorphism  - Allows objects to take on multiple forms, making code more flexible and dynamic/.
# Modularity    - Code is organized into classes and objects, making it easier to manage and maintain.
# Reusability   - Classes can be reused across different parts of the program or in other programs.
# Scalability   - OOP makes it easier to scale and extend applications.



# oops have classes and objects
# class have attributes and methods
# attributes - data
# class attributes and instant attributes

# class attributes      - these are default attributes or the attributes defined by class
# instance attributes   - data changing form user to user

# Instance methods- the method that deals with instance attributes
# class methods   - the method that deals with class attributes **need to use decorator @classmethod 
# static methods  - when we need work with small functions**need to use decorator @staticmethod

# class is a blueprint
# object is user [syntax] => user = classname()

class Instagram:
    ui = 1
    def addingusername(self,username):          # self will specify the user to know who call the function
        print(f"{username} added")
    @classmethod
    def uiupdate(cls,update_ui):
        cls.ui = update_ui
        print("ui updated")
    @staticmethod
    def reels(ui):
        print("ui updated")

    

kiran = Instagram()
sri = Instagram()
kiran.addingusername('Kiran') 
sri.addingusername('sri')


kiran.uiupdate(7)
kiran.Instagram(6)


kiran.reels(6)
kiran.Instagram(6)