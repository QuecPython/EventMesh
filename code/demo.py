# Copyright (c) Quectel Wireless Solution, Co., Ltd.All Rights Reserved.
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  
#     http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from usr import EventMesh

# APP Management
class App(object):
    def __init__(self):
        self.managers = []

    def append_manager(self, manager):
        # Add function manager
        self.managers.append(manager)
        return self

    def start(self):
        # Invoke event registration interface
        for manager in self.managers:
            manager.init_event_subscribe()


class FunctionTestA(object):

    def __init__(self):
        pass

    def init_event_subscribe(self):
        # Register event function, 'function_test_A' is the event name, self.function_test is the function to execute for this event
        print("FunctionTestA event subscribe finished")
        EventMesh.subscribe("function_test_A", self.function_test)

    def function_test(self, event, data=None):
        print("FunctionTestA func test, event: {}, data: {}".format(event, data))


class FunctionTestB(object):

    def __init__(self):
        pass

    def init_event_subscribe(self):
        # Register event function, 'function_test_B' is the event name, self.function_test is the function to execute for this event
        print("FunctionTestB event subscribe finished")
        EventMesh.subscribe("function_test_B", self.function_test)

    def function_test(self, event, data=None):
        print("FunctionTestB func test, event: {}, data: {}".format(event, data))


# APP Initialization
TestApp = App()
# Register function managers
TestApp.append_manager(function_a.FunctionTestA())
TestApp.append_manager(function_b.FunctionTestB())
# Initialize app event methods, call event initialization registration interface
TestApp.start()

# Synchronously publish event
EventMesh.publish("function_test_A", "Hello QuecTel")
EventMesh.publish("function_test_B", "Hello QuecPython")
# Asynchronously publish event
EventMesh.publish_async("function_test_A", "publish async Hello QuecTel")
EventMesh.publish_async("function_test_B", "publish async Hello QuecPython")
