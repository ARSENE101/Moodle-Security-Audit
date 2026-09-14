# Moodle Security Audit — SecChkLab Research

> "Security-minded builder who finds and fixes what others miss."

## What Is This?

This repository documents an ongoing security audit of Moodle 5.1.6+ — 
one of the most widely deployed open source Learning Management Systems 
in the world, used by universities, schools and corporations across 190+ countries.

The goal is not to break things for sport. The goal is to answer one question:

**How hackproof is the system millions of students trust with their grades?**

All testing is performed on a locally hosted sandbox environment (SecChkLab) 
running Moodle 5.1.6+ on XAMPP. No real systems, no real users, no real data.

## Researcher Background

Fullstack developer with a background in Information Technology and Security. 
Currently studying Data Science. This audit sits at the intersection of both worlds — 
building things and understanding how they break.

## Environment

| Component | Version |
|---|---|
| Moodle | 5.1.6+ |
| PHP | 8.2.12 |
| MariaDB | 10.4.32 |
| OS | Windows 11 |
| Web Server | Apache 2.4.58 |

## Tools

| Tool | Purpose |
|---|---|
| Burp Suite Community | HTTP interception and manipulation |
| OWASP ZAP | Automated vulnerability scanning |
| Semgrep | Static analysis of PHP source code |
| SQLmap | SQL injection detection |
| Snyk | Dependency vulnerability scanning |
| Nmap | Network reconnaissance |
| Custom Python scripts | Targeted exploit testing |

## Findings

| ID | Attack Vector | Status | Severity |
|---|---|---|---|
| SCL-001 | Session Analysis | 🔄 In Progress | TBD |
| SCL-002 | IDOR | ⏳ Planned | TBD |
| SCL-003 | SQL Injection | ⏳ Planned | TBD |
| SCL-004 | XSS | ⏳ Planned | TBD |
| SCL-005 | File Upload Exploitation | ⏳ Planned | TBD |
| SCL-006 | CSRF | ⏳ Planned | TBD |
| SCL-007 | Quiz Integrity Analysis | ⏳ Planned | TBD |

## Repository Structure
