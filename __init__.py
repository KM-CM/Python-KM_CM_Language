from __SHARED__ import __LANGUAGE__ as _dLang
from re import sub as _sub

def Add( Identifier, Translation, Group = '__ALL__' ):
    try:
        _dLang[ Group ][ Identifier ] = Translation
    except:
        _dLang[ Group ] = {}
        _dLang[ Group ][ Identifier ] = Translation

def Get( Identifier, Group = '__ALL__' ):
    """
``Get``'s the phrase at ``Identifier``.
    """
    try:
        return _dLang[ Group ][ Identifier ]
    except:
        return ''

def Free( Identifier, Group = '__ALL__' ):
    """
Frees the space at ``Identifier``.
    """
    try:
        G = _dLang[ Group ]
        del G[ Identifier ]
        if not G: del _dLang[ Group ]
    except: pass

def Localize( String, Group = '__ALL__' ):
    try: D = _dLang[ Group ]
    except: D = {}
    def W( M ):
        if M.group( 1 ):
            return '#' + M.group( 1 )
        if M.group( 2 ):
            K = M.group( 2 )
            try: return '\\' + D[ K ]
            except: return '\\' + K
        K = M.group( 3 )
        try: return D[ K ]
        except: return K
    return _sub( r'\\#([A-Za-z0-9_]+)|\\\\#([A-Za-z0-9_]+)|#([A-Za-z0-9_]+)', W, String )