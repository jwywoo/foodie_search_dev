from django.db import models


class Food(models.Model):
    english_name = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)
    UNDECIDED = 'UD'
    # country choices
    KOREA = 'KR'
    JAPAN = 'JP'
    COUNTRY_CHOICES = [
        (KOREA, 'Korean'),
        (JAPAN, 'Japanese'),
        (UNDECIDED, 'Not sure')
    ]
    country = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICES,
        default=UNDECIDED,
    )
    # color choices
    YELLOW = 'YL'
    RED = 'RD'
    BROWN = 'BR'
    BLACK = 'BL'
    COLOR_CHOICES = [
        (YELLOW, 'Yellow'),
        (RED, 'Red'),
        (BROWN, 'Brown'),
        (BLACK, 'Black'),
        (UNDECIDED, 'Not sure')
    ]
    color = models.CharField(
        max_length=2,
        choices=COLOR_CHOICES,
        default=UNDECIDED,
    )
    # taste choices
    SWEET = 'SW'
    SPICY = 'SC'
    SOUR = 'SR'
    SALTY = 'SL'
    BITTER = 'BT'
    TASTE_CHOICES = [
        (SWEET, 'Sweet'),
        (SPICY, 'Spicy'),
        (SOUR, 'Sour'),
        (SALTY, 'Salty'),
        (BITTER, 'Bitter'),
        (UNDECIDED, 'Not sure'),
    ]
    taste = models.CharField(
        max_length=2,
        choices=TASTE_CHOICES,
        default=UNDECIDED,
    )
    # protein choices
    BEEF = 'BF'
    PORK = 'PR'
    FISH = 'FS'
    SHELLFISH = 'SF'
    CHICKEN = 'CK'
    NOMEAT = 'NM'
    VEGETARIAN = 'VG'
    PROTEIN_CHOICES = [
        (BEEF, 'Beef'),
        (PORK, 'Pork'),
        (SHELLFISH, 'Shell fish'),
        (FISH, 'Fish'),
        (VEGETARIAN, 'Vegetarian'),
        (CHICKEN, 'Chicken'),
        (NOMEAT, 'No protein'),
        (UNDECIDED, 'Not sure'),
    ]
    protein = models.CharField(
        max_length=2,
        choices=PROTEIN_CHOICES,
        default=UNDECIDED,
    )
    # type choices (how the food being prepared)
    BOILED = 'BD'
    FRIED = 'FR'
    STEAMED = 'ST'
    BAKED = 'BE'
    BARBEQUE = 'BQ'
    RAW = 'RW'
    TYPE_CHOICES = [
        (BOILED, 'Boiled'),
        (FRIED, 'Fried'),
        (STEAMED, 'Steamed'),
        (BAKED, 'Baked'),
        (BARBEQUE, 'Barbeque'),
        (RAW, 'Raw'),
        (UNDECIDED, 'Not sure'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=UNDECIDED,
    )
    # Carbohydrates
    NOODLES = 'ND'
    RICE = 'RE'
    CAR_CHOICES = [
        (NOODLES, "Noodles"),
        (RICE, "Rice"),
        (UNDECIDED, "Not sure"),
    ]
    carbohydrate = models.CharField(
        max_length=2,
        choices=None,
        default=UNDECIDED,
    )
    # list of descriptions for phase 2
    # descriptions = []
