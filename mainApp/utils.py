# utils.py
def get_user_initials(user):
    first_initial = user.first_name[0].upper() if user.first_name else ''
    last_initial = user.last_name[0].upper() if user.last_name else ''
    return f'{first_initial}{last_initial}'
