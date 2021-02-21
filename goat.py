class Person():

    # Constructor
    def init(self):
        pass

    # Destructor
    def __del__(self):
        pass

    # Methods
    def setter(self, name, instagram, twitter, phone, email):
        f = open("friends.txt","a",)
        f.write("{"+ name + ","
                   + instagram + ","
                   + twitter + ","
                   + phone + ","
                   + email + "}},"
                    )
        f.close()

    def getter(self, name):
        with open("friends.txt","r") as file:
            data = file.read()
        lines = data.split('},')
        for line in lines:
            v = line.split(',')
            if name == v[0][1:]:
                v[0] == v[0][1:]
                line =  line.split(',')
                line[0] = line[0][1:]
                line[4] = line[4][:-1]
                return line
        return ["-1"]

