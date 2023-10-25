#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import semantic_kernel as sk
import os
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
kernel = sk.Kernel()
api_key = os.getenv("OPENAI_API_KEY")
endpoint = os.getenv("OPENAI_API_BASE")
model = OpenAIChatCompletion("gpt-3.5-turbo", api_key, endpoint=endpoint)
# 安装驱动程序
kernel.add_text_completion_service("my-gpt3", model)
functions = kernel.import_semantic_skill_from_directory(
    "./sk_samples/", "SamplePlugin"
)
cli = functions["GenerateCommand"]
print(cli("将系统日期设为2023-04-01"))
