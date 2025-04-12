__LANGUAGE__ = {}

from re import sub as _sub

def Add( Identifier, Translation, Group = '__ALL__' ):
    try:
        __LANGUAGE__[ Group ][ Identifier ] = Translation
    except:
        __LANGUAGE__[ Group ] = {}
        __LANGUAGE__[ Group ][ Identifier ] = Translation

def AddGroup( Translations, Group = '__ALL__' ):
    try: G = __LANGUAGE__[ Group ]
    except:
        G = {}
        __LANGUAGE__[ Group ] = G
    G.update( Translations )

def Get( Identifier, Group = '__ALL__' ):
    try:
        return __LANGUAGE__[ Group ][ Identifier ]
    except:
        return ''

def Free( Identifier, Group = '__ALL__' ):
    try:
        G = __LANGUAGE__[ Group ]
        del G[ Identifier ]
        if not G: del __LANGUAGE__[ Group ]
    except: pass

def FreeGroup( Group ):
    try: del __LANGUAGE__[ Group ]
    except: pass

def Localize( String, Group = '__ALL__' ):
    try: D = __LANGUAGE__[ Group ]
    except: D = {}
    def W( M ):
        if M.group( 1 ):
            return '#' + M.group( 1 )
        if M.group( 2 ):
            K = M.group( 2 )
            try: return '\\' + D[ K ]
            except: return '\\' + K
        if M.group( 3 ):
            return '\\#' + M.group( 3 )
        K = M.group( 4 )
        try: return D[ K ]
        except: return K
    return _sub( r'\\#([A-Za-z0-9_]+)|\\\\#([A-Za-z0-9_]+)|\\\\\\#([A-Za-z0-9_]+)|#([A-Za-z0-9_]+)', W, String )
