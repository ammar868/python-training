Python Training Day 4

This README file provide a brief summary of what I have learned in this module.
Methods:

Class Methods:

    Related to the class not the object.
    Defined using @classmethod.
    Have access to the state of the class and can modify it.
    

Static Methods:

    Related to the class not the object.
    Defined using @statismethod.
    Can't modify the state of the class or the instance.
    

Attributes:
Class Attributes:

    Set at the class-level
    Shared among all instances of the class.

Instance Attributes:

    Set at init level.
    Specific to each instance.

Encapsulation:

To restrict the access to certain parts of an object.

    Private Attributes: can be defined by prefixing the attributs/method with double underscores __
    Protected Attributes: can be defined by prefixing the attributs/method with single underscore _

Properties:

    Can be defined using @property.
    Allows us to define methods that can be called as attributes.

Abstraction:

    Abstract classes are classes that can't be instantiated.
    Abstract methods are methods declared in an abstract class but have no implemntation on the abstract class.
    The subclass of the abstract class must provide the implementation for the abstract methods.

Method Chaining:

    Allows you to call multiple methods on an object consecutively in a single line of code.

Multiple Inheritance:

    A class can inherit attributes and methods from more than one superclass.
