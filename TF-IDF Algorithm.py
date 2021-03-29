# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:41:17 2020

@author: Administrator
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.linalg import norm
#  str1 是网上关于QA的工作职责要求，  str3 是46的印度老大哥的简历，Android是某个安卓开发的简历， Loki是Loki的简历，QA2是一个印度的学霸哥的简历，str5是咱们团队某个QA的简历

str1='Design and develop test frameworks or test management methods to help test teams use technical means to make product tests faster and better, and use test technical tools to improve test efficiency and coverage. Technical tools improve test efficiency and coverage. Collect the needs of the testing team and provide technical solutions. Be good at innovation and sharing in the test team, and provide technical support for the test team. Have experience in large-scale systems, distributed system testing is preferred. Familiar with selenium, appium automation framework. Those with python, Js or other language development experience '
str3='12-years into Testing and 3 years into development,Strong in Functional testing, System Testing, Integration testing, Adhoc testing, User-Acceptance testing.3+ years of Mobile apps functional testing on e-commerce domain. 5+  years of Test automation exp using selenium and Java. 4+ years of API testing using postman and also automate api using python-requests library. 2+ years of AWS experience on deployment of test stacks and also verify log files for test analysis. 5+ years of experience as Test lead/Manager role and delivered multiple projects. Experience on Requirement analysis of projects and create them into Test design specifications. 5+ years of testing Unix/C++ projects from end to end. Strong knowledge on Defect management tools like TestDirector, Bugzilla, N-trak. Strong in Analyzing the Performance data and Performance tuning. Good knowledge in C/C++ /Core Java and TCP/IP Socket programming. '
Android='5+ years of experience in Android development. Strong knowledge of native android programming with several skills like MVVM, Jetpack components, Dagger2, Clean architecture, Unit testing (Mockito & JUnit), REST architecture, location tracking, Google maps, push notification (FCM & One signal), Firebase Services, UI design with XML and Material design concepts. Having in- depth knowledge of support libraries with new Material design phenomena. '
Loki='Coordinate and organize work with teammates and discusses client issues with technical support to provide the optimal solutions. Help developers understand bugs and defects by investigating the problems with them, gathering helpful information and running performance and automated scripts to better solve the issues by roots. Focus on the customer requirement and product specifications, attach great importance to user experience and the usability of the product.'
QA2='6+ years of experience in software testing, having expertise in web, client-server, desktop and mobile application testing.Sound knowledge of all type of manual testing. Experience in Functional Automation testing using Selenium WebDriver (Python + PYtest, C, & Java) and Katalon Studio Having knowledge of automation using (Python + Appium + PYtest). Having knowledge of API Testing (Talend API Tester, Postman). Experience in testing Web applications, Mobile Apps (Android/iOS), Desktop Applications and Games (Android/iOS).Knowledge in Jmeter for load/Performance testing.Knowledge in Jenkins for continuous integration.Well acquainted with Software Development Life Cycle (SDLC) and Software Testing Life Cycle (STLC).Sound knowledge of bug tracking tools (Mantis, BugTracker, Trello, Workspace, JIRA, TFS). Proficient in QA Testing Methodologies and Agile Software Development Life cycle.Functional/Domain Knowledge of Applications/Systems (e.g. eCommerce, Finance, Hotel Management, Travel Portal, Airport Management, FMCG, Cocos2dx Games, Unity 3D games etc.)Preparing Test Scenarios, Test Cases for module, Test Plan, integration and system testing.Report and track the defects found in the Pre-Production or Live environment. Experience in defect management, defect analysis and defect reporting using test management tools. Experience in executing Black Box, Functionality Testing, Smoke Testing, System Testing, GUI Testing, Integration Testing, Regression Testing and UAT on various applications.Interpreting business requirements and system analysis of application. Experience in client communication and taking part in requirement review meetings with AD, BA and other stakeholders'

def tfidf_similarity(s1,s2):
    def add_space(s):
        return ''.join(list(s))
    # 将字中间加入空格
    s1, s2= add_space(s1),add_space(s2)
    # 转化为TF 矩阵
    cv=TfidfVectorizer(tokenizer=lambda s:s.split())
    corpus =[s1,s2]
    vectors=cv.fit_transform(corpus).toarray()
    print(vectors)
    # 计算TF 系数
    return np.dot(vectors[0], vectors[1])/(norm (vectors[0])* norm(vectors[1]))

print('Loki',tfidf_similarity(str1,Loki))
print('老大哥',tfidf_similarity(str1,str3))
print('学霸哥',tfidf_similarity(str1,QA2))
print('Android',tfidf_similarity(str1,Android))