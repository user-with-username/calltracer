<div align="center" style="max-width: 100%; overflow-x: auto; margin: 0 auto;">
  <div style="text-align: center; padding: 0 10px; width: 100%;">
    <h1 style="font-size: clamp(24px, 5vw, 36px); margin: 0 auto;">CallTrace</h1>
  </div>



  <div style="display: flex; justify-content: center; margin: 20px auto; width: 100%;">
    <img src="./assets/calltracer_logo.svg" alt="Calltracer Logo" style="max-width: 100%; height: auto; display: block;">
  </div>

  <div style="text-align: center; margin: 20px auto; width: 100%;">
    <div style="display: inline-flex; flex-wrap: wrap; justify-content: center; gap: 8px;">
      <img src="https://img.shields.io/pypi/v/call-trace?color=blue&label=Latest%20Version" alt="PyPI Version">
      <img src="https://img.shields.io/badge/Python-3.11%2B-blue" alt="Python 3.8+">
      <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
    </div>
  </div>
</div>

A lightweight Python utility to track and log call hierarchy with class and method context.

## Features

- Automatically detects calling class and method names
- Tracks nested call paths within the same class
- Simple integration with existing code
- Clean formatted output for debugging

## Installation

```bash
pip install calltracing
```

## Quick Start

```python
from calltracing import CallContext

class MyClass:
    def method1(self):
        self.method2()
    
    def method2(self):
        print(CallContext.get_caller())

def standalone_function():
    print(CallContext.get_caller())

obj = MyClass()
obj.method1()
standalone_function()
```

## License

MIT License