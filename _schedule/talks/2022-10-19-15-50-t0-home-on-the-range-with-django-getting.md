---
abstract: "Building complex range-based queries with individual `start` and `end`
  fields is inconvenient, inefficient, and does not make use of the expressiveness
  available in Postgres' range fields - but working with ranges is a topic that is
  often glossed over.\r\n\r\nWe will work through examples in a project demonstrating
  the way to use and query with ranges. The audience will receive link to the example
  code and a cheatsheet for working with ranges."
accepted: true
category: talks
difficulty: Intermediate
date: 2022-10-19 15:50:00-07:00
end_date: 2022-10-19 16:35:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fjack-linke%252F/opengraph/
layout: session-details
permalink: /talks/home-on-the-range-with-django-getting/
presenter_slugs:
- jack-linke
published: true
room: Salon A-E
schedule_layout: full
sitemap: true
slug: home-on-the-range-with-django-getting-comfortable-with-ranges-and-range-fields
summary: ''
tags: null
title: Home on the range with Django - getting comfortable with ranges and range fields
track: t0
---

## Objectives

Audience members will learn why ranges are more useful than distinct start and end values, will become familiar with range-based terminology, will have the opportunity to see a number of approaches to using and querying with ranges, and will have resources for further reading and learning. These resources will include a link to a GitHub repository containing the examples from the talk, additional examples, and a cheatsheet for working with ranges.

## Outline

The naive approach to ranges (2 min)

- Using separate start and stop model fields
- Querying with start and stop values
- Quickly gets complicated

Range visualization for concrete understanding (3 min)

- Terminology
    - Inclusive vs Exclusive
    - Overlap
    - Contains
    - Contained By
    - Comparisons (fully_lt, fully_gt, etc)

[diagram](https://lucid.app/publicSegments/view/19424336-bc96-4a42-a5cb-a8ff04928caf/image.png)

A before-and-after look at the models (5 min)

The example project is a Swimming Pool Resource Scheduler that makes heavy use of ranges (probably more than would be used in most projects) in order to demonstrate various approaches. The model layout can be visualized in the following diagrams:

![database schema simple](https://raw.githubusercontent.com/jacklinke/home-on-the-range-with-django/master/presentation/img/erd_light.png)

![database schema detailed](https://raw.githubusercontent.com/jacklinke/home-on-the-range-with-django/master/presentation/img/erd.png)

We will look at the models before and after using range fields.

The initial (stripped down) models.py file using distinct fields for lower and upper values is:

    class Pool(models.Model):
        """An instance of a Pool. Multiple pools may exist within the municipality"""

        name = models.CharField(_("Pool Name"), max_length=100)
        address = models.TextField(_("Address"))
        depth_minimum = models.IntegerField(_("Depth Minimum"), help_text=_("What is the depth in feet of the shallow end of this pool?"))
        depth_maximum = models.IntegerField(_("Depth Maximum"), help_text=_("What is the depth in feet of the deep end of this pool?"))
        business_hours_start = models.IntegerField(_("Business Hours Start Hour"), default=9)
        business_hours_end = models.IntegerField(_("Business Hours End Hour"), default=17)

        class Meta:
            verbose_name = _("Pool")
            verbose_name_plural = _("Pools")


    class Closure(models.Model):
        """A way of recording dates that a pool is closed"""

        pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name="closures")
        start_date = models.DateField(_("Pool Closure Start Date"))
        end_date = models.DateField(_("Pool Closure End Date"))
        reason = models.TextField(_("Closure Reason"))

        class Meta:
            verbose_name = _("Closure")
            verbose_name_plural = _("Closures")


    class Lane(models.Model):
        """Each pool may have multiple lanes, each of which can be reserved by multiple people"""

        name = models.CharField(_("Lane Name"), max_length=50)
        pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name="lanes")
        max_swimmers = models.PositiveSmallIntegerField(_("Maximum Swimmers"), )
        per_hour_cost = models.DecimalField(_("Per-Hour Cost"), max_digits=5, decimal_places=2)

        class Meta:
            verbose_name = _("Lane")
            verbose_name_plural = _("Lanes")


    class Locker(models.Model):
        """Each pool may have multiple lockers, each of which can be reserved by only one person at a time"""

        # Using CharField, because sometimes locker number might be "A23" or "56-B"
        number = models.CharField(_("Locker Number"), max_length=20)
        pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name="lockers")
        per_hour_cost = models.DecimalField(_("Per-Hour Cost"), max_digits=5, decimal_places=2)

        class Meta:
            verbose_name = _("Locker")
            verbose_name_plural = _("Lockers")


    class LaneReservation(models.Model):
        """A lane reservations defines a set of users, a period of time, and a pool lane"""

        users = models.ManyToManyField(User, on_delete=models.CASCADE, related_name="lane_reservations")
        lane = models.ForeignKey(Lane, on_delete=models.CASCADE, related_name="lane_reservations")
        period_start = models.DateTimeField(_("Reservation Period Start"))
        period_end = models.DateTimeField(_("Reservation Period End"))
        actual_start = models.DateTimeField(_("Actual Usage Period Start"))
        actual_end = models.DateTimeField(_("Actual Usage Period End"))
        cancelled = models.DateTimeField(_("Reservation is Cancelled"), null=True)

        class Meta:
            verbose_name = _("Lane Reservation")
            verbose_name_plural = _("Lane Reservations")


    class LockerReservation(models.Model):
        """A locker reservation defines a user, a period of time, and a pool locker"""

        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="locker_reservations")
        locker = models.ForeignKey(Locker, on_delete=models.CASCADE, related_name="locker_reservations")
        period_start = models.DateTimeField(_("Reservation Period Start"))
        period_end = models.DateTimeField(_("Reservation Period End"))
        actual_start = models.DateTimeField(_("Actual Usage Period Start"))
        actual_end = models.DateTimeField(_("Actual Usage Period End"))
        cancelled = models.DateTimeField(_("Reservation is Cancelled"), null=True)

        class Meta:
            verbose_name = _("Locker Reservation")
            verbose_name_plural = _("Locker Reservations")


