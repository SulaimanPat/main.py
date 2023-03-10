from aiogram.utils import executor
import logging
from config import dp
from Handlers import client, callback, admin, extra

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admins(dp)
extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)