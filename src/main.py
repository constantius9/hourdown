#!/usr/bin/env python

"""A simple tool asking for a time and date and counting down to that moment.

Currently works in interactive mode only.
"""

import datetime as dt
import json
import sys


"""Format string of datetime"""
format_str = "%d.%m.%Y %H:%M"



def set_date_time():
    """Returns the datetime object obtained from interactive user input."""
    date_time_str = raw_input(
        'Enter time and date in the format {0}: '.format(format_str))
    date_time = dt.datetime.strptime(date_time_str, format_str)
    return date_time


def add_project(projects):
    """Asks user for project name and adds it to tracking dictionary."""
    project_name = raw_input('Enter project name: ')
    try:
        spent_time = projects[project_name]
        print 'You spent {0} hours on {1}. You can journal more time.'
    except KeyError:
        projects[project_name] = 0
    
    return projects


def journal_spending(projects):
    """Log time spending on project.

    Asks user for a number of project and for time (in hours) spent on it
    and adds it.
    """
    di = dict()
    for i, item in enumerate(projects.keys()):
        di[i] = item
        print i, '- ', item
    choice = raw_input('Choose the project: ')
    amount = raw_input('How much time did you spend? ')
    try:
        project = di[int(choice)]
    except (ValueError, KeyError):
        print 'Incorrect number of project.'

    try:
        projects[project] += int(amount)
    except KeyError:
        print "There's no such project. Add it or try again."
    except ValueError:
        print 'Incorrect amount. Try again.'

    return projects


def save_everything(**kwargs):
    """Saves projects and date."""
    fp = open('projects.json', 'w')
    projects = kwargs['projects']
    json.dump(projects, fp)
    fp.close()

    date_time = kwargs['date_time']
    if date_time:
        fp = open('date_time.json', 'w')
        date_time_str = dt.datetime.strftime(date_time, format_str)
        json.dump(date_time_str, fp)
        fp.close()
    print 'Saved OK.'


def load_everything():
    """Loads projects and date and returns them."""
    fp = None
    try:
        fp = open('projects.json', 'r')
        projects = json.load(fp)
    except (IOError, ValueError):
        projects = dict()
    finally:
        if fp:
            fp.close()

    try:
        fp = open('date_time.json', 'r')
        date_time_str = json.load(fp)
        date_time = dt.datetime.strptime(date_time_str, format_str)
        seconds_left = (date_time - dt.datetime.now()).total_seconds()
        hours_left = round(seconds_left / 3600, 1)
    except (IOError, ValueError):
        date_time = None
        hours_left = 0
    finally:
        if fp:
            fp.close()
    return projects, date_time, hours_left


def show_journal(projects):
    """Show current time spendings."""
    for project, amount in projects.items():
        print '{0}: {1} hours.'.format(project, amount)


def main():
    """Main loop"""

    projects, date_time, hours_left = load_everything()
    while True:
        print """You have {0} hours left. Set date is {1}.
        Choose action:
        1 - Set time/date
        2 - Add a project
        3 - Journal time spending
        4 - Show journal
        5 - Exit
        """.format(hours_left, date_time)
        choice = raw_input('Choose and action: ')
        if choice == '1':
            date_time = set_date_time()
        elif choice == '2':
            projects = add_project(projects)
        elif choice == '3':
            projects = journal_spending(projects)
        elif choice == '4':
            show_journal(projects)
        elif choice == '5':
            save_everything(projects=projects, date_time=date_time)
            print 'Bye.'
            sys.exit(0)
        else:
            print 'Incorrect choice. Please try again.'

main()
