from enum import Enum

# Definition of some common types
EnvironmentKeyType = str
NodeIdType = int


# Possible results of an evaluation
class ResultEnum(Enum):
    UNDEFINED = 0
    FAILED = 1
    RUNNING = 2
    SUCCEEDED = 3


# State information keys
ADDITIONAL_INFORMATION = "additional_information"
NODE_RESULT = "result"
RUNNING_CHILD = "running_child"
