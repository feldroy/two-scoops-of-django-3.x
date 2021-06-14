# Two Scoops of Django Changelog

This lists many, but not all the changes between TSD 1.11 and TSD 3.x.

# Updates until 2021-06-14

## General

- Changed our names to Daniel and Audrey Roy Greenfeld
- Grammar and spelling corrections

## PAAS

- Add Digital Ocean App Platform
- Be honest about Heroku so users see it with open eyes

## Debugging

- Brought chapter in
- Removed link to ancient blog post
- Added mention of `breakpoint()`

## Where and how to ask for help

- Added section on the official forums 
- Added Libera Chat IRC
- Linkified a few items to make things easier on readers


---

# Updates until 2021-01-27

## General

- Converted all docs links to point to Django 3.2

## Coding Style

- Changed `isort` tip box to a package tip

## Graphql

- Removed trygql.com 

## Security

- Mention OTPs in 2FA

## Logging

- Chapter has been revised and is available for readers!
- Added warning box about using f-strings with loggers
- Removed Python 2 mention

## Packages

- Added aldjemy
- Added django-stronghold
- Added environment variable section with multiple packages

---

# Updates until 2020-12-02

## General Changes

- Added Authorized Vendors and Distributors informations
- Various spelling and grammar corrections
- Removed last python 2.7-style usages of `super()` 

## Database Queries

- Use `breakpoint()` instead of importing pdb

## FBVs

- Added Luke Plant's "Django Views the Right Way"

## User models

- Corrected wrong parent class




---

# Updates until 2020-07-27

## General Changes

- Grammar fixes

## Settings and Requirements

- Add missing `ql` to ORM engine

## Models and Queries

- JSONField is now for all database types

## Templates

- Removed GitHub's 404 page from the list of being self-contained HTML, CSS, and JS 

## Third-party packages

- Fix code highlighting

## Security

- Fix borked link

## Appendix: Resources

- Added testdriven.io

---

# Updates until 2020-07-09

## General Changes

- Moved first reference to indexes from chapter 6 to chapter 7 
- The inevitable grammar corrections

## Settings and Requirements

- Added `.zshrc` for configuring environment variables

## Best Practices for FBVs

- Made use of `functools.wraps` consistent

## Best Practices for CBVs

- Mixins should not inherit from `object`, that is a holdover from Python 2.7 

## Finding and Reducing bottlenecks

- Reviewed content in full and added to the book

## Third-Party Packages

- Add instruction for git tagging project releases

## Async Task Queues

- Started on reviewing content

## Internationalization

- All pages updated for Django 3.x and Python 3.8

----

# Updates until 2020-07-07

This update adds 15 new pages to Two Scoops of Django, bringing us up to 461! 

## General Changes

- Yet more grammar fixes

## Javascript

- Added quote by DHH about the state of JavaScript in 2020

## Admin chapter

- Removed mention of long deprecated `allow_tags` property descriptor
- Add warning box to use `format_html` function for enhancing security

## User model chapter

- Added multiple user models
- Demonstration of proxy models

## Package Used in this Book Appendix

- Out of "being updated mode"
- Reviewed all packages
- Added new packages
- Removal of deprecated packages

# Updates until 2020-06-16

## General Changes

- Revised and legible bad code examples!
- More grammar fixes
- All use of `reverse()` function now include URL namespaces

## Coding Standards

- Change focus of `Use Explicit Relative Imports` to `Understand Explicit Relative Imports` and removed `Implicit Relative Imports`

## Chapter - Settings and Requirements

- Removed tipbox for `Using django-admin Instead of manage.py`. This advice has been removed from the Django docs

## Chapter - Database Model Best Practices

- Removed link to blog post that used to describe how to use `DateTimeField` with logical deletes 

## Chapter - Building APIs with Django Rest Framework

- Added references to OpenAPI and tools
- Mentioned using vanilla Django for creating APIs
- Converted package tip for django-tastypie and django-jsonview into a new section for DRF alternatives
- Added trailing 'r' on `rest_framework.permissions.IsAdminUser`

## Chapter - JavaScript

- Changed section "Popular JavaScript Frameworks" to "Popular JavaScript Approaches"
- Added description list for serverside rendering of templates
- Included alpine.js and turbolinks
- Added section on JSON encoding for data rendered in the template but consumed by JavaScript


## Chapter - Security
 
- Corrected typo so PHI is now the acronym for `Protected Health Information`


## Acknowledgements

- Added Bio for Haris Ibrahim

----

# Updates until 2020-06-05

