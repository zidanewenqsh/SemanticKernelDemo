#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import semantic_kernel as sk
kernel = sk.Kernel()
# functions = kernel.import_semantic_skill_from_directory(
#     "./sk_samples/", "SamplePlugin"
# )
# cli = functions["GenerateCommand"]

# 加载 semantic function。注意目录结构
functions = kernel.import_semantic_skill_from_directory(
    "./sk_samples/", "SamplePlugin")
cli = functions["GenerateCommand"]

# 看结果
print(cli("将系统日期设为2023-04-01"))