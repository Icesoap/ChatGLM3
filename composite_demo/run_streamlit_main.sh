#!/bin/bash
cd /root/work/project/ChatGLM3/composite_demo
source activate chatglm3
nohup streamlit run  main.py --server.port=9106 >> /root/work/project/ChatGLM3/composite_demo/logs/logs_run_streamlit_main-`date +%Y%m%d`.log 2>&1 &
