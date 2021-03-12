class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_auth(f):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            f(*args, **kwargs)

    return wrapper


@is_auth
def create_blog_post(user):
    print(f"This is {user.name}'s blog post.")


new_user = User("Denis")
create_blog_post(new_user)

new_user.is_logged_in = True
create_blog_post(new_user)