The final (stripped down) models.py with range fields is:

    class Pool(models.Model):
        """An instance of a Pool. Multiple pools may exist within the municipality"""

        name = models.CharField(_("Pool Name"), max_length=100)
        address = models.TextField(_("Address"))
        depth_range = IntegerRangeField(
            _("Depth Range"),
            help_text=_("What is the range in feet for the depth of this pool (shallow to deep)?"),
        )
        business_hours = IntegerRangeField(_("Business Hours"), default=(9, 17))

        class Meta:
            verbose_name = _("Pool")
            verbose_name_plural = _("Pools")


    class Closure(models.Model):
        """A way of recording dates that a pool is closed"""

        pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name="closures")
        dates = DateRangeField(_("Pool Closure Dates"))
        reason = models.TextField(_("Closure Reason"))

        class Meta:
            verbose_name = _("Closure")
            verbose_name_plural = _("Closures")


    class Lane(models.Model):
        """Each pool may have multiple lanes, each of which can be reserved by multiple people"""

        name = models.CharField(_("Lane Name"), max_length=50)
        pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name="lanes")
        max_swimmers = models.PositiveSmallIntegerField(
            _("Maximum Swimmers"),
        )
        per_hour_cost = models.DecimalField(_("Per-Hour Cost"), max_digits=5, decimal_places=2)

        class Meta:
            verbose_name = _("Lane")
            verbose_name_plural = _("Lanes")


    class Locker(models.Model):
        """Each pool may have multiple lockers, each of which can be reserved by only one person at a time"""

        # Using CharField, because sometimes locker number might be "A23" or "56-B"
        number = models.CharField(_("Locker Number"), max_length=20)
        pool = models.ForeignKey(Pool, on_delete=models.CASCADE, related_name="lockers")
        per_hour_cost = models.DecimalField(_("Per-Hour Cost"), max_digits=5, decimal_places=2)

        class Meta:
            verbose_name = _("Locker")
            verbose_name_plural = _("Lockers")


    class LaneReservation(models.Model):
        """A lane reservations defines a set of users, a period of time, and a pool lane"""

        users = models.ManyToManyField(User, related_name="lane_reservations")
        lane = models.ForeignKey(Lane, on_delete=models.CASCADE, related_name="lane_reservations")
        period = DateTimeRangeField(
            _("Reservation Period"),
            validators=[
                DateTimeRangeLowerMinuteValidator(0, 30),
                DateTimeRangeUpperMinuteValidator(0, 30),
                validate_zeroed_dt_sec_microsec,
            ],
        )
        actual = DateTimeRangeField(_("Actual Usage Period"), default=(None, None))
        cancelled = models.DateTimeField(_("Reservation is Cancelled"), null=True)

        class Meta:
            verbose_name = _("Lane Reservation")
            verbose_name_plural = _("Lane Reservations")


    class LockerReservation(models.Model):
        """A locker reservation defines a user, a period of time, and a pool locker"""

        user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="locker_reservations")
        locker = models.ForeignKey(Locker, on_delete=models.CASCADE, related_name="locker_reservations")
        period = DateTimeRangeField(_("Reservation Period"))
        actual = DateTimeRangeField(_("Actual Usage Period"), default=(None, None))
        cancelled = models.DateTimeField(_("Reservation is Cancelled"), null=True)

        class Meta:
            verbose_name = _("Locker Reservation")
            verbose_name_plural = _("Locker Reservations")


Example Project Walkthrough (30 min)

The models in this project will be used to demonstrate a variety of tasks in django views, including a number of the following:

- Set constraints for the various range fields
- Access the lower and upper values of a range fields in views and templates
- Get reservations that start at a specific datetime
- Get reservations that overlap with a single date
- Get reservations that overlap with a range
- Check if a reservations start datetime matches any value in a list
- Get reservations with a start or end that falls between two dates
- Get reservations whose lower/upper date falls within a range
- Get reservations for the current week
- Get reservations that end before now
- Get reservations that start on or before September
- Get reservations that end in May OR September
- Given a list of datetimes, get all reservations that overlap with the items in the list
- Order the queryset by lower. If two reservations have the same lower, also sort by upper. (This is the default behavior in django)
- Get reservations with an overdue start (the reservation time started, but the party has not yet checked in)
- Get reservations with an overdue end (the reservation time ended, but the party has not checked out)
- Given a datetime (and other filtering criteria), get the count of reservations at that moment
- For a particular Lane (or set of Lanes), get the aggregate count/sum of reservations during each hour of a daterange
- Sum of all swimmers at a given moment
- Sum of all swimmers at each time period change
    - For a particular Lane or entire Pool, get the time and value of all changes in number of swimmers
    - Given a start time stop time and a Lane, return a queryset of the swimmers at each 15 minute increment.
- Calculated overall usage (number of swimmers * time interval = swimmer hours) within a time range
    - Total usage by day/week/month by Pool/Lane
    - Usage by range:  Given a list of ranges, calculate the usage during each range
- Prevent overlapping reservation_period for the same resource (here, it's Rooms), where the reservation has not already been cancelled
- Add validation to model field for minimum and maximum datetimes
- Aggregate the minimum Lower and maximum Upper reservations dates for all reservations in a queryset
- Similarly, annotate the minimum Lower and maximum Lower reservations dates for all reservations in a queryset
- Assuming each reservation is associated with a Resource, annotate Resources with the most recently ending reservation (similar for most recent starting or longest-ago starting/ending reservation)
- Multiple ways of saving a model instance with DateTimeRangeField

*Note: Those examples above which we are unable to cover during the talk can be viewed in the example project GitHub repo which will be provided for the talk*

Resources (5 min)

- [psycopg2.extras](https://www.psycopg.org/docs/extras.html)
- [This talk & Example Project](https://github.com/jacklinke/home-on-the-range-with-django)
- [django-range-merge](https://github.com/jacklinke/django-range-merge/) - use `range_merge` aggregate with Django
- [django-generate-series](https://github.com/jacklinke/django-generate-series) - create sequences with Django's ORM
