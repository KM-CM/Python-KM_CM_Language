def Add( Identifier: str, Translation: str, Group: str = ... ) -> None:
    """
``Add``'s an ``Identifier`` for ``Translation``.
    """

def Get( Identifier: str, Group: str = ... ) -> str:
    """
``Get``'s the phrase at ``Identifier``.
Returns ``None`` if not found.
(For oh-no-my-editor-is-crying purposes,
the ``| None`` part won't be annotated)
    """

def Free( Identifier: str, Group: str = ... ) -> None:
    """
``Free``'s the space at ``Identifier``.
    """

def Localize( String: str, Group: str = ... ) -> str:
    """
Localize everything in ``String``.
Follows the format used by the Source Engine.

For example, imagine that ``Add( 'EX', 'Example' )`` was run.
'#EX' -> 'Example'
'\\\\#EX' -> '#EX'
'\\\\\\\\#EX -> '\\\\Example'

Keys that aren't found are ignored.
'#X' -> 'X'
'\\#X' -> '#X'
'\\\\#X' -> '\\X'
    """