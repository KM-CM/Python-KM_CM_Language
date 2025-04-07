The `Language` library will help you with localizing strings.

There is the global language dictionary (`__LANGUAGE__`), which contains groups, which contain identifiers and translations.
```py
__LANGUAGE__ = {
    '__ALL__': { #`__ALL__` is the group for all translations, useful when you have only one language
        'HelloWorld': 'Hello, World!'
    }
}
assert Localize( '#HelloWorld' ) == Get( 'HelloWorld' ) == 'Hello, World!'
```

The `__ALL__` group is the default group for all translations, useful when you have one language.

The `Localize` function is the only one which I want to talk about more than in the documentation,
and there's no better way to talk about something complicated than straight up show it.

```py
Add( 'Class', 'Class' )
Add( 'OtherClass', 'Other Class' )
print( Localize( '#Class is the parent of #OtherClass who is the parent of #Another #Class' ) ) #'Class is the parent of Other Class who is the parent of Another Class'
```

Now, you might be wondering - why did "Another Class" translate correctly?
Well, it's quite simple - "#Another" turns to "Another", as it's a non-existent translation,
and "#Class" turns into "Class".

Ways for using escape sequences
```py
Add( 'X', 'EX' )
Localize( '#X' ) #'EX'
Localize( '\\#X' ) #'#X'
Localize( '\\\\#X' ) #'\\EX'
```
