""" Module containing serializers.

    These functions are provided as definitions of the basic interface
    that all serializers should implement.

    This abstraction is intended to allow easily switching from one form
    of serialization to another.
"""

import json
from python_agent_utils.messages.message import Message


class BaseSerializer:
    @staticmethod
    def unpack(dump: bytes) -> Message: #pylint: disable=unused-argument
        """ Deserialize to Message.
        """

        raise NotImplementedError("Unpack method in serializer module \
            is not implemented. Use the methods contained in a submodule of \
            serializer, such as json_serializer.")

    @staticmethod
    def pack(msg: Message) -> bytes: #pylint: disable=unused-argument
        """ Serialize to bytes.
        """

        raise NotImplementedError("Pack method in serializer module \
            is not implemented. Use the methods contained in a submodule of \
            serializer, such as json_serializer.")


class JSONSerializer(BaseSerializer):
    """ Serializer using json as i/o format.
    """
    @staticmethod
    def unpack(dump: bytes):
        """ Deserialize from json string to Message, if it looks like a Message.
            Returns a dictionary otherwise.
        """
        def as_message(dct):
            return Message(dct)

        return json.loads(dump, object_hook=as_message)

    @staticmethod
    def pack(msg: Message) -> bytes:
        """ Serialize from Message to json string or from dictionary to json string.
        """
        # TODO: Should return bytes and not string
        # return msg.as_json().encode()
        return msg.as_json()
