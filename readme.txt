# Rappy

Rappy is a Python library designed with a similar network/node paradigm that allows RapidMiner extensions to call and
use it. There are two ways to use Rappy:

(1) Using the built-in RapidMiner "Execute Python" operator, you can simply call Rappy objects.
(2) You can build a custom extension for RapidMiner that calls the REST API of Rappy using the URLConnection
    library in Java.