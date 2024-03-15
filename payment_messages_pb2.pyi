from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("user_id", "name", "balance")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    name: str
    balance: float
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., balance: _Optional[float] = ...) -> None: ...

class PaymentRequest(_message.Message):
    __slots__ = ("sender_id", "recipient_id", "amount")
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    sender_id: str
    recipient_id: str
    amount: float
    def __init__(self, sender_id: _Optional[str] = ..., recipient_id: _Optional[str] = ..., amount: _Optional[float] = ...) -> None: ...

class Transaction(_message.Message):
    __slots__ = ("transaction_id", "sender_id", "recipient_id", "amount", "timestamp")
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    sender_id: str
    recipient_id: str
    amount: float
    timestamp: str
    def __init__(self, transaction_id: _Optional[str] = ..., sender_id: _Optional[str] = ..., recipient_id: _Optional[str] = ..., amount: _Optional[float] = ..., timestamp: _Optional[str] = ...) -> None: ...

class PaymentResponse(_message.Message):
    __slots__ = ("success", "message", "transaction")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    transaction: Transaction
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...
