
import random
def generate_random_email(domain="ya.ru", username_prefix="cherenkova_06"):
    random_number = random.randint(0, 9999)
    login = f"{username_prefix}{random_number}"
    email = f"{login}@{domain}"
    return email