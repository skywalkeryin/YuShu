from app.view_models.book import BookViewModel


class MyWishes:
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []

        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list

        self.gifts = self.__parse()
        pass

    # 不建议在方法里， 去修改某个实例变量
    def __parse(self):
        temp_gifts = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_gifts.append(my_gift)
        return temp_gifts


        pass
    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        r = {'id': gift.id,
             'book' : BookViewModel(gift.book),
             'wishes_count': count
             }
        return  r
        # my_gift = MyGift(gift.id, BookViewModel(gift.book), count)
        # return my_gift

# class MyGift:
#     def __init__(self):
#         pass