#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import ExecStats.ttypes
import Status.ttypes
import Types.ttypes
import beeswaxd.ttypes
import TCLIService.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TImpalaQueryOptions(object):
  ABORT_ON_ERROR = 0
  MAX_ERRORS = 1
  DISABLE_CODEGEN = 2
  BATCH_SIZE = 3
  MEM_LIMIT = 4
  NUM_NODES = 5
  MAX_SCAN_RANGE_LENGTH = 6
  MAX_IO_BUFFERS = 7
  NUM_SCANNER_THREADS = 8
  ALLOW_UNSUPPORTED_FORMATS = 9
  DEFAULT_ORDER_BY_LIMIT = 10
  DEBUG_ACTION = 11
  ABORT_ON_DEFAULT_LIMIT_EXCEEDED = 12
  COMPRESSION_CODEC = 13
  SEQ_COMPRESSION_MODE = 14
  HBASE_CACHING = 15
  HBASE_CACHE_BLOCKS = 16
  PARQUET_FILE_SIZE = 17
  EXPLAIN_LEVEL = 18
  SYNC_DDL = 19
  REQUEST_POOL = 20
  V_CPU_CORES = 21
  RESERVATION_REQUEST_TIMEOUT = 22
  DISABLE_CACHED_READS = 23
  DISABLE_OUTERMOST_TOPN = 24
  RM_INITIAL_MEM = 25
  QUERY_TIMEOUT_S = 26
  MAX_BLOCK_MGR_MEMORY = 27
  APPX_COUNT_DISTINCT = 28
  DISABLE_UNSAFE_SPILLS = 29
  EXEC_SINGLE_NODE_ROWS_THRESHOLD = 30

  _VALUES_TO_NAMES = {
    0: "ABORT_ON_ERROR",
    1: "MAX_ERRORS",
    2: "DISABLE_CODEGEN",
    3: "BATCH_SIZE",
    4: "MEM_LIMIT",
    5: "NUM_NODES",
    6: "MAX_SCAN_RANGE_LENGTH",
    7: "MAX_IO_BUFFERS",
    8: "NUM_SCANNER_THREADS",
    9: "ALLOW_UNSUPPORTED_FORMATS",
    10: "DEFAULT_ORDER_BY_LIMIT",
    11: "DEBUG_ACTION",
    12: "ABORT_ON_DEFAULT_LIMIT_EXCEEDED",
    13: "COMPRESSION_CODEC",
    14: "SEQ_COMPRESSION_MODE",
    15: "HBASE_CACHING",
    16: "HBASE_CACHE_BLOCKS",
    17: "PARQUET_FILE_SIZE",
    18: "EXPLAIN_LEVEL",
    19: "SYNC_DDL",
    20: "REQUEST_POOL",
    21: "V_CPU_CORES",
    22: "RESERVATION_REQUEST_TIMEOUT",
    23: "DISABLE_CACHED_READS",
    24: "DISABLE_OUTERMOST_TOPN",
    25: "RM_INITIAL_MEM",
    26: "QUERY_TIMEOUT_S",
    27: "MAX_BLOCK_MGR_MEMORY",
    28: "APPX_COUNT_DISTINCT",
    29: "DISABLE_UNSAFE_SPILLS",
    30: "EXEC_SINGLE_NODE_ROWS_THRESHOLD",
  }

  _NAMES_TO_VALUES = {
    "ABORT_ON_ERROR": 0,
    "MAX_ERRORS": 1,
    "DISABLE_CODEGEN": 2,
    "BATCH_SIZE": 3,
    "MEM_LIMIT": 4,
    "NUM_NODES": 5,
    "MAX_SCAN_RANGE_LENGTH": 6,
    "MAX_IO_BUFFERS": 7,
    "NUM_SCANNER_THREADS": 8,
    "ALLOW_UNSUPPORTED_FORMATS": 9,
    "DEFAULT_ORDER_BY_LIMIT": 10,
    "DEBUG_ACTION": 11,
    "ABORT_ON_DEFAULT_LIMIT_EXCEEDED": 12,
    "COMPRESSION_CODEC": 13,
    "SEQ_COMPRESSION_MODE": 14,
    "HBASE_CACHING": 15,
    "HBASE_CACHE_BLOCKS": 16,
    "PARQUET_FILE_SIZE": 17,
    "EXPLAIN_LEVEL": 18,
    "SYNC_DDL": 19,
    "REQUEST_POOL": 20,
    "V_CPU_CORES": 21,
    "RESERVATION_REQUEST_TIMEOUT": 22,
    "DISABLE_CACHED_READS": 23,
    "DISABLE_OUTERMOST_TOPN": 24,
    "RM_INITIAL_MEM": 25,
    "QUERY_TIMEOUT_S": 26,
    "MAX_BLOCK_MGR_MEMORY": 27,
    "APPX_COUNT_DISTINCT": 28,
    "DISABLE_UNSAFE_SPILLS": 29,
    "EXEC_SINGLE_NODE_ROWS_THRESHOLD": 30,
  }


