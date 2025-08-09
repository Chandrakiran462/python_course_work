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
'''
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
Instagram.uiupdate(6)


kiran.reels(6)
kiran.Instagram(6)
'''

# constructor

class Instagaram:
    # constructor
    def __init__ (self,username,password):                # when ever we need to initialize attributes when we call objects
        print("Welcome to Instagram")
        self._bio= ''       # protected variable
        self.post= []
        self.followers = []
        self.following = []
        self.username = username
        self.__password = password
        print(f'Hello {username} login successful')

    @property           # getter
    def bio(self):
        return self._bio
    @bio.setter         # setter
    def bio(self,upd_bio):
        self._bio = upd_bio
    
    def showPassword(self):
        return self.__password
    def updatePassword(self):
        self.__password = new_pwd 

kiran = Instagaram('Kiran','Kiran@132')


# Encapsulation
# to protect attributes to 


# Public Variables
print ("Bio: ",kiran.bio)
print ("Post: ",kiran.post)
print ("Followers: ",kiran.followers)
print ("Following: ",kiran.following)
print ("Username: ",kiran.username)

# private Variables
print (kiran.showPassword())

# modifing - public variables
# modifing public variables can be done inside class and also outside the class
kiran.bio = 'peace'
kiran.post.append('kiran.png')
kiran.followers.extend(['shannu','sri','sai'])
kiran.following.extend(['ram','chanran'])
kiran.username = 'i_am_kiran'

print('After Update')
print ("Bio: ",kiran.bio)
print ("Post: ",kiran.post)
print ("Followers: ",kiran.followers)
print ("Following: ",kiran.following)
print ("Username: ",kiran.username)


# modifying - private variables
# modifying the private variables can only be done inside the class using a function
# print("showpass",kiran.showPassword())
# print("update password:",updatePassword("krian12") )