- Included forward by [Will Vincent](https://learndjango.com)
- Began expanding the async views chapter
- Made pipenv active again now that they had a formal release
- Added first half of Appendix A: Chapters mentioned in this book

----

# Updates until 2020-05-29

## General

- Model mommy is now model bakery

## Chapter - Models

- Table layout corrections in chapter 6
- `BooleanField(null=True)` recommended instead of `NullBooleanField`

## Chapter - FBVs

- Corrected return type for `check_sprinkles` function


## Chapter - Django REST Framework

- Link to sources on how to rate limit
- Removed material on coreapi because that project has been replaced by openapi

## Chapter - Documentation

- Added myst for rendering markdown in Sphinx

## Chapter - User Model

- Mention that django-authtools doesn't yet work for Django 3

## Chapter - Security

- Ponycheckup is no more. Many thanks to Sasha Romijn for providing such an invaluable
- Added PyCharm Django Security

----

# Updates until 2020-05-19

## General

- More grammar!
- Consistent case for `URLConfs`

## Chapter - Environment Setup

- Replaced "typing" with "type casting", the latter is more explicit

## Chapter - Project Setup

- Added link to Cookiecutter docs

## Chapter - Databases

- Took out the long removed `use_for_related_fields` attribute from manager code example

## Chapter - Templates

- Fix LaTeX escape failure

## Chapter - Security

- Removed Pony Checkup

## Chapter - PaaS

- Added Zappa as an option
- Took away statement that Elastic Beanstalk was on mod_wsgi and hence no channels


## Chapter - CI

 - Added MacOS to Azure Pipelines in feature table

## Chapter - Debugging

- Updated IDE preferences


----

# Updates until 2020-05-13

## General changes

- General grammar and spelling improvements
- Updated Django version to 3.x
- Updated Python version to Python 3.8/3.9
- Removed Appendix giving advice on upgrading from Python 2 to 3
- Remove mention of Mercurial. 
- Changed `README.rst` to `README.md`
- `OS X` is now `Mac`
- References to `django-admin.py` replace with `django-admin`
- Changed pypi.python.org to pypi.org
- Removed last vestige of `Twitter Bootstrap` in favor of `Bootstrap`
- Due to problems with a number of PDF renderers on the Mac URL escaping '#' incorrectly, URLs with '#" are forwarded through our `feld.to` link shortener. The reader sees the correct URL, but clicking links takes them through feld.to.
- "Don't Do This!!" code examples have new style
- Use "README file" instead of README.md or README.rst
- Added footer to instruct users where to submit issues
- Added warnings at the front of chapters which won't be published  

## Book crafting process

- LaTeX datestamping now automated. Why didn't we do this years ago?
- Added placeins LaTex package to the `requirements-latex.yml` file.
- Updated the book build instructions.


## Note from the authors

- Added Sentry
- Remove Pinterest from company list

## Introduction

- Removed apocryphal statement by Leonardo Da Vinci
-

## Chapter - Coding Style

- Added quote from "Structure and Interpretation of Computer Programs"
- Removed duplicate URL
- Added black
- Added wemake-python-styleguide
- Added isort for ordering imports
- Change JS coding style standard URL to github.com/standard/standard


## Chapter - Environment Setup

- Added mention of poetry, conda, and pipenv
- Git is now the only tool for version control
- Added Docker to summary
- Warn that pip doesn't necessarily come with Python installations on Linux distros
- Removed mention of `easy_install`

## Chapter - Settings and Requirements

- Use of `json.load` instead of `json.loads`

## Chapter - Django Project Layout

- Added "Don't Upload Environment Directories To Open Source" warning box
- Now calls runserver with the correct settings argument
- Removed wemake-python-styleguide as a recommendation for Django projects

## Chapter - Fundamentals of App Design

- Removed extra `models.py` from app layout example
- Added Tom Christie's article for refuting the service layer approach to organizing business logic

## Chapter - Database/Model Best Practices

- Rewrote the enumeration types segment as Django now includes them as part of core
- Mention `BooleanField` has default of `blank=True`
- Added Haki Benita's excellent article on bullet proofing Django models
- `null=True` for `ManyToManyField` is now recommended against as it raises a check warning
- Custom default Model Managers are no longer forbidden, just an advanced technique to be wary of 
- Removed mention of South as a competing migrations system

## Chapter - More Forms

- Added links to more useful references, removed some outdated ones
- Switch from JWT library to dj-rest-auth for authentication
- Remove link to csrf docs



## Chapter - Function- and Class-Based Views

- Removed historical note from Django 1.5 era about not removing function-based views
- Now using `path()` url route declarations instead of the old `url()` function

## Chapter - Function-Based Views

- Added type annotations to views

## Chapter - Class-Based Views

- Added type annotations to views
- Flavor model now uses enumeration choices
- Advice on Mixins inheritance clarified for Python 3
- Added Serafeim Papastefanos' excellent CBV post to the resources section
- Added links to more useful references, removed some outdated ones

## Chapter - Asynchronous Views

- Added stub chapter

## Chapter - Templates

- Made Python code example more concise
- HTML/DTL examples now use 2-space examples
- Removed Python 2 era mention that `super()` accepts arguments

## Chapter - Template Tags

- Marked django-wysiwyg as deprecated

## Chapter - Jinja2

- Removed statement about maturity of Jinja2 in Django, it's mature now
- Switched to 2 character tabs

## Chapter - Django REST Framework

- Make more explicit that routers go into `urls.py` modules
- Mention Randall Degges advice about Usage-Based Plans
- Mention DRF support for different versioning schemas and link to docs
- Fixed link to Classy DRF site

## Chapter - Building GraphQL APIs with Graphene

- New chapter!

## Chapter - JavaScript and Django

- Changed the name from **Consuming REST APIs** to **JavaScript and Django**
- Restructured to be about JavaScript in the Django domain, with REST APIs being a topic
- Added Vanilla JS as progressive option
- Moved JQuery to legacy. While, JQuery isn't legacy yet it is on the way to become so
- Rewrote strengthening JavaScript skills
- Removed section on `CSRF_COOKIE_HTTPONLY` as it doesn't make Django any more secure, just satisfies some security auditors. 
- No longer recommend JWT as an authentication method
- No longer excuse turning off CSRF to support JWT


## Chapter - FrankenDjango

- Added https://daniel.feldroy.com/when-to-use-mongodb-with-django.html
- Made Kevin Systrom a co-founder of Instagram instead of CEO

## Chapter - Django Admin

- Removed `python_2_unicode_compatible` from the example model

## Chapter - Third Party Packages

- Switched from cookiecutter-pypackage to cookiecutter-pylibrary
- Switched from `.txt` and `.rst` doc extensions to `.md`
- Removed link to Jeff Knupp's excellent article on open sourcing projects as it is unfortunately out of date
- For Twine, replaced "non-ssh" with "non-secure"

## Chapter - Bottlenecks

- Replaced django-johnnycache and django-cache-machine with django-cacheops
- Removed yslow
- Change link to Lanyrd search for conference talks to YouTube
- Removed link to David Cramer's now defunct blog
- Reference Andrew Brook's excellent book, [The Temple of Django Database Performance](https://spellbookpress.com/books/temple-of-django-database-performance/) 

## Chapter - Signals

- Added `on_delete` argument to foreign key example

## Chapter - User Model

- Added methods for differint user types

## Chapter - Testing

- Added assertRaisesMessage
- Added assertInHTML
- Added assertURLEqual
- Removed the defunct requestb.in
- Added Postman
- Added interrogate

## Chapter - Documentation

- Removed advising the global installation of Sphinx
- Switch to recommending Markdown over reStructuredText
- Provide reStructuredText as the older alternative
- Remove segment on converting reStructuredText to Markdown
- Added tipbox for other markdown doc site renderers
- Added interrogate

## Chapter - Bottlenecks

- Changed `ATOMIC_REQUESTS` to `False`

## Chapter - Security

_Many thanks to our incredibly diligent security reviewers!_

- Fixed borked link to Security Failures Chapter
- Added warningbox that Let's Encrypt is the most secure option (in progress of being rewritten)
- Added warningbox that not having HTTPS/SSL is inexescusable in 2020
- CSP report submitting is optional per the spec
- Made call for SSL very strident
- Added cloudflare as a free option for SSL
- Mentioned big cloud providers for SSL options
- Remove Sasha Romijn's Pony Checkup. Wonderful tool and we thank her for all those years of supporting Django.
- ALLOWED_HOSTS and DEBUG=True now throws 400 errors
- `IceCreamPayment` model's UUID switched from `db_index=True` to `unique=True`
- Discussion of `SECRET_KEY` now states what can actually occur
- Added section on not storing unnecessary data which includes credit card, PII, and PHI data
- Added missing 'N' to the word 'ever'
- Added section on upgrading password hasher to Argon2 
- Added section on using SRI when loading static assets from external CDNs


## Chapter - Utilities

- Removed `django.utils.six`, we're in Python 3 land now!

## Chapter - Deployment

- Removed mention of `mod_python`
- Removed reference to very old versions of `mod_wsgi` (3.3 or less)
- Removed `--no-site-packages` from virtualenv

## Chapter - Continuous Integration

- Removed Python version column from CI-as-a-Service table and replaced with ``operating systems''
- Added Circle CI, GitHub Actions, Azure Pipelines, and Drone

## Chapter - Debugging

- Removed defunct django-gargoyle package and added django-flags as the plucky newcomer


## Appendix - Packages

- Separated Dependency Management out of Core into own category
- Added MkDocs
- Added markdown as option to Sphinx
- Fixed link to Channels

## Appendix - i18n

- Replace `string_concat` with `format_lazy`

## Appendix - Additional resources

- Added Simple Better Than Complex, apologies to Vitor we didn't include it at launch
- Added classy Django forms
- Removed links to our own pages of additional resources


## Appendix - Handling Security Failures

- Removed django-maintenaincemode as it hasn't been updated yet to Django 3
- Removed django-maintenancemode-2 as it could create a false sense of security. Per the security reviewer: "that's not a solution, because if your Django installation is compromised, attackers can turn the maintenance mode off again."

# Appendix - Security Settings

- Made SMTP as SSL mandatory
- ALLOWED_HOSTS and DEBUG=True now throws CommandError

# Appendix - Websockets with Channels

- Removed "Channels Works Better With Python 3.6+". Django 3 makes Python 3.6 or higher mandatory
- Fix broken link to Channels' testing documentation
