"""
    Below is an example of how the Single Responsibility principle works
"""

# Wrong way to do it

class UserManager:
    def authenticateUser(self, username, password):
        # Authentication logic
        pass
    
    def update_user_profile(self, user_id, new_profile_data):
        # Updation logic
        pass

    def send_email(self, user_email, email_text):
        # Email logic
        pass

"""
    This way is going to cause issues in the future if a change is made to one of the methods.

    For example, if the authentication method changes, it might effect the email notification logic, etc
"""

# Correct way to do it

class UserAuthenticator:
    def auth_user(self, username, password):
        # Authentication logic
        pass

class ProfileManager:
    def update_user_profile(self, user_id, new_profile_data):
        # Updation logic
        pass

class EmailNotifier:
    def send_email(self, user_email, email_text):
        # Email logic
        pass

"""
    This way won't cause any issues because each functionality is modular and changing one won't inadvertantly affect the other
"""