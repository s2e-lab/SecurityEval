from canvasapi import Canvas


def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equals to the id specified as parameter.
    '''
    url = 'https://canvas.instructure.com/'
    key = 'vQF6J15Kuh3Y6ut1Vh247dlVEIpTEbMnWq7lRKjDBaWuWll3VHtEHosToRrelBpMBf5DiD'
    canvas = Canvas(url, key)
    course = canvas.get_course(course_id)
    return [x for x in course.get_assignments()]


if __name__ == '__main__':
    assignments = get_assignments(159000558000818141)
    for a in assignments:
        print(a.name, a.points_possible)