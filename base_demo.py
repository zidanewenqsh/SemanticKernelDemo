#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# 启动操作系统
kernel = sk.Kernel()
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("OPENAI_API_BASE")
model = OpenAIChatCompletion("gpt-3.5-turbo", api_key, endpoint=endpoint)
# 安装驱动程序
kernel.add_text_completion_service("my-gpt3", model)
# 安装应用程序
tell_joke_about = kernel.create_semantic_function("Please tell me a joke about {{$input}} in Chinese")
# 运行应用程序
print(tell_joke_about("Hello world"))