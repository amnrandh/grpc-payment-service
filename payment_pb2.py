# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: payment.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import payment_messages_pb2 as payment__messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rpayment.proto\x12\x07payment\x1a\x16payment_messages.proto2\xee\x01\n\x07Payment\x12>\n\x0bMakePayment\x12\x17.payment.PaymentRequest\x1a\x14.payment.Transaction\"\x00\x12@\n\x15GetTransactionHistory\x12\r.payment.User\x1a\x14.payment.Transaction\"\x00\x30\x01\x12\x33\n\x11GetAccountBalance\x12\r.payment.User\x1a\r.payment.User\"\x00\x12,\n\nAddAccount\x12\r.payment.User\x1a\r.payment.User\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'payment_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PAYMENT']._serialized_start=51
  _globals['_PAYMENT']._serialized_end=289
# @@protoc_insertion_point(module_scope)
