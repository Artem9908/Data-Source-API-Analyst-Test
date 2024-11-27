# Data Source API Analyst Test

## Introduction

This repository contains my submission for the Data Source API Analyst assignment. The goal is to demonstrate proficiency in working with APIs, data extraction, and troubleshooting by interacting with the GitHub API.

## Client Requirements

The client requires the following functionality:

1. **Search for public repositories** based on specific keywords or topics.
2. **Retrieve commit history** for any repository to analyze changes over time.
3. **Access repository contents** to review specific files or the structure of a repository.
4. Ensure the solution handles **pagination**, **rate limits**, and **error scenarios** for smooth and efficient data extraction.

This project addresses these requirements by implementing secure authentication, API interaction, and validation using Python and Google Colab.

---

## Approach to Client Requirements

To meet the client's needs, the following approach was taken:

1. **Research GitHub API**:  
   - Researched API endpoints for searching repositories, listing commits, and retrieving repository contents.  
   - Analyzed rate limits and implemented handling for pagination and errors.

2. **Secure Authentication**:  
   - Used a Personal Access Token (PAT) to ensure secure and reliable authentication for API requests.

3. **Implementation**:  
   - Designed modular Python functions to handle specific tasks like fetching data, managing rate limits, and processing paginated responses.

4. **Validation**:  
   - Tested each function using a Google Colab notebook and printed outputs for verification.

---

## Repository Structure

The repository is organized as follows:

