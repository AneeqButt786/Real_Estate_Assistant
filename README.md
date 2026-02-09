# Multi-Agent Real Estate Assistant

## Overview

Orchestrates three specialized AI agents: Mortgage Eligibility Checker, Property Recommender, Multilingual Buyer Support. Routes requests to the appropriate specialist based on user intent.

## Features

- Mortgage eligibility evaluation
- Property recommendations (location, budget, type)
- Multilingual support for translations

## Tech Stack

Python 3.12+, OpenAI Agents SDK, Chainlit, python-dotenv

## Setup

1. cd Real_Estate_Assistant
2. pip install -r requirements.txt
3. Copy .env.example to .env and set OPENAI_API_KEY

## Run Commands

chainlit run app.py
