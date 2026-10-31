from models.user import User


def select_top_users_by_rate(users: list[User], top_size: int) -> list[User]:
    if top_size <= 0:
        return []
    return sorted(users, key=lambda user: user.rate, reverse=True)[:top_size]
