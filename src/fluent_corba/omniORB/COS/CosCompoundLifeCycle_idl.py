# Python stubs generated by omniidl from ..\..\..\..\..\idl\COS\CosCompoundLifeCycle.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


# #include "CosNaming.idl"
import CosNaming_idl
_0_CosNaming = omniORB.openModule("CosNaming")
_0_CosNaming__POA = omniORB.openModule("CosNaming__POA")

# #include "CosLifeCycle.idl"
import CosLifeCycle_idl
_0_CosLifeCycle = omniORB.openModule("CosLifeCycle")
_0_CosLifeCycle__POA = omniORB.openModule("CosLifeCycle__POA")

# #include "corbaidl.idl"
import corbaidl_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")

# #include "boxes.idl"
import boxes_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")

# #include "ir.idl"
import ir_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")

# #include "CosObjectIdentity.idl"
import CosObjectIdentity_idl
_0_CosObjectIdentity = omniORB.openModule("CosObjectIdentity")
_0_CosObjectIdentity__POA = omniORB.openModule("CosObjectIdentity__POA")

# #include "CosRelationships.idl"
import CosRelationships_idl
_0_CosRelationships = omniORB.openModule("CosRelationships")
_0_CosRelationships__POA = omniORB.openModule("CosRelationships__POA")

# #include "CosGraphs.idl"
import CosGraphs_idl
_0_CosGraphs = omniORB.openModule("CosGraphs")
_0_CosGraphs__POA = omniORB.openModule("CosGraphs__POA")

#
# Start of module "CosCompoundLifeCycle"
#
__name__ = "CosCompoundLifeCycle"
_0_CosCompoundLifeCycle = omniORB.openModule("CosCompoundLifeCycle", r"..\..\..\..\..\idl\COS\CosCompoundLifeCycle.idl")
_0_CosCompoundLifeCycle__POA = omniORB.openModule("CosCompoundLifeCycle__POA", r"..\..\..\..\..\idl\COS\CosCompoundLifeCycle.idl")


# forward interface OperationsFactory;
_0_CosCompoundLifeCycle._d_OperationsFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/OperationsFactory:1.0", "OperationsFactory")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/OperationsFactory:1.0"] = _0_CosCompoundLifeCycle._d_OperationsFactory

# forward interface Operations;
_0_CosCompoundLifeCycle._d_Operations = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/Operations:1.0", "Operations")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Operations:1.0"] = _0_CosCompoundLifeCycle._d_Operations

# forward interface Node;
_0_CosCompoundLifeCycle._d_Node = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/Node:1.0", "Node")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Node:1.0"] = _0_CosCompoundLifeCycle._d_Node

# forward interface Role;
_0_CosCompoundLifeCycle._d_Role = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/Role:1.0", "Role")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Role:1.0"] = _0_CosCompoundLifeCycle._d_Role

# forward interface Relationship;
_0_CosCompoundLifeCycle._d_Relationship = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/Relationship:1.0", "Relationship")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Relationship:1.0"] = _0_CosCompoundLifeCycle._d_Relationship

# forward interface PropagationCriteriaFactory;
_0_CosCompoundLifeCycle._d_PropagationCriteriaFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/PropagationCriteriaFactory:1.0", "PropagationCriteriaFactory")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/PropagationCriteriaFactory:1.0"] = _0_CosCompoundLifeCycle._d_PropagationCriteriaFactory

# enum Operation
_0_CosCompoundLifeCycle.copy = omniORB.EnumItem("copy", 0)
_0_CosCompoundLifeCycle.move = omniORB.EnumItem("move", 1)
_0_CosCompoundLifeCycle.remove = omniORB.EnumItem("remove", 2)
_0_CosCompoundLifeCycle.Operation = omniORB.Enum("IDL:omg.org/CosCompoundLifeCycle/Operation:1.0", (_0_CosCompoundLifeCycle.copy, _0_CosCompoundLifeCycle.move, _0_CosCompoundLifeCycle.remove,))

_0_CosCompoundLifeCycle._d_Operation  = (omniORB.tcInternal.tv_enum, _0_CosCompoundLifeCycle.Operation._NP_RepositoryId, "Operation", _0_CosCompoundLifeCycle.Operation._items)
_0_CosCompoundLifeCycle._tc_Operation = omniORB.tcInternal.createTypeCode(_0_CosCompoundLifeCycle._d_Operation)
omniORB.registerType(_0_CosCompoundLifeCycle.Operation._NP_RepositoryId, _0_CosCompoundLifeCycle._d_Operation, _0_CosCompoundLifeCycle._tc_Operation)

