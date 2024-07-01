Python Training Day 6

This README file provide a brief summary of what I have learned in this module.


File Handling and Serialization

File Handling:
Python supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files.

File Modes:
Some of the most common file modes are:
- `r`: Opens a file for reading. (default)
- `w`: Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
- `a`: Opens a file for appending. Creates a new file if it does not exist.
- `x`: Creates a new file. Returns an error if the file exists.
- `r+`: Opens a file for reading and writing.
- `w+`: Opens a file for writing and reading. Creates a new file if it does not exist or truncates the file if it exists.




Reading and Writing CSV Files:

File handling in Python is highly flexible, as it allows you to work with different file types (e.g. text files, binary files, CSV files, etc.), and to perform different operations on files (e.g. read, write, append, etc.).


Serialization and Deserialization:
Serialization is the process of converting an object into a format that can be stored or transmitted. Deserialization is the process of converting the serialized data back into an object. Python provides built-in modules like `pickle` and `json` for serialization and deserialization.

Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object) using this conversion table.

If skipkeys is true (default: False), then dict keys that are not of a basic type (str, int, float, bool, None) will be skipped instead of raising a TypeError.

The json module always produces str objects, not bytes objects. Therefore, fp.write() must support str input.

If ensure_ascii is true (the default), the output is guaranteed to have all incoming non-ASCII characters escaped. If ensure_ascii is false, these characters will be output as-is.


Serialization with Pickle:
Pickle is a module in Python that allows you to serialize and deserialize Python objects. You can use the `pickle.dump()` method to serialize an object to a file and the `pickle.load()` method to deserialize an object from a file.

The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” [1] or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.


