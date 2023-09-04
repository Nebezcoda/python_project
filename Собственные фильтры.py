from aiogram.filters import BaseFilter

# ...
# Это список администраторов бота
admin_ids: list[int] = [173901673, 178876776, 197177271]


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids

# ...
