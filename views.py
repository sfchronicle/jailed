from flask import render_template, redirect, url_for, request

from app import app, db, freezer
from models import *


# Project Title
app.config['PROJ_TITLE'] = ''

# Site Path/Slug
app.config['PATH'] = 'captive-lives'

# Project Category for Omniture 
app.config['CATEGORY'] = 'Metro'

# Project Hashtag
app.config['HASHTAG'] = 'CaptiveLives'

"""
slug completes:
- twitter:url
- og:image/Facebook image preview
- Twitter/Facebook share url
- url for email body

title:
- Page title
- og:title/Facebook headline
- email subject
- twitter:title

description:
- meta description
- og:description/Facebook description

twitter_text:
- text that appears on tweet

"""

@app.route('/')
def index():
    return render_template('index.html',
    	slug='',
    	title="Children of inmates face long odds of success",
    	description="Captive Lives: Studies show the needs of some 10 million children with incarcerated parents have been largely ignored. But slowly, efforts to help them are growing.",
    	twitter_text="Special report: Children of incarcerated parents face long odds of success.")

@app.route('/visits/')
def visits():
    return render_template('visits.html',
    	slug='visits',
    	title="SF jail helps families bond behind bars",
    	description="Captive Lives: While many jails reduce or eliminate in-person visits, San Francisco's works to bring inmates and their children together.",
    	twitter_text="SF jail works to help families bond behind bars.")
