#!/usr/bin/env python3

class Solution(object):
    def hasLoop(self, course, course_to_prereq):
        """
        Followers:
           Awndre
           cptwalrus
           alvin5How
           TheldOfAlan
           SimoncitoOwU
           andre_santoz
        """
        to_visit = [course]
        seen = set()

        while to_visit:
            print(seen)
            # Get the course to visit
            current = to_visit.pop()

            if current in seen:
                print("Encountered a seen node" + str(current))
                return True
            else:
                seen.add(current)

            # Queue up the dependencies
            for dep in course_to_prereq[current]:
                if dep not in to_visit:
                    to_visit.append(dep)

        return False

    def canFinish(self, numCourses, prerequisites):
        """
        Followers
           nillhiam
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        course_to_prereq = {}

        for course in range(numCourses):
            course_to_prereq[course] = []

        for pair in prerequisites:
            course_to_prereq[pair[0]].append(pair[1])

        # Walk the depcourseendency path
        for course in course_to_prereq:
            loop = self.hasLoop(course, course_to_prereq)

            if loop:
                return False

        return True
