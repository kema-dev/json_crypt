# roadmap

* Detect input file encoding / make an option to specify it for input and output files
* Maybe read / write in steps instead of one big I/O operation
* Make an api that can be used by other programs, and create a documentation for it
* Make a proper readme with examples, pros and cons
* Make it usable on different type of files (csv, password manager export, ...)
* Use haveibeenpwnd.com to check if a password has been pwned
* Test on different platforms (.replace('\\', '/') for windows might be broken)

## regex

* [demo of used regex](https://regex101.com/r/NBCdDv/1)

## pros / cons

* 7z or w/e can be used to compress files using aes256, but you lose the keys and thus need to decrypt the whole file in order to extract any data.json_crypt is a good choice for larg files that need to access a small amount of targeted data.
