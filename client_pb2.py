# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='client.proto',
  package='isr.simulation',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63lient.proto\x12\x0eisr.simulation\"!\n\x0cInitResponse\x12\x11\n\tisRunning\x18\x01 \x01(\x08\"\x1e\n\x0cStepResponse\x12\x0e\n\x06isDone\x18\x01 \x01(\x08\"\x8a\x01\n\x11\x45missionsResponse\x12\x43\n\temissions\x18\x01 \x03(\x0b\x32\x30.isr.simulation.EmissionsResponse.EmissionsEntry\x1a\x30\n\x0e\x45missionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\x19\n\x17\x43hangeCellStateResponse\"\x06\n\x04Void2\xa9\x02\n\x05\x41gent\x12\x46\n\x10start_simulation\x12\x1c.isr.simulation.InitResponse\x1a\x14.isr.simulation.Void\x12:\n\x04step\x12\x1c.isr.simulation.StepResponse\x1a\x14.isr.simulation.Void\x12H\n\rget_emissions\x12!.isr.simulation.EmissionsResponse\x1a\x14.isr.simulation.Void\x12R\n\x11\x63hange_cell_state\x12\'.isr.simulation.ChangeCellStateResponse\x1a\x14.isr.simulation.Voidb\x06proto3'
)




_INITRESPONSE = _descriptor.Descriptor(
  name='InitResponse',
  full_name='isr.simulation.InitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isRunning', full_name='isr.simulation.InitResponse.isRunning', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=65,
)


_STEPRESPONSE = _descriptor.Descriptor(
  name='StepResponse',
  full_name='isr.simulation.StepResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isDone', full_name='isr.simulation.StepResponse.isDone', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=97,
)


_EMISSIONSRESPONSE_EMISSIONSENTRY = _descriptor.Descriptor(
  name='EmissionsEntry',
  full_name='isr.simulation.EmissionsResponse.EmissionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='isr.simulation.EmissionsResponse.EmissionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='isr.simulation.EmissionsResponse.EmissionsEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=238,
)

_EMISSIONSRESPONSE = _descriptor.Descriptor(
  name='EmissionsResponse',
  full_name='isr.simulation.EmissionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='emissions', full_name='isr.simulation.EmissionsResponse.emissions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EMISSIONSRESPONSE_EMISSIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=238,
)


_CHANGECELLSTATERESPONSE = _descriptor.Descriptor(
  name='ChangeCellStateResponse',
  full_name='isr.simulation.ChangeCellStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=265,
)


_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='isr.simulation.Void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=273,
)

_EMISSIONSRESPONSE_EMISSIONSENTRY.containing_type = _EMISSIONSRESPONSE
_EMISSIONSRESPONSE.fields_by_name['emissions'].message_type = _EMISSIONSRESPONSE_EMISSIONSENTRY
DESCRIPTOR.message_types_by_name['InitResponse'] = _INITRESPONSE
DESCRIPTOR.message_types_by_name['StepResponse'] = _STEPRESPONSE
DESCRIPTOR.message_types_by_name['EmissionsResponse'] = _EMISSIONSRESPONSE
DESCRIPTOR.message_types_by_name['ChangeCellStateResponse'] = _CHANGECELLSTATERESPONSE
DESCRIPTOR.message_types_by_name['Void'] = _VOID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InitResponse = _reflection.GeneratedProtocolMessageType('InitResponse', (_message.Message,), {
  'DESCRIPTOR' : _INITRESPONSE,
  '__module__' : 'client_pb2'
  # @@protoc_insertion_point(class_scope:isr.simulation.InitResponse)
  })
_sym_db.RegisterMessage(InitResponse)

StepResponse = _reflection.GeneratedProtocolMessageType('StepResponse', (_message.Message,), {
  'DESCRIPTOR' : _STEPRESPONSE,
  '__module__' : 'client_pb2'
  # @@protoc_insertion_point(class_scope:isr.simulation.StepResponse)
  })
_sym_db.RegisterMessage(StepResponse)

EmissionsResponse = _reflection.GeneratedProtocolMessageType('EmissionsResponse', (_message.Message,), {

  'EmissionsEntry' : _reflection.GeneratedProtocolMessageType('EmissionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EMISSIONSRESPONSE_EMISSIONSENTRY,
    '__module__' : 'client_pb2'
    # @@protoc_insertion_point(class_scope:isr.simulation.EmissionsResponse.EmissionsEntry)
    })
  ,
  'DESCRIPTOR' : _EMISSIONSRESPONSE,
  '__module__' : 'client_pb2'
  # @@protoc_insertion_point(class_scope:isr.simulation.EmissionsResponse)
  })
_sym_db.RegisterMessage(EmissionsResponse)
_sym_db.RegisterMessage(EmissionsResponse.EmissionsEntry)

ChangeCellStateResponse = _reflection.GeneratedProtocolMessageType('ChangeCellStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANGECELLSTATERESPONSE,
  '__module__' : 'client_pb2'
  # @@protoc_insertion_point(class_scope:isr.simulation.ChangeCellStateResponse)
  })
_sym_db.RegisterMessage(ChangeCellStateResponse)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'client_pb2'
  # @@protoc_insertion_point(class_scope:isr.simulation.Void)
  })
_sym_db.RegisterMessage(Void)


_EMISSIONSRESPONSE_EMISSIONSENTRY._options = None

_AGENT = _descriptor.ServiceDescriptor(
  name='Agent',
  full_name='isr.simulation.Agent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=276,
  serialized_end=573,
  methods=[
  _descriptor.MethodDescriptor(
    name='start_simulation',
    full_name='isr.simulation.Agent.start_simulation',
    index=0,
    containing_service=None,
    input_type=_INITRESPONSE,
    output_type=_VOID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='step',
    full_name='isr.simulation.Agent.step',
    index=1,
    containing_service=None,
    input_type=_STEPRESPONSE,
    output_type=_VOID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_emissions',
    full_name='isr.simulation.Agent.get_emissions',
    index=2,
    containing_service=None,
    input_type=_EMISSIONSRESPONSE,
    output_type=_VOID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='change_cell_state',
    full_name='isr.simulation.Agent.change_cell_state',
    index=3,
    containing_service=None,
    input_type=_CHANGECELLSTATERESPONSE,
    output_type=_VOID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENT)

DESCRIPTOR.services_by_name['Agent'] = _AGENT

# @@protoc_insertion_point(module_scope)
