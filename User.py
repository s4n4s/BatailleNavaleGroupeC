class User:

    def sAdmin(self, login, mdp):
        if login == "admin" and mdp == "admin":
            return True
        return False
