Rappy is a Python library that should make it easier to use custom Python modules inside RapidMiner. There are two
main approaches to using Rappy in RapidMiner:

(1) Call the Rappy package directly
(2) Call the Rappy through its REST API.

Rappy contains a RESTful server written in Flask that allows RapidMiner custom extensions to call Python functions
without the need for Java's ProcessBuilder. The latter is not allowed in RapidMiner's security settings and generates
java.io.FilePermission errors. However, executing HTTP calls is allowed.

POST /rest/radiomics/tag2dcm - Runs "tag2dcm" conversion
