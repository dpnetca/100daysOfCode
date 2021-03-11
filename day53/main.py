#!/usr/bin/env python

from config import config
from data_entry import DataEntry
from property_finder import PropertyFinder


property_finder = PropertyFinder(config.zillow_url)
property_finder.get_property_list()

form = DataEntry(config.google_form_url)
form.input_list(property_finder.property_list)
form.quit()
