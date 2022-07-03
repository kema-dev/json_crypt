# roadmap

* Maybe read / write in steps instead of one big I/O operation
* Make an api that can be used by other programs, and create a documentation for it. Permit to get the value of a given key directly, using a regex
* Make a key exchange protocol, so that the key can be shared between the two programs and thus do not need to provide plaintext key within each request
* Make an option to specify encoding for input and output files (currently only utf-8 is supported)
* Make it usable on different type of files (csv, password manager export, ...)
* Test on different platforms (.replace('\\', '/') for windows might be broken)
* Use haveibeenpwnd.com to check if a password has been pwned
