from address import Address
from mailing import Mailing


to_address = Address("101000", "Москва", "Тверская", "1", "5")
from_address = Address("102000", "Санкт-Петербург", "Невский", "2", "10")


mail = Mailing(to_address, from_address, 150, "TRACK123456")
print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")