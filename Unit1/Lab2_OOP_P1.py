class User:
    def __init__(self, name, password, label):
        self.name = name
        self.__password =  password
        self.label = label
    def login(self, name, password):
        if (name == self.name and password == self.password):
            print("Logged in.")
    def create_post(self, content, setprivate):
        self.newpost = Post(self)
        self.newpost.upload(content, setprivate)
    def answer_pub(self, publication, content):
        self.newans = Comments(self)
        self.newans.upload(publication.userposter.label,content)


class Post:
    def __init__(self, userposter):
        self.userposter = userposter
        self.content = -1
        self.isprivate = -1
    def upload(self, content, isprivate):
        self.userlabel = self.userposter.label
        self.content = content
        self.isprivate = isprivate
        self.likes = 0
        self.dislikes = 0
        print(f"{self.userlabel}\n{self.content}\nLikes:{self.likes} Dislikes:{self.dislikes}")
    def comment(self, sender):
        comm = Comments(sender)


class Comments:
    def __init__(self, user_commented):
        self.user = user_commented
        self.likes = 0
        self.dislikes = 0
    def upload(self, whoimans, content):
        self.whoimans = whoimans
        self.content = content
        print(f"{self.user.label} answers to {self.whoimans}\n{self.content}\nLikes:{self.likes} Dislikes:{self.dislikes}")



class Message:
    def __init__(self, sender, receptor, content):
        self.sender = sender
        self.receptor = receptor
        self.content = content
    

UserA = User("Juan","Abecedario","@juan123")
UserB = User("Dulce","Vocales","@dulce528")

UserA.create_post("Hola mundo", False)
UserB.answer_pub(UserA.newpost, "Hola devuelta.")