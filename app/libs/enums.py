

__author__ = 'skywalker'

from enum import Enum


class PendingStatus(Enum):

    Waiting = 1
    Success = 2
    Reject = 3
    Withdrawal = 4

    @classmethod
    def pending_str(cls, status, key):
        key_map = {
            cls.Waiting: {
                'requester': '等待对方邮寄',
                'donor': '等待你邮寄'
            },
            cls.Reject: {
                'requester': '对方已拒绝',
                'donor': '你已拒绝'
            },
            cls.Withdrawal: {
                'requester': '你已撤销',
                'donor': '对方已撤销'
            },
            cls.Success: {
                'requester': '对方已邮寄',
                'donor': '你已邮寄，交易完成'
            }
        }
        return key_map[status][key]
