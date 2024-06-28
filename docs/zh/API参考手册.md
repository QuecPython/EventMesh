# EventMesh通用中间件 API 参考手册

EventMesh是一种动态基础中间件，在事件驱动架构语境中，事件指的是系统中的变更、操作或观察，他们会生成通知，然后响应到各个对事件做出响应的处理器函数中，从而实现解耦合的目的。

使用该中间件的原因是因为业务功能模块之间存在很多直接的调用关系，导致驱动和业务之间的沟通变成了一个强关联的关系，导致我们业务拆解十分复杂，为了独立每个功能块，拆解功能和需求以及产品之间的耦合关系，需要使用独立出来的中间件来解决相关之间的业务耦合和功能耦合，方便分层开发。

## 注册事件

### `EventMesh.subscribe`

```python
EventMesh.subscribe(topic, function)
```

**参数**

- `topic` - 自定义事件函数名称，字符串类型。
-  `function `- 事件函数。
  - function(topic, data=None),事件函数必须接收两个参数。
    - `topic` - 事件函数名称。
    - `data` - 携带的参数，可设置默认值，调用时无需传参。

> 事件函数必须先注册才可通过发布topic的方式执行

## 同步发布事件

### `EventMesh.publish`

```python
EventMesh.publish(topic, data)
```

**参数**

- `topic` - 自定义事件函数名称，字符串类型。
-  `data `- 事件函数所需要的形参，有默认值可不传。

**返回值**

接收对应事件执行函数的返回结果

## 异步发布事件

### `EventMesh.publish_async`

```python
EventMesh.publish_async(topic, data)
```

**参数**

- `topic` - 自定义事件函数名称，字符串类型。
-  `data `- 事件函数所需要的形参，有默认值可不传。

**返回值**

异步发布事件的方式无返回值

## 异步发布事件

### `EventMesh.publish_async`

```python
EventMesh.publish_async(topic, data)
```

**参数**

- `topic` - 自定义事件函数名称，字符串类型。
-  `data `- 事件函数所需要的形参，有默认值可不传。

**返回值**

异步发布事件的方式无返回值