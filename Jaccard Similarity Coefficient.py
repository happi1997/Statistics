# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:53:56 2020

@author: Administrator
"""
str1='Design and develop test frameworks or test management methods to help test teams use technical means to make product tests faster and better, and use test technical tools to improve test efficiency and coverage. Technical tools improve test efficiency and coverage. Collect the needs of the testing team and provide technical solutions. Be good at innovation and sharing in the test team, and provide technical support for the test team. Have experience in large-scale systems, distributed system testing is preferred. Familiar with selenium, appium automation framework. Those with python, Js or other language development experience '
str3='12-years into Testing and 3 years into development,Strong in Functional testing, System Testing, Integration testing, Adhoc testing, User-Acceptance testing.3+ years of Mobile apps functional testing on e-commerce domain. 5+  years of Test automation exp using selenium and Java. 4+ years of API testing using postman and also automate api using python-requests library. 2+ years of AWS experience on deployment of test stacks and also verify log files for test analysis. 5+ years of experience as Test lead/Manager role and delivered multiple projects. Experience on Requirement analysis of projects and create them into Test design specifications. 5+ years of testing Unix/C++ projects from end to end. Strong knowledge on Defect management tools like TestDirector, Bugzilla, N-trak. Strong in Analyzing the Performance data and Performance tuning. Good knowledge in C/C++ /Core Java and TCP/IP Socket programming. '
Android='5+ years of experience in Android development. Strong knowledge of native android programming with several skills like MVVM, Jetpack components, Dagger2, Clean architecture, Unit testing (Mockito & JUnit), REST architecture, location tracking, Google maps, push notification (FCM & One signal), Firebase Services, UI design with XML and Material design concepts. Having in- depth knowledge of support libraries with new Material design phenomena. '
Loki='Coordinate and organize work with teammates and discusses client issues with technical support to provide the optimal solutions. Help developers understand bugs and defects by investigating the problems with them, gathering helpful information and running performance and automated scripts to better solve the issues by roots. Focus on the customer requirement and product specifications, attach great importance to user experience and the usability of the product.'
QA2='6+ years of experience in software testing, having expertise in web, client-server, desktop and mobile application testing.Sound knowledge of all type of manual testing. Experience in Functional Automation testing using Selenium WebDriver (Python + PYtest, C, & Java) and Katalon Studio Having knowledge of automation using (Python + Appium + PYtest). Having knowledge of API Testing (Talend API Tester, Postman). Experience in testing Web applications, Mobile Apps (Android/iOS), Desktop Applications and Games (Android/iOS).Knowledge in Jmeter for load/Performance testing.Knowledge in Jenkins for continuous integration.Well acquainted with Software Development Life Cycle (SDLC) and Software Testing Life Cycle (STLC).Sound knowledge of bug tracking tools (Mantis, BugTracker, Trello, Workspace, JIRA, TFS). Proficient in QA Testing Methodologies and Agile Software Development Life cycle.Functional/Domain Knowledge of Applications/Systems (e.g. eCommerce, Finance, Hotel Management, Travel Portal, Airport Management, FMCG, Cocos2dx Games, Unity 3D games etc.)Preparing Test Scenarios, Test Cases for module, Test Plan, integration and system testing.Report and track the defects found in the Pre-Production or Live environment. Experience in defect management, defect analysis and defect reporting using test management tools. Experience in executing Black Box, Functionality Testing, Smoke Testing, System Testing, GUI Testing, Integration Testing, Regression Testing and UAT on various applications.Interpreting business requirements and system analysis of application. Experience in client communication and taking part in requirement review meetings with AD, BA and other stakeholders'

def jaccard_similarity(s1,s2):
    st1=set(s1.lower().split())
    st2=set(s2.lower().split())
    intersection= st1.intersection(st2)
    union=st1.union(st2)
    return float(len(intersection))/len(union)*100


print('老大哥',jaccard_similarity(str1,str3),'%')
print('Android',jaccard_similarity(str1,Android),'%')
print('Loki',jaccard_similarity(str1,Loki),'%')
print('学霸哥',jaccard_similarity(str1,QA2),'%')

List = [jaccard_similarity(str1,str3),jaccard_similarity(str1,Android),jaccard_similarity(str1,Loki),jaccard_similarity(str1,QA2),]
List.sort(reverse=True)
print(List)