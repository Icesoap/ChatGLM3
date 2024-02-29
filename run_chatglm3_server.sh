#!/bin/bash
cd /root/work/project/ChatGLM3/openai_api_demo
source activate chatglm3
nohup python api_server.py -a >> /root/work/project/ChatGLM3/logs_my/logs_run_server-`date +%Y%m%d`.log 2>&1 &
