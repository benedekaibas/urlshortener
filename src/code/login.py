"""Login for the user's Instagram profile."""

import instaloader

"""
username: bet3655416
password: Pythonproba99-
"""

class Login:
    """Class containing the needed functions."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_login_information(self):
        """Do the login based on user's information."""

        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")

        return self.username, self.password
    
    def user_login(self):
        """Checking user's followers."""
        loader = instaloader.Instaloader()
        return loader.login(self.username, self.password)
    
    def check_followers(self):
        """Checking the followers of the given user."""
        loader = instaloader.Instaloader()
        user_profile = instaloader.Profile.from_username(loader.context, self.username)
        followers = user_profile.get_followers()
        return followers