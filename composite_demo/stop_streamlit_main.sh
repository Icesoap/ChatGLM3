#!/bin/bash
ps -aux|grep 'streamlit run main.py'|grep -v grep|awk '{print $2}'|xargs kill -9