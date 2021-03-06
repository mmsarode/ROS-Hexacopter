"""autogenerated by genpy from rotors_comm/OctomapRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class OctomapRequest(genpy.Message):
  _md5sum = "344fde5399047dec2897455486dc4bf9"
  _type = "rotors_comm/OctomapRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
geometry_msgs/Point bounding_box_origin

geometry_msgs/Point bounding_box_lengths

float64 leaf_size

string filename

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

"""
  __slots__ = ['bounding_box_origin','bounding_box_lengths','leaf_size','filename']
  _slot_types = ['geometry_msgs/Point','geometry_msgs/Point','float64','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       bounding_box_origin,bounding_box_lengths,leaf_size,filename

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(OctomapRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.bounding_box_origin is None:
        self.bounding_box_origin = geometry_msgs.msg.Point()
      if self.bounding_box_lengths is None:
        self.bounding_box_lengths = geometry_msgs.msg.Point()
      if self.leaf_size is None:
        self.leaf_size = 0.
      if self.filename is None:
        self.filename = ''
    else:
      self.bounding_box_origin = geometry_msgs.msg.Point()
      self.bounding_box_lengths = geometry_msgs.msg.Point()
      self.leaf_size = 0.
      self.filename = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_7d.pack(_x.bounding_box_origin.x, _x.bounding_box_origin.y, _x.bounding_box_origin.z, _x.bounding_box_lengths.x, _x.bounding_box_lengths.y, _x.bounding_box_lengths.z, _x.leaf_size))
      _x = self.filename
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.bounding_box_origin is None:
        self.bounding_box_origin = geometry_msgs.msg.Point()
      if self.bounding_box_lengths is None:
        self.bounding_box_lengths = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 56
      (_x.bounding_box_origin.x, _x.bounding_box_origin.y, _x.bounding_box_origin.z, _x.bounding_box_lengths.x, _x.bounding_box_lengths.y, _x.bounding_box_lengths.z, _x.leaf_size,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.filename = str[start:end].decode('utf-8')
      else:
        self.filename = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_7d.pack(_x.bounding_box_origin.x, _x.bounding_box_origin.y, _x.bounding_box_origin.z, _x.bounding_box_lengths.x, _x.bounding_box_lengths.y, _x.bounding_box_lengths.z, _x.leaf_size))
      _x = self.filename
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.bounding_box_origin is None:
        self.bounding_box_origin = geometry_msgs.msg.Point()
      if self.bounding_box_lengths is None:
        self.bounding_box_lengths = geometry_msgs.msg.Point()
      end = 0
      _x = self
      start = end
      end += 56
      (_x.bounding_box_origin.x, _x.bounding_box_origin.y, _x.bounding_box_origin.z, _x.bounding_box_lengths.x, _x.bounding_box_lengths.y, _x.bounding_box_lengths.z, _x.leaf_size,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.filename = str[start:end].decode('utf-8')
      else:
        self.filename = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_7d = struct.Struct("<7d")
"""autogenerated by genpy from rotors_comm/OctomapResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import octomap_msgs.msg
import std_msgs.msg

class OctomapResponse(genpy.Message):
  _md5sum = "be9d2869d24fe40d6bc21ac21f6bb2c5"
  _type = "rotors_comm/OctomapResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """octomap_msgs/Octomap map


================================================================================
MSG: octomap_msgs/Octomap
# A 3D map in binary format, as Octree
Header header

# Flag to denote a binary (only free/occupied) or full occupancy octree (.bt/.ot file)
bool binary

# Class id of the contained octree 
string id

# Resolution (in m) of the smallest octree nodes
float64 resolution

# binary serialization of octree, use conversions.h to read and write octrees
int8[] data

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['map']
  _slot_types = ['octomap_msgs/Octomap']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       map

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(OctomapResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.map is None:
        self.map = octomap_msgs.msg.Octomap()
    else:
      self.map = octomap_msgs.msg.Octomap()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs))
      _x = self.map.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.map.binary))
      _x = self.map.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.map.resolution))
      length = len(self.map.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(struct.pack(pattern, *self.map.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.map is None:
        self.map = octomap_msgs.msg.Octomap()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.map.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.map.binary,) = _struct_B.unpack(str[start:end])
      self.map.binary = bool(self.map.binary)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.id = str[start:end].decode('utf-8')
      else:
        self.map.id = str[start:end]
      start = end
      end += 8
      (self.map.resolution,) = _struct_d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.map.data = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs))
      _x = self.map.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.map.binary))
      _x = self.map.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_d.pack(self.map.resolution))
      length = len(self.map.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sb'%length
      buff.write(self.map.data.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.map is None:
        self.map = octomap_msgs.msg.Octomap()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.map.header.seq, _x.map.header.stamp.secs, _x.map.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.map.header.frame_id = str[start:end]
      start = end
      end += 1
      (self.map.binary,) = _struct_B.unpack(str[start:end])
      self.map.binary = bool(self.map.binary)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map.id = str[start:end].decode('utf-8')
      else:
        self.map.id = str[start:end]
      start = end
      end += 8
      (self.map.resolution,) = _struct_d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sb'%length
      start = end
      end += struct.calcsize(pattern)
      self.map.data = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_d = struct.Struct("<d")
class Octomap(object):
  _type          = 'rotors_comm/Octomap'
  _md5sum = '372c615313844175e948d7a83972d589'
  _request_class  = OctomapRequest
  _response_class = OctomapResponse
