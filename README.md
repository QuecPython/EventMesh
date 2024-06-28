# EventMesh General Middleware

[中文](./README_ZH.md) | English

## Overview

EventMesh is a dynamic foundational middleware. In the context of event-driven architecture, an event refers to changes, operations, or observations within a system. These events generate notifications, which are then responded to by various handler functions that react to the events, thereby achieving decoupling.

The reason for using this middleware is due to the numerous direct calling relationships between business function modules. This creates a strong correlation between the driver and business, making business decomposition very complex. To separate each functional block and to decouple functions, requirements, and products, it is necessary to use independent middleware to resolve business and functional coupling, facilitating layered development.

## Usage

- [API Reference Manual](./docs/en/API_Reference.md)
- [Example Code](./code/demo.py)

## Contribution

We welcome contributions to improve this project! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the Apache License. See the [LICENSE](./LICENSE) file for details.

## Support

If you have any questions or need support, please refer to the [QuecPython documentation](https://python.quectel.com/doc/en) or open an issue in this repository.

