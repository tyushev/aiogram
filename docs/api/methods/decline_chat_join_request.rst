######################
declineChatJoinRequest
######################

Returns: :obj:`bool`

.. automodule:: aiogram.methods.decline_chat_join_request
    :members:
    :member-order: bysource
    :undoc-members: True


Usage
=====

As bot method
-------------

.. code-block::

    result: bool = await bot.decline_chat_join_request(...)


Method as object
----------------

Imports:

- :code:`from aiogram.methods.decline_chat_join_request import DeclineChatJoinRequest`
- alias: :code:`from aiogram.methods import DeclineChatJoinRequest`

In handlers with current bot
----------------------------

.. code-block:: python

    result: bool = await DeclineChatJoinRequest(...)

With specific bot
~~~~~~~~~~~~~~~~~

.. code-block:: python

    result: bool = await bot(DeclineChatJoinRequest(...))

As reply into Webhook in handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    return DeclineChatJoinRequest(...)
