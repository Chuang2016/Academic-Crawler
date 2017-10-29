# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name: task.py
   Description: 生成任务列表
   Author: Dexter Chen
   Date：2017-10-11
-------------------------------------------------
"""

from datetime import date, datetime, timedelta
import mongodb_handler as mh
import utilities as ut
import pmid_crawler as pc
import detail_crawler as dc


task_list = []

def get_task_config(project_name, sstr):
    project_task_number = mh.count_project_task(project_name) # 本项目一共运行过多少task
    task_number = mh.count_task(project_name, sstr) #本sstr运行过多少次
    if project_task_number == 0: # 如果从来没有运行过这个项目下的task
        endwith = 0
    else:
        endwith = 1 # 按条件提前终止
    if task_number == 0: # 如果是本sstr第一次运行
        mrhours = 2 # 单位是小时
        itemnum = 10000
    else:
        mrhours = 0.1
        itemnum = 20
    return itemnum, mrhours, endwith #  返回了一个列表


def generate_tasks(project_name, sstr): #
    config = get_task_config(project_name, sstr)
    mh.add_new_task(project_name, sstr, ut.time_str("full"), config[0], config[1], config[2], 0)


def generate_task_list(): # 项目名称，第一个项目几小时后开始，项目间最小间隔
    pass

def run_task(project, sstr, itemnum, mrhours, endwith):  # 多少时间后开始运行
    pc.crawl_run(project, sstr, itemnum)
    dc.run_crawler_many(project, itemnum)





if __name__ == '__main__':
    run_task("cancer", "lung,cancer", 10000, 1, 0)
