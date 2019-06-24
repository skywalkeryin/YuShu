# -*- coding: utf-8 -*-


'''
 Author :'skywalkeryin'
 Date :  2019-06-24
'''
from app.view_models.book import BookViewModel


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_single(single) for single in goods]

    def __map_to_single(self, single):

        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = 'unknown'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )


class MyTrades:
    def __init__(self, trades_of_mine, trades_count_list):
        self.trades = []

        self.__trades_of_mine = trades_of_mine
        self.__trades_count_list = trades_count_list

        self.trades = self.__parse()
        pass

    # 不建议在方法里， 去修改某个实例变量
    def __parse(self):
        temp_trades = []
        for trade in self.__trades_of_mine:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)
        return temp_trades

    def __matching(self, trade):
        count = 0
        for trade_count in self.__trades_count_list:
            if trade.isbn == trade_count['isbn']:
                count = trade_count['count']
        r = {'id': trade.id,
             'book': BookViewModel(trade.book),
             'wishes_count': count
             }
        return r