# struct RelationshipHandle
_0_CosCompoundLifeCycle.RelationshipHandle = omniORB.newEmptyClass()
class RelationshipHandle (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/CosCompoundLifeCycle/RelationshipHandle:1.0"

    def __init__(self, the_relationship, constant_random_id):
        self.the_relationship = the_relationship
        self.constant_random_id = constant_random_id

_0_CosCompoundLifeCycle.RelationshipHandle = RelationshipHandle
_0_CosCompoundLifeCycle._d_RelationshipHandle  = (omniORB.tcInternal.tv_struct, RelationshipHandle, RelationshipHandle._NP_RepositoryId, "RelationshipHandle", "the_relationship", omniORB.typeMapping["IDL:omg.org/CosRelationships/Relationship:1.0"], "constant_random_id", omniORB.typeMapping["IDL:omg.org/CosObjectIdentity/ObjectIdentifier:1.0"])
_0_CosCompoundLifeCycle._tc_RelationshipHandle = omniORB.tcInternal.createTypeCode(_0_CosCompoundLifeCycle._d_RelationshipHandle)
omniORB.registerType(RelationshipHandle._NP_RepositoryId, _0_CosCompoundLifeCycle._d_RelationshipHandle, _0_CosCompoundLifeCycle._tc_RelationshipHandle)
del RelationshipHandle

# interface OperationsFactory
_0_CosCompoundLifeCycle._d_OperationsFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/OperationsFactory:1.0", "OperationsFactory")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/OperationsFactory:1.0"] = _0_CosCompoundLifeCycle._d_OperationsFactory
_0_CosCompoundLifeCycle.OperationsFactory = omniORB.newEmptyClass()
class OperationsFactory :
    _NP_RepositoryId = _0_CosCompoundLifeCycle._d_OperationsFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosCompoundLifeCycle.OperationsFactory = OperationsFactory
_0_CosCompoundLifeCycle._tc_OperationsFactory = omniORB.tcInternal.createTypeCode(_0_CosCompoundLifeCycle._d_OperationsFactory)
omniORB.registerType(OperationsFactory._NP_RepositoryId, _0_CosCompoundLifeCycle._d_OperationsFactory, _0_CosCompoundLifeCycle._tc_OperationsFactory)

