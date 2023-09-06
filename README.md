
### Problem statement 1:
   Part 1: EC2 Instance Management using Boto3
   You are tasked with using the Boto3 library to manage an Amazon EC2 instance. Follow the instructions below:
   1. Create an EC2 instance with a public address assigned to it.
   2. Implement a method that allows you to stop and start the instance.
   3. Configure the EC2 instance to run only on alternate days (Monday, Wednesday, Friday, Sunday) 
      between 9:00 AM GMT to 11:30 AM GMT. Ensure that the instance remains stopped during the remaining time to avoid unnecessary costs.

## Pre-requisites: 
1. Create AWS account with default VPC, subnet id, instance_type   
2. Create aws_access_key_id, aws_secret_access_key and set in environment before running script.

## Start application 
1. Install requirments.txt 
   pip install -r requrments.txt
2. ./run.py

## Features:
1. EC2 Instance manager
2. schedule the task 

## Enhancements
1. EC2 manager can be enhanced to handle multiple EC2's
2. REST API to support Instance creation, start, stop, terminate etc 


## PART 2

### Problem statement 2:
   Using any Python libraries of your choice (such as Beautiful Soup, Scrapy, or Requests), write a program to scrape data from a website of your choosing. The data you extract can be related to products, articles, or any other relevant content available on the website. You are required to:
   Choose a website for scraping.
   Extract specific information from the website's pages, such as product details, article titles, or any other relevant data.
   Store the scraped data in a structured format (e.g., CSV, JSON) for further analysis.

## Pre-requisites:
Start Webscrapping 
  1. preinstall requirments 
     pip install requests bs4
  2. set websites urls
  3. set xpath templates 
  4. run python webscrapper.py
  5. output will be saved in output.json file