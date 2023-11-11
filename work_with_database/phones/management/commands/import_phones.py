import csv

from django.core.management.base import BaseCommand
from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones_list = list(csv.DictReader(file, delimiter=';'))

        for phone_dict in phones_list:

            Phone.objects.create(name = phone_dict['name'],
                  price = phone_dict['price'],
                  image = phone_dict['image'],
                  release_date = phone_dict['release_date'],
                  lte_exists = phone_dict['lte_exists'],
                  )



# class Phone(models.Model):
#     name = models.CharField(max_length= 100)
#     price = models.IntegerField()
#     image = models.URLField()
#     release_date = models.DateField()
#     lte_exists = models.BooleanField()
#     slug = models.SlugField(max_length=50)


# with open('phones.csv', 'r') as file:
#     phones = list(csv.DictReader(file, delimiter=';'))
#     print(phones)
    #[{'id': '1', 'name': 'Samsung Galaxy Edge 2', 'image': 'https://avatars.mds.yandex.net/get-mpic/364668/img_id5636027222104023144.jpeg/orig', 'price': '73000', 'release_date': '2016-12-12', 'lte_exists': 'True'},
    # {'id': '2', 'name': 'Iphone X', 'image': 'https://avatars.mds.yandex.net/get-mpic/200316/img_id270362589725797013.png/orig', 'price': '80000', 'release_date': '2017-06-01', 'lte_exists': 'True'},
    # {'id': '3', 'name': 'Nokia 8', 'image': 'https://avatars.mds.yandex.net/get-mpic/397397/img_id6752445806321208103.jpeg/orig', 'price': '20000', 'release_date': '2013-01-20', 'lte_exists': 'False'}]

#     for phone in phones:
#         print(phone)
#         print (phone['id'],phone['name'],phone['price'],phone['release_date'],phone['lte_exists'],)

# Результат:
# {'id': '1', 'name': 'Samsung Galaxy Edge 2', 'image': 'https://avatars.mds.yandex.net/get-mpic/364668/img_id5636027222104023144.jpeg/orig', 'price': '73000', 'release_date': '2016-12-12', 'lte_exists': 'True'}
# 1 Samsung Galaxy Edge 2 73000 2016-12-12 True
# {'id': '2', 'name': 'Iphone X', 'image': 'https://avatars.mds.yandex.net/get-mpic/200316/img_id270362589725797013.png/orig', 'price': '80000', 'release_date': '2017-06-01', 'lte_exists': 'True'}
# 2 Iphone X 80000 2017-06-01 True
# {'id': '3', 'name': 'Nokia 8', 'image': 'https://avatars.mds.yandex.net/get-mpic/397397/img_id6752445806321208103.jpeg/orig', 'price': '20000', 'release_date': '2013-01-20', 'lte_exists': 'False'}
# 3 Nokia 8 20000 2013-01-20 False