from aiogram.dispatcher.filters.state import StatesGroup, State


class AuthState(StatesGroup):
    user_login = State()
    user_password = State()
    user_password_2 = State()