# OperationsFactory operations and attributes
OperationsFactory._d_create_compound_operations = ((), (omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Operations:1.0"], ), None)

# OperationsFactory object reference
class _objref_OperationsFactory (CORBA.Object):
    _NP_RepositoryId = OperationsFactory._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def create_compound_operations(self, *args):
        return self._obj.invoke("create_compound_operations", _0_CosCompoundLifeCycle.OperationsFactory._d_create_compound_operations, args)

omniORB.registerObjref(OperationsFactory._NP_RepositoryId, _objref_OperationsFactory)
_0_CosCompoundLifeCycle._objref_OperationsFactory = _objref_OperationsFactory
del OperationsFactory, _objref_OperationsFactory

# OperationsFactory skeleton
__name__ = "CosCompoundLifeCycle__POA"
class OperationsFactory (PortableServer.Servant):
    _NP_RepositoryId = _0_CosCompoundLifeCycle.OperationsFactory._NP_RepositoryId


    _omni_op_d = {"create_compound_operations": _0_CosCompoundLifeCycle.OperationsFactory._d_create_compound_operations}

OperationsFactory._omni_skeleton = OperationsFactory
_0_CosCompoundLifeCycle__POA.OperationsFactory = OperationsFactory
omniORB.registerSkeleton(OperationsFactory._NP_RepositoryId, OperationsFactory)
del OperationsFactory
__name__ = "CosCompoundLifeCycle"

# interface Operations
_0_CosCompoundLifeCycle._d_Operations = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/Operations:1.0", "Operations")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Operations:1.0"] = _0_CosCompoundLifeCycle._d_Operations
_0_CosCompoundLifeCycle.Operations = omniORB.newEmptyClass()
class Operations :
    _NP_RepositoryId = _0_CosCompoundLifeCycle._d_Operations[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosCompoundLifeCycle.Operations = Operations
_0_CosCompoundLifeCycle._tc_Operations = omniORB.tcInternal.createTypeCode(_0_CosCompoundLifeCycle._d_Operations)
omniORB.registerType(Operations._NP_RepositoryId, _0_CosCompoundLifeCycle._d_Operations, _0_CosCompoundLifeCycle._tc_Operations)

# Operations operations and attributes
Operations._d_copy = ((omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Node:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Node:1.0"], ), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotCopyable._NP_RepositoryId: _0_CosLifeCycle._d_NotCopyable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
Operations._d_move = ((omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Node:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotMovable._NP_RepositoryId: _0_CosLifeCycle._d_NotMovable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
Operations._d_remove = ((omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Node:1.0"], ), (), {_0_CosLifeCycle.NotRemovable._NP_RepositoryId: _0_CosLifeCycle._d_NotRemovable})
Operations._d_destroy = ((), (), None)

# Operations object reference
class _objref_Operations (CORBA.Object):
    _NP_RepositoryId = Operations._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def copy(self, *args):
        return self._obj.invoke("copy", _0_CosCompoundLifeCycle.Operations._d_copy, args)

    def move(self, *args):
        return self._obj.invoke("move", _0_CosCompoundLifeCycle.Operations._d_move, args)

    def remove(self, *args):
        return self._obj.invoke("remove", _0_CosCompoundLifeCycle.Operations._d_remove, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_CosCompoundLifeCycle.Operations._d_destroy, args)

omniORB.registerObjref(Operations._NP_RepositoryId, _objref_Operations)
_0_CosCompoundLifeCycle._objref_Operations = _objref_Operations
del Operations, _objref_Operations

# Operations skeleton
__name__ = "CosCompoundLifeCycle__POA"
class Operations (PortableServer.Servant):
    _NP_RepositoryId = _0_CosCompoundLifeCycle.Operations._NP_RepositoryId


    _omni_op_d = {"copy": _0_CosCompoundLifeCycle.Operations._d_copy, "move": _0_CosCompoundLifeCycle.Operations._d_move, "remove": _0_CosCompoundLifeCycle.Operations._d_remove, "destroy": _0_CosCompoundLifeCycle.Operations._d_destroy}

Operations._omni_skeleton = Operations
_0_CosCompoundLifeCycle__POA.Operations = Operations
omniORB.registerSkeleton(Operations._NP_RepositoryId, Operations)
del Operations
__name__ = "CosCompoundLifeCycle"

# interface Node
_0_CosCompoundLifeCycle._d_Node = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/Node:1.0", "Node")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Node:1.0"] = _0_CosCompoundLifeCycle._d_Node
_0_CosCompoundLifeCycle.Node = omniORB.newEmptyClass()
class Node (_0_CosGraphs.Node):
    _NP_RepositoryId = _0_CosCompoundLifeCycle._d_Node[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    
    # exception NotLifeCycleObject
    _0_CosCompoundLifeCycle.Node.NotLifeCycleObject = omniORB.newEmptyClass()
    class NotLifeCycleObject (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosCompoundLifeCycle/Node/NotLifeCycleObject:1.0"

        _NP_ClassName = "CosCompoundLifeCycle.Node.NotLifeCycleObject"

        def __init__(self):
            CORBA.UserException.__init__(self)
    
    _d_NotLifeCycleObject  = (omniORB.tcInternal.tv_except, NotLifeCycleObject, NotLifeCycleObject._NP_RepositoryId, "NotLifeCycleObject")
    _tc_NotLifeCycleObject = omniORB.tcInternal.createTypeCode(_d_NotLifeCycleObject)
    omniORB.registerType(NotLifeCycleObject._NP_RepositoryId, _d_NotLifeCycleObject, _tc_NotLifeCycleObject)


_0_CosCompoundLifeCycle.Node = Node
_0_CosCompoundLifeCycle._tc_Node = omniORB.tcInternal.createTypeCode(_0_CosCompoundLifeCycle._d_Node)
omniORB.registerType(Node._NP_RepositoryId, _0_CosCompoundLifeCycle._d_Node, _0_CosCompoundLifeCycle._tc_Node)

# Node operations and attributes
Node._d_copy_node = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Node:1.0"], omniORB.typeMapping["IDL:omg.org/CosGraphs/Node/Roles:1.0"]), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotCopyable._NP_RepositoryId: _0_CosLifeCycle._d_NotCopyable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
Node._d_move_node = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotMovable._NP_RepositoryId: _0_CosLifeCycle._d_NotMovable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
Node._d_remove_node = ((), (), {_0_CosLifeCycle.NotRemovable._NP_RepositoryId: _0_CosLifeCycle._d_NotRemovable})
Node._d_get_life_cycle_object = ((), (omniORB.typeMapping["IDL:omg.org/CosLifeCycle/LifeCycleObject:1.0"], ), {_0_CosCompoundLifeCycle.Node.NotLifeCycleObject._NP_RepositoryId: _0_CosCompoundLifeCycle.Node._d_NotLifeCycleObject})

# Node object reference
class _objref_Node (_0_CosGraphs._objref_Node):
    _NP_RepositoryId = Node._NP_RepositoryId

    def __init__(self, obj):
        _0_CosGraphs._objref_Node.__init__(self, obj)

    def copy_node(self, *args):
        return self._obj.invoke("copy_node", _0_CosCompoundLifeCycle.Node._d_copy_node, args)

    def move_node(self, *args):
        return self._obj.invoke("move_node", _0_CosCompoundLifeCycle.Node._d_move_node, args)

    def remove_node(self, *args):
        return self._obj.invoke("remove_node", _0_CosCompoundLifeCycle.Node._d_remove_node, args)

    def get_life_cycle_object(self, *args):
        return self._obj.invoke("get_life_cycle_object", _0_CosCompoundLifeCycle.Node._d_get_life_cycle_object, args)

omniORB.registerObjref(Node._NP_RepositoryId, _objref_Node)
_0_CosCompoundLifeCycle._objref_Node = _objref_Node
del Node, _objref_Node

# Node skeleton
__name__ = "CosCompoundLifeCycle__POA"
class Node (_0_CosGraphs__POA.Node):
    _NP_RepositoryId = _0_CosCompoundLifeCycle.Node._NP_RepositoryId


    _omni_op_d = {"copy_node": _0_CosCompoundLifeCycle.Node._d_copy_node, "move_node": _0_CosCompoundLifeCycle.Node._d_move_node, "remove_node": _0_CosCompoundLifeCycle.Node._d_remove_node, "get_life_cycle_object": _0_CosCompoundLifeCycle.Node._d_get_life_cycle_object}
    _omni_op_d.update(_0_CosGraphs__POA.Node._omni_op_d)

Node._omni_skeleton = Node
_0_CosCompoundLifeCycle__POA.Node = Node
omniORB.registerSkeleton(Node._NP_RepositoryId, Node)
del Node
__name__ = "CosCompoundLifeCycle"

# interface Role
_0_CosCompoundLifeCycle._d_Role = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/Role:1.0", "Role")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Role:1.0"] = _0_CosCompoundLifeCycle._d_Role
_0_CosCompoundLifeCycle.Role = omniORB.newEmptyClass()
class Role (_0_CosGraphs.Role):
    _NP_RepositoryId = _0_CosCompoundLifeCycle._d_Role[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosCompoundLifeCycle.Role = Role
_0_CosCompoundLifeCycle._tc_Role = omniORB.tcInternal.createTypeCode(_0_CosCompoundLifeCycle._d_Role)
omniORB.registerType(Role._NP_RepositoryId, _0_CosCompoundLifeCycle._d_Role, _0_CosCompoundLifeCycle._tc_Role)

# Role operations and attributes
Role._d_copy_role = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Role:1.0"], ), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotCopyable._NP_RepositoryId: _0_CosLifeCycle._d_NotCopyable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
Role._d_move_role = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotMovable._NP_RepositoryId: _0_CosLifeCycle._d_NotMovable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
Role._d_life_cycle_propagation = ((omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Operation:1.0"], omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/RelationshipHandle:1.0"], omniORB.typeMapping["IDL:omg.org/CosRelationships/RoleName:1.0"]), (omniORB.typeMapping["IDL:omg.org/CosGraphs/PropagationValue:1.0"], omniORB.tcInternal.tv_boolean), None)

# Role object reference
class _objref_Role (_0_CosGraphs._objref_Role):
    _NP_RepositoryId = Role._NP_RepositoryId

    def __init__(self, obj):
        _0_CosGraphs._objref_Role.__init__(self, obj)

    def copy_role(self, *args):
        return self._obj.invoke("copy_role", _0_CosCompoundLifeCycle.Role._d_copy_role, args)

    def move_role(self, *args):
        return self._obj.invoke("move_role", _0_CosCompoundLifeCycle.Role._d_move_role, args)

    def life_cycle_propagation(self, *args):
        return self._obj.invoke("life_cycle_propagation", _0_CosCompoundLifeCycle.Role._d_life_cycle_propagation, args)

omniORB.registerObjref(Role._NP_RepositoryId, _objref_Role)
_0_CosCompoundLifeCycle._objref_Role = _objref_Role
del Role, _objref_Role

# Role skeleton
__name__ = "CosCompoundLifeCycle__POA"
class Role (_0_CosGraphs__POA.Role):
    _NP_RepositoryId = _0_CosCompoundLifeCycle.Role._NP_RepositoryId


    _omni_op_d = {"copy_role": _0_CosCompoundLifeCycle.Role._d_copy_role, "move_role": _0_CosCompoundLifeCycle.Role._d_move_role, "life_cycle_propagation": _0_CosCompoundLifeCycle.Role._d_life_cycle_propagation}
    _omni_op_d.update(_0_CosGraphs__POA.Role._omni_op_d)

Role._omni_skeleton = Role
_0_CosCompoundLifeCycle__POA.Role = Role
omniORB.registerSkeleton(Role._NP_RepositoryId, Role)
del Role
__name__ = "CosCompoundLifeCycle"

# interface Relationship
_0_CosCompoundLifeCycle._d_Relationship = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/Relationship:1.0", "Relationship")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Relationship:1.0"] = _0_CosCompoundLifeCycle._d_Relationship
_0_CosCompoundLifeCycle.Relationship = omniORB.newEmptyClass()
class Relationship (_0_CosRelationships.Relationship):
    _NP_RepositoryId = _0_CosCompoundLifeCycle._d_Relationship[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosCompoundLifeCycle.Relationship = Relationship
_0_CosCompoundLifeCycle._tc_Relationship = omniORB.tcInternal.createTypeCode(_0_CosCompoundLifeCycle._d_Relationship)
omniORB.registerType(Relationship._NP_RepositoryId, _0_CosCompoundLifeCycle._d_Relationship, _0_CosCompoundLifeCycle._tc_Relationship)

# Relationship operations and attributes
Relationship._d_copy_relationship = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"], omniORB.typeMapping["IDL:omg.org/CosGraphs/NamedRoles:1.0"]), (omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Relationship:1.0"], ), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotCopyable._NP_RepositoryId: _0_CosLifeCycle._d_NotCopyable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
Relationship._d_move_relationship = ((omniORB.typeMapping["IDL:omg.org/CosLifeCycle/FactoryFinder:1.0"], omniORB.typeMapping["IDL:omg.org/CosLifeCycle/Criteria:1.0"]), (), {_0_CosLifeCycle.NoFactory._NP_RepositoryId: _0_CosLifeCycle._d_NoFactory, _0_CosLifeCycle.NotMovable._NP_RepositoryId: _0_CosLifeCycle._d_NotMovable, _0_CosLifeCycle.InvalidCriteria._NP_RepositoryId: _0_CosLifeCycle._d_InvalidCriteria, _0_CosLifeCycle.CannotMeetCriteria._NP_RepositoryId: _0_CosLifeCycle._d_CannotMeetCriteria})
Relationship._d_life_cycle_propagation = ((omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Operation:1.0"], omniORB.typeMapping["IDL:omg.org/CosRelationships/RoleName:1.0"], omniORB.typeMapping["IDL:omg.org/CosRelationships/RoleName:1.0"]), (omniORB.typeMapping["IDL:omg.org/CosGraphs/PropagationValue:1.0"], omniORB.tcInternal.tv_boolean), None)

# Relationship object reference
class _objref_Relationship (_0_CosRelationships._objref_Relationship):
    _NP_RepositoryId = Relationship._NP_RepositoryId

    def __init__(self, obj):
        _0_CosRelationships._objref_Relationship.__init__(self, obj)

    def copy_relationship(self, *args):
        return self._obj.invoke("copy_relationship", _0_CosCompoundLifeCycle.Relationship._d_copy_relationship, args)

    def move_relationship(self, *args):
        return self._obj.invoke("move_relationship", _0_CosCompoundLifeCycle.Relationship._d_move_relationship, args)

    def life_cycle_propagation(self, *args):
        return self._obj.invoke("life_cycle_propagation", _0_CosCompoundLifeCycle.Relationship._d_life_cycle_propagation, args)

omniORB.registerObjref(Relationship._NP_RepositoryId, _objref_Relationship)
_0_CosCompoundLifeCycle._objref_Relationship = _objref_Relationship
del Relationship, _objref_Relationship

# Relationship skeleton
__name__ = "CosCompoundLifeCycle__POA"
class Relationship (_0_CosRelationships__POA.Relationship):
    _NP_RepositoryId = _0_CosCompoundLifeCycle.Relationship._NP_RepositoryId


    _omni_op_d = {"copy_relationship": _0_CosCompoundLifeCycle.Relationship._d_copy_relationship, "move_relationship": _0_CosCompoundLifeCycle.Relationship._d_move_relationship, "life_cycle_propagation": _0_CosCompoundLifeCycle.Relationship._d_life_cycle_propagation}
    _omni_op_d.update(_0_CosRelationships__POA.Relationship._omni_op_d)

Relationship._omni_skeleton = Relationship
_0_CosCompoundLifeCycle__POA.Relationship = Relationship
omniORB.registerSkeleton(Relationship._NP_RepositoryId, Relationship)
del Relationship
__name__ = "CosCompoundLifeCycle"

# interface PropagationCriteriaFactory
_0_CosCompoundLifeCycle._d_PropagationCriteriaFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosCompoundLifeCycle/PropagationCriteriaFactory:1.0", "PropagationCriteriaFactory")
omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/PropagationCriteriaFactory:1.0"] = _0_CosCompoundLifeCycle._d_PropagationCriteriaFactory
_0_CosCompoundLifeCycle.PropagationCriteriaFactory = omniORB.newEmptyClass()
class PropagationCriteriaFactory :
    _NP_RepositoryId = _0_CosCompoundLifeCycle._d_PropagationCriteriaFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosCompoundLifeCycle.PropagationCriteriaFactory = PropagationCriteriaFactory
_0_CosCompoundLifeCycle._tc_PropagationCriteriaFactory = omniORB.tcInternal.createTypeCode(_0_CosCompoundLifeCycle._d_PropagationCriteriaFactory)
omniORB.registerType(PropagationCriteriaFactory._NP_RepositoryId, _0_CosCompoundLifeCycle._d_PropagationCriteriaFactory, _0_CosCompoundLifeCycle._tc_PropagationCriteriaFactory)

# PropagationCriteriaFactory operations and attributes
PropagationCriteriaFactory._d_create = ((omniORB.typeMapping["IDL:omg.org/CosCompoundLifeCycle/Operation:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalCriteria:1.0"], ), None)

# PropagationCriteriaFactory object reference
class _objref_PropagationCriteriaFactory (CORBA.Object):
    _NP_RepositoryId = PropagationCriteriaFactory._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def create(self, *args):
        return self._obj.invoke("create", _0_CosCompoundLifeCycle.PropagationCriteriaFactory._d_create, args)

omniORB.registerObjref(PropagationCriteriaFactory._NP_RepositoryId, _objref_PropagationCriteriaFactory)
_0_CosCompoundLifeCycle._objref_PropagationCriteriaFactory = _objref_PropagationCriteriaFactory
del PropagationCriteriaFactory, _objref_PropagationCriteriaFactory

# PropagationCriteriaFactory skeleton
__name__ = "CosCompoundLifeCycle__POA"
class PropagationCriteriaFactory (PortableServer.Servant):
    _NP_RepositoryId = _0_CosCompoundLifeCycle.PropagationCriteriaFactory._NP_RepositoryId


    _omni_op_d = {"create": _0_CosCompoundLifeCycle.PropagationCriteriaFactory._d_create}

PropagationCriteriaFactory._omni_skeleton = PropagationCriteriaFactory
_0_CosCompoundLifeCycle__POA.PropagationCriteriaFactory = PropagationCriteriaFactory
omniORB.registerSkeleton(PropagationCriteriaFactory._NP_RepositoryId, PropagationCriteriaFactory)
del PropagationCriteriaFactory
__name__ = "CosCompoundLifeCycle"

#
# End of module "CosCompoundLifeCycle"
#
__name__ = "CosCompoundLifeCycle_idl"

_exported_modules = ( "CosCompoundLifeCycle", )

# The end.
