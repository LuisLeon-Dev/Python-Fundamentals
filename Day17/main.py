"""
In Python, a class is a blueprint for creating objects (instances). 
It defines the properties (attributes) and behaviors (methods) that all objects of that class will have.

We define a class called User.
1. The __init__ method is a special method called a constructor, which initializes the object's attributes. 
    self refers to the instance of the class being created.
2. Inside the constructor, we initialize two attributes: user_id and user_name.
3. We also define a method called follow which count how many followers the user have.
4. We create an instance of the User class called user_1 filling the parameters.
5. We access the attributes (user_id and user_name) using dot notation.
6. We call the follo method on the user_1 object.

Classes provide a way to organize and structure code in a more logical and manageable way, especially for larger projects.
They promote code reuse and make it easier to maintain and extend your codebase.
"""


class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.followings = 0

    def follow(self, user):
        user.followers += 1
        self.followings += 1


user_1 = User("001", "Duke")
user_2 = User("007", "James Bond")

print(
    user_1.id,
    user_1.username,
    "following: ",
    user_1.followings,
    "followers: ",
    user_1.followers,
)
print(
    user_2.id,
    user_2.username,
    "following: ",
    user_2.followings,
    "followers: ",
    user_2.followers,
)
print("************************************")

user_1.follow(user_2)
print(
    user_1.id,
    user_1.username,
    "following: ",
    user_1.followings,
    "followers: ",
    user_1.followers,
)
print(
    user_2.id,
    user_2.username,
    "following: ",
    user_2.followings,
    "followers: ",
    user_2.followers,
)
print("************************************")
user_2.follow(user_1)
print(
    user_1.id,
    user_1.username,
    "following: ",
    user_1.followings,
    "followers: ",
    user_1.followers,
)
print(
    user_2.id,
    user_2.username,
    "following: ",
    user_2.followings,
    "followers: ",
    user_2.followers,
)