class TInsertResult(object):
  """
  Attributes:
   - rows_appended
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'rows_appended', (TType.STRING,None,TType.I64,None), None, ), # 1
  )

  def __init__(self, rows_appended=None,):
    self.rows_appended = rows_appended

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.rows_appended = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString()
            _val6 = iprot.readI64()
            self.rows_appended[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TInsertResult')
    if self.rows_appended is not None:
      oprot.writeFieldBegin('rows_appended', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.I64, len(self.rows_appended))
      for kiter7,viter8 in self.rows_appended.items():
        oprot.writeString(kiter7)
        oprot.writeI64(viter8)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.rows_appended is None:
      raise TProtocol.TProtocolException(message='Required field rows_appended is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.rows_appended)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TPingImpalaServiceResp(object):
  """
  Attributes:
   - version
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'version', None, None, ), # 1
  )

  def __init__(self, version=None,):
    self.version = version

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.version = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TPingImpalaServiceResp')
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.STRING, 1)
      oprot.writeString(self.version)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.version)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TResetTableReq(object):
  """
  Attributes:
   - db_name
   - table_name
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'db_name', None, None, ), # 1
    (2, TType.STRING, 'table_name', None, None, ), # 2
  )

  def __init__(self, db_name=None, table_name=None,):
    self.db_name = db_name
    self.table_name = table_name

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.db_name = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.table_name = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TResetTableReq')
    if self.db_name is not None:
      oprot.writeFieldBegin('db_name', TType.STRING, 1)
      oprot.writeString(self.db_name)
      oprot.writeFieldEnd()
    if self.table_name is not None:
      oprot.writeFieldBegin('table_name', TType.STRING, 2)
      oprot.writeString(self.table_name)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.db_name is None:
      raise TProtocol.TProtocolException(message='Required field db_name is unset!')
    if self.table_name is None:
      raise TProtocol.TProtocolException(message='Required field table_name is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.db_name)
    value = (value * 31) ^ hash(self.table_name)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TGetExecSummaryReq(object):
  """
  Attributes:
   - operationHandle
   - sessionHandle
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'operationHandle', (TCLIService.ttypes.TOperationHandle, TCLIService.ttypes.TOperationHandle.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'sessionHandle', (TCLIService.ttypes.TSessionHandle, TCLIService.ttypes.TSessionHandle.thrift_spec), None, ), # 2
  )

  def __init__(self, operationHandle=None, sessionHandle=None,):
    self.operationHandle = operationHandle
    self.sessionHandle = sessionHandle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.operationHandle = TCLIService.ttypes.TOperationHandle()
          self.operationHandle.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.sessionHandle = TCLIService.ttypes.TSessionHandle()
          self.sessionHandle.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TGetExecSummaryReq')
    if self.operationHandle is not None:
      oprot.writeFieldBegin('operationHandle', TType.STRUCT, 1)
      self.operationHandle.write(oprot)
      oprot.writeFieldEnd()
    if self.sessionHandle is not None:
      oprot.writeFieldBegin('sessionHandle', TType.STRUCT, 2)
      self.sessionHandle.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.operationHandle)
    value = (value * 31) ^ hash(self.sessionHandle)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TGetExecSummaryResp(object):
  """
  Attributes:
   - status
   - summary
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'status', (TCLIService.ttypes.TStatus, TCLIService.ttypes.TStatus.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'summary', (ExecStats.ttypes.TExecSummary, ExecStats.ttypes.TExecSummary.thrift_spec), None, ), # 2
  )

  def __init__(self, status=None, summary=None,):
    self.status = status
    self.summary = summary

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = TCLIService.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.summary = ExecStats.ttypes.TExecSummary()
          self.summary.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TGetExecSummaryResp')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.summary is not None:
      oprot.writeFieldBegin('summary', TType.STRUCT, 2)
      self.summary.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.summary)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TGetRuntimeProfileReq(object):
  """
  Attributes:
   - operationHandle
   - sessionHandle
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'operationHandle', (TCLIService.ttypes.TOperationHandle, TCLIService.ttypes.TOperationHandle.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'sessionHandle', (TCLIService.ttypes.TSessionHandle, TCLIService.ttypes.TSessionHandle.thrift_spec), None, ), # 2
  )

  def __init__(self, operationHandle=None, sessionHandle=None,):
    self.operationHandle = operationHandle
    self.sessionHandle = sessionHandle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.operationHandle = TCLIService.ttypes.TOperationHandle()
          self.operationHandle.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.sessionHandle = TCLIService.ttypes.TSessionHandle()
          self.sessionHandle.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TGetRuntimeProfileReq')
    if self.operationHandle is not None:
      oprot.writeFieldBegin('operationHandle', TType.STRUCT, 1)
      self.operationHandle.write(oprot)
      oprot.writeFieldEnd()
    if self.sessionHandle is not None:
      oprot.writeFieldBegin('sessionHandle', TType.STRUCT, 2)
      self.sessionHandle.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.operationHandle)
    value = (value * 31) ^ hash(self.sessionHandle)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TGetRuntimeProfileResp(object):
  """
  Attributes:
   - status
   - profile
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'status', (TCLIService.ttypes.TStatus, TCLIService.ttypes.TStatus.thrift_spec), None, ), # 1
    (2, TType.STRING, 'profile', None, None, ), # 2
  )

  def __init__(self, status=None, profile=None,):
    self.status = status
    self.profile = profile

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.status = TCLIService.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.profile = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TGetRuntimeProfileResp')
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 1)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.profile is not None:
      oprot.writeFieldBegin('profile', TType.STRING, 2)
      oprot.writeString(self.profile)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.status is None:
      raise TProtocol.TProtocolException(message='Required field status is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.profile)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
