# EventMesh通用中间件

中文| [English](./README.md) 

## 概述

EventMesh是一种动态基础中间件，在事件驱动架构语境中，事件指的是系统中的变更、操作或观察，他们会生成通知，然后响应到各个对事件做出响应的处理器函数中，从而实现解耦合的目的。

使用该中间件的原因是因为业务功能模块之间存在很多直接的调用关系，导致驱动和业务之间的沟通变成了一个强关联的关系，导致我们业务拆解十分复杂，为了独立每个功能块，拆解功能和需求以及产品之间的耦合关系，需要使用独立出来的中间件来解决相关之间的业务耦合和功能耦合，方便分层开发。

## 用法

- [API 参考手册](./docs/zh/API参考手册.md)
- [示例代码](./code/demo.py)

## 贡献

我们欢迎对本项目的改进做出贡献！请按照以下步骤进行贡献：

1. Fork 此仓库。
2. 创建一个新分支（`git checkout -b feature/your-feature`）。
3. 提交您的更改（`git commit -m 'Add your feature'`）。
4. 推送到分支（`git push origin feature/your-feature`）。
5. 打开一个 Pull Request。

## 许可证

本项目使用 Apache 许可证。详细信息请参阅 [LICENSE](./LICENSE) 文件。

## 支持

如果您有任何问题或需要支持，请参阅 [QuecPython 文档](https://python.quectel.com/doc) 或在本仓库中打开一个 issue。
