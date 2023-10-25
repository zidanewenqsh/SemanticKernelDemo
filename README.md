# SemanticKernelDemo
My microsoft semantic-kernel demo project
# 通过操作系统来类比sk
1. 启动操作系统：`kernel = sk.Kernel()`
2. 安装驱动程序：`kernel.add_xxx_service()`
3. 安装应用程序：`func = kernel.create_semantic_function()`
4. 运行应用程序：`func()`

# Plugins
Plugin就是一组函数的集合，它可以包含两种函数
- Semantic Functions - 语义函数，本质是Prompt Engineering
- Native Functions - 原生函数，本质是OpenAI的Function Calling
## Semantic Functions
Semantic Functions是纯用数据{prompt+描述}定义的，不需要编写任何代码。
一个典型的semantic function包含两个文件：
- skprompt.txt：存放prompt，可以包含参数，还可以调用其它函数
- config.json：存放描述，包括函数功能，参数的数据类型，以及调用大模型的参数
# Memory
# Pipline/Chain

