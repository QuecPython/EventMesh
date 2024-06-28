# EventMesh General Middleware API Reference Manual

EventMesh is a dynamic middleware designed for use within an event-driven architecture framework. In this context, "events" refer to changes, actions, or observations within the system that generate notifications. These are then dispatched to various handler functions that respond to the events, thereby achieving decoupling.

The rationale for using this middleware stems from the existence of many direct calling relationships between business function modules, which turn the communication between the drivers and the business into a tightly coupled relationship. This complexity makes business modularization very challenging. To isolate each function block and break down the coupling between functions, requirements, and products, it is necessary to employ a standalone middleware. This middleware resolves business and functional couplings, facilitating layered development.

## Event Registration

### `EventMesh.subscribe`

```python
EventMesh.subscribe(topic, function)
```

**Parameters**

- `topic` - The name of the custom event function, a string.
- `function` \- The event function.
  - function(topic, data=None) - The event function must accept two parameters:
    - `topic` - The name of the event function.
    - `data` - The parameters carried, can be set to a default so that no arguments need to be passed when called.

> The event function must be registered before it can be executed by publishing a topic.

## Synchronous Event Publishing

### `EventMesh.publish`

```python
EventMesh.publish(topic, data)
```

**Parameters**

- `topic` - The name of the custom event function, a string.
- `data` - The formal parameters required by the event function, can have a default value and thus not require passing.

**Return Value**

Returns the result of the corresponding event execution function.

## Asynchronous Event Publishing

### `EventMesh.publish_async`

```python
EventMesh.publish_async(topic, data)
```

**Parameters**

- `topic` - The name of the custom event function, a string.
- `data` - The formal parameters required by the event function, can have a default value and thus not require passing.

**Return Value**

Asynchronous event publishing does not return a value.