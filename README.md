# `dropt.util`: DrOpt Utility Package
This package provides utilities required by the DrOpt suite.
Here is the list of utilities and their description.


## `dropt.util.log`: logging
This module provides standardized logging tools,
including __standard format__, __logger classes__ and __logger wrapper__.
- __standard format__:  
  The standard format for console output is
  ```
  [yyyy-mm-dd HH:MM:SS] {logger_name} [{level_name}] {message}
  ```

  The standard format for log file output is
  ```
  yyyy-mm-dd HH:MM:SS|{logger_name}|{level_name}|{message}
  ```

- __logger classes__:
  - `class Logger`
  - `class DrOptLogger(Logger)`
  - `class DrOptServiceLogger(DrOptLogger)`
  - `class DrOptClientLogger(DrOptLogger)`
  - `class DroptUserLogger(DrOptLogger)`

- __logger wrapper__:
  - `class FuncLoggingWrapper`
