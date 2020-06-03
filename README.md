# `dropt.util`: DrOpt Utility Package
This package provides utilities required by the DrOpt suite.
Here is the list of utilities and their description.


## `dropt.util.log`: logging utility
This module provides standardized logging,
which includes __standard format__, __logger classes__ and __logger wrapper__.
- __standard format__:  
  The standard format for console output is
  ```
  [yyyy-mm-dd HH:MM:SS] {logger_name} [{level_name}] {message}
  ```

  The standard format for file output is
  ```
  yyyy-mm-dd HH:MM:SS|{logger_name}|{level_name}|{message}
  ```

- __logger classes__:
  - `class MetaLogger`
  - `class BaseLogger(MetaLogger)`
  - `class Logger(BaseLogger)`
  - `class SrvLogger(BaseLogger)`
  - `class CliLogger(BaseLogger)`
  - `class UserLogger(BaseLogger)`

- __logger wrapper__:
  - `class FuncLoggingWrapper`